"""Erzeugt die Keepsight-Webseite aus src/content_<sprache>.py.

Aufruf: python3 build.py
Englisch und Deutsch sind vollständige Module (src/content_en.py, src/content_de.py). Alle anderen
Sprachen liegen als src/i18n/<code>.txt vor: eine Zeile `Nummer|Text` je Textstück des englischen
Inhalts (siehe src/i18n.py). Namen von Knöpfen kommen aus den Texten der App (src/app_strings.json,
eine Kopie von ios/Keepsight/Localizable.xcstrings).
"""
import html
import json
import importlib
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
import i18n  # noqa: E402

FULL = ["de", "en"]
FALLBACK = "en"
C = {lang: importlib.import_module(f"content_{lang}") for lang in FULL}
# Textstücke, die in jeder Sprache gleich lauten (Eigennamen, Masse, Pfade und Bildnamen)
KEEP_TEXTS = {"48 MP", "Pro", "iPhone", "Bluetooth", "Insta360 Flow Pro and Flow 2 Pro", "Apple DockKit",
              "DJI Osmo Mobile 8", "Belkin Auto-Tracking Stand Pro", "FeiyuTech AK4500", "1× (24 mm)", "12 MP",
              "Original", "Stratux (JSON)", "GDL90 (UDP)",
              "<kbd>Auto</kbd> <kbd>Pro</kbd>", "ISO", "<kbd>Off</kbd> <kbd>On</kbd>"}
KEEP = [i for i, text in enumerate(i18n.segments(C["en"]))
        if text in KEEP_TEXTS or text.startswith("docs/") or text.startswith("story-")]
SITE = "https://andreasreinert.github.io/keepsight-site/"
ORDER = ["en", "de", "fr", "it", "es", "pt-BR", "nl", "sv", "pl", "ru", "uk", "tr", "ar", "hi", "id", "vi", "th",
         "ja", "ko", "zh-Hans", "zh-Hant"]
_app = i18n.app_strings(os.path.join(os.path.dirname(__file__), "src", "app_strings.json"))
PROBLEMS = []
for _code in ORDER:
    if _code in FULL or not os.path.exists(os.path.join(os.path.dirname(__file__), "src", "i18n", f"{_code}.txt")):
        continue
    C[_code], _problems = i18n.load(_code, C["en"], _app, KEEP)
    PROBLEMS += _problems
LANGS = [code for code in ORDER if code in C]


def _app_buttons(lang):
    """Deutsch ist ein eigenes Inhaltsmodul: Knopfnamen, die dort englisch stehen, kommen aus der App."""
    def button(m):
        return f"<kbd>{_app.get(m.group(1), {}).get(lang) or m.group(1)}</kbd>"
    C[lang].DOCS = [(slug, title, short, i18n.KBD.sub(button, text)) for slug, title, short, text in C[lang].DOCS]


for _code in FULL:
    if _code != "en":
        _app_buttons(_code)

def page(lang, rel, title, description, body, current):
    """Schreibt eine Seite. `rel` ist der Pfad innerhalb des Sprachordners."""
    ui = C[lang].UI
    depth = rel.count("/")
    up = "../" * depth            # zum Sprachordner
    root = up + "../"             # zur Wurzel der Seite
    options = "".join(
        f'<option value="{root}{code}/{rel}" data-lang="{code}"{" selected" if code == lang else ""}>'
        f'{C[code].UI["name"]}</option>' for code in LANGS)
    alternates = "".join(f'<link rel="alternate" hreflang="{code}" href="{root}{code}/{rel}">' for code in LANGS)

    def nav(key, href, label):
        mark = ' aria-current="page"' if current == key else ""
        return f'<a href="{up}{href}"{mark}>{label}</a>'

    out = f"""<!DOCTYPE html>
<html lang="{lang}"{' dir="rtl"' if lang in i18n.RTL else ""}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="canonical" href="{SITE}{lang}/{rel}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Keepsight">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:url" content="{SITE}{lang}/{rel}">
<meta property="og:image" content="{SITE}img/social.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{html.escape(C[lang].SHOTS["hero"])}">
<meta name="twitter:card" content="summary_large_image">
{alternates}
<link rel="icon" href="{root}icon.png">
<link rel="stylesheet" href="{root}assets/site.css">
</head>
<body>
<header class="top">
<a class="brand" href="{up}index.html"><img src="{root}icon.png" alt="">Keepsight</a>
<nav>{nav("home", "index.html", ui["nav_home"])}{nav("docs", "docs/index.html", ui["nav_docs"])}{nav("support", "support.html", ui["nav_support"])}</nav>
<select class="lang" aria-label="{ui["language"]}">{options}</select>
</header>
{body}
<footer class="foot"><span>© 2026 Andreas Reinert</span>
<a href="{up}docs/index.html">{ui["nav_docs"]}</a><a href="{up}support.html">{ui["nav_support"]}</a>
<a href="{up}privacy.html">{ui["privacy"]}</a><a href="{up}imprint.html">{ui["imprint"]}</a></footer>
<script src="{root}assets/site.js"></script>
</body>
</html>
"""
    path = os.path.join(lang, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(out)


with open(os.path.join(os.path.dirname(__file__), "campaign.json"), encoding="utf-8") as _f:
    CAMPAIGN = json.load(_f)


def campaign(c):
    """Preisauftritt nach Zustand: PRELAUNCH, UNVERIFIED, INTRO_ACTIVE oder REGULAR.

    Eine Stelle (campaign.json). Der Wechsel vom Einführungs- zum Normalpreis geschieht beim Aufruf
    der Seite nach Schweizer Datum, ohne neuen Build. Kein Countdown, kein durchgestrichener Preis,
    keine Ersparnis in Prozent. Ohne geprüften Preis steht nur, dass der App Store den Preis zeigt.
    """
    t = c["campaign"]
    url = CAMPAIGN.get("appStoreUrl")
    swiss = f'<p class="fine">{t["swiss"]}</p>'
    if not url:
        planned = f'<p>{t["prelaunch"]}</p>{swiss}' if CAMPAIGN.get("announcePlannedPrice") else ""
        return f'<div class="offer" data-campaign="PRELAUNCH"><p><strong>{c["note"]}</strong></p>{planned}</div>'
    button = f'<p><a class="cta" href="{html.escape(url)}">{t["store"]}</a></p>'
    if not CAMPAIGN.get("priceVerified"):
        return f'<div class="offer" data-campaign="UNVERIFIED"><p>{t["unverified"]}</p>{button}</div>'
    intro = t["intro"]
    return (f'<div class="offer" data-campaign="DATED" data-intro-ends="{CAMPAIGN["introEndsInclusive"]}" '
            f'data-zone="{CAMPAIGN["timeZone"]}">'
            f'<div data-state="none"><p>{t["unverified"]}</p></div>'
            f'<div data-state="INTRO_ACTIVE" hidden><p><strong>{intro[0]}</strong></p><p>{intro[1]} {intro[2]}</p>{swiss}</div>'
            f'<div data-state="REGULAR" hidden><p><strong>{t["regular"]}</strong></p>{swiss}</div>{button}</div>'
            """<script>(function(){var e=document.querySelector('[data-campaign="DATED"]');if(!e)return;
try{var d=new Intl.DateTimeFormat('en-CA',{timeZone:e.dataset.zone}).format(new Date());
var s=d<=e.dataset.introEnds?'INTRO_ACTIVE':'REGULAR';
e.querySelectorAll('[data-state]').forEach(function(n){n.hidden=n.dataset.state!==s});}catch(x){}})();</script>""")


def picture(lang, name, up, sizes, eager=False):
    """Ein Bild im Querformat in drei Breiten. Feste Masse, damit beim Laden nichts springt."""
    alt = html.escape(C[lang].SHOTS[name])
    srcset = ", ".join(f"{up}img/{name}-{w}.webp {w}w" for w in (640, 1100, 1672))
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return (f'<img src="{up}img/{name}-1100.webp" srcset="{srcset}" sizes="{sizes}" width="1672" height="941" '
            f'{load} alt="{alt}">')


def home(lang):
    c, ui = C[lang].HOME, C[lang].UI
    rows = "".join(f'<div class="row"><h3>{t}</h3><p>{p}</p></div>' for t, p in c["what"])
    cam = "".join(f"<div><b>{n}</b><span>{t}</span></div>" for n, t in c["cam"])
    need = "".join(f'<div class="row"><h3>{t}</h3><p>{p}</p></div>' for t, p in c["need"])
    cols = c["price_cols"]
    yes = {"de": "Ja", "en": "Yes"}.get(lang, "✓")
    no = {"de": "Nein", "en": "No"}.get(lang, "–")
    price = "".join(
        f'<tr><td>{name}</td><td{" class=y" if free else ""}>{yes if free else no}</td><td class="y">{yes}</td></tr>'
        for name, free, _ in c["price_rows"])
    tries = "".join(f"<li>{t}</li>" for t in c["try"])
    faq = "".join(f'<div class="row"><h3>{q}</h3><p>{a}</p></div>' for q, a in c["faq"])
    how = "".join(f"<li><h3>{t}</h3><p>{p}</p></li>" for t, p in c["how"])
    stories = ""
    for image, title, text, href, label in c["stories"]:
        figure = (f'<figure>{picture(lang, image, "../", "(max-width: 860px) 100vw, 560px")}</figure>'
                  if image else "")
        stories += (f'<article class="story{"" if image else " lead"}">{figure}<div><h3>{title}</h3><p>{text}</p>'
                    f'<p><a href="{href}">{label}</a></p></div></article>')
    body = f"""<main class="wrap">
<section class="hero">
<div><h1>{c["h1"]}</h1><p class="lead">{c["lead"]}</p>
<a class="cta" href="docs/index.html">{c["cta"]}</a><span class="note">{c["free_line"]} {c["note"]}</span></div>
<figure class="heroimg">{picture(lang, "hero", "../", "(max-width: 860px) 100vw, 640px", eager=True)}</figure>
</section>
<section class="band"><h2>{c["how_h"]}</h2><ol class="steps">{how}</ol></section>
<section class="band"><h2>{c["stories_h"]}</h2><div class="stories">{stories}</div>
<p class="fine">{c["stories_note"]}</p></section>
<section class="band"><h2>{c["what_h"]}</h2><div class="rows">{rows}</div></section>
<section class="band"><h2>{c["cam_h"]}</h2><div class="lens">{cam}</div></section>
<section class="band"><h2>{c["shots_h"]}</h2>{shots(lang, ["tracking-help", "camera", "format-video"], "../")}</section>
<section class="band"><h2>{c["price_h"]}</h2><p style="max-width:62ch;color:var(--soft)">{c["price_p"]}</p>
<table><tr><th>{cols[0]}</th><th>{cols[1]}</th><th>{cols[2]}</th></tr>{price}</table>
<p style="color:var(--soft)">{c["price_note"]}</p>
<div class="plans"><div class="plan"><h3>{c["try_h"]}</h3><ul>{tries}</ul></div>
<div class="plan pro"><h3>Keepsight Pro</h3><p>{c["pro_card"]}</p>{campaign(c)}</div></div></section>
<section class="band"><h2>{c["faq_h"]}</h2><div class="rows">{faq}</div></section>
<section class="band"><h2>{c["need_h"]}</h2><div class="rows">{need}</div></section>
</main>"""
    page(lang, "index.html", c["title"], c["description"], body, "home")


def docs(lang):
    c, ui = C[lang], C[lang].UI
    chapters = c.DOCS

    def toc(active):
        items = "".join(
            f'<li><a href="{slug}.html"{" aria-current=page" if slug == active else ""}>{title}</a></li>'
            for slug, title, _, _ in chapters)
        number = next((i for i, ch in enumerate(chapters, 1) if ch[0] == active), None)
        current = f"{number} · {chapters[number - 1][1]}" if number else ui["chapters"]
        # Schmale Bildschirme: aufklappbare Kapitelliste; breite: feste Spalte
        return (f'<details class="tocm"><summary><span>{ui["chapters"]}</span><b>{current}</b></summary>'
                f'<ol>{items}</ol></details>'
                f'<nav class="toc" aria-label="{ui["docs_title"]}"><ol>{items}</ol></nav>')

    overview = "".join(f'<li><a href="{slug}.html"><span><b>{title}</b><span>{short}</span></span></a></li>'
                       for slug, title, short, _ in chapters)
    body = f"""<main class="wrap"><div class="docs">{toc(None)}
<article class="doc"><h1>{ui["docs_title"]}</h1><p class="lead">{ui["docs_lead"]}</p>
<ol class="chapters">{overview}</ol></article></div></main>"""
    page(lang, "docs/index.html", f'{ui["docs_title"]} – Keepsight', ui["docs_lead"], body, "docs")

    for i, (slug, title, short, text) in enumerate(chapters):
        prev = chapters[i - 1] if i > 0 else None
        nxt = chapters[i + 1] if i + 1 < len(chapters) else None
        pager = '<nav class="pager">'
        pager += f'<a href="{prev[0]}.html"><small>{ui["prev"]}</small>{prev[1]}</a>' if prev else "<span></span>"
        pager += (f'<a href="{nxt[0]}.html" style="text-align:right"><small>{ui["next"]}</small>{nxt[1]}</a>'
                  if nxt else "<span></span>")
        pager += "</nav>"
        body = f"""<main class="wrap"><div class="docs">{toc(slug)}
<article class="doc"><h1>{title}</h1><p class="lead">{short}</p>{expand(lang, text, "../../")}{pager}</article></div></main>"""
        page(lang, f"docs/{slug}.html", f"{title} – Keepsight", short, body, "docs")


def simple(lang, rel, block, current):
    lead = f'<p class="lead">{block["lead"]}</p>' if block["lead"] else ""
    body = f'<main class="wrap"><article class="doc" style="padding:28px 0 72px"><h1>{block["title"]}</h1>{lead}{block["body"]}</article></main>'
    page(lang, rel, f'{block["title"]} – Keepsight', block["lead"] or block["title"], body, current)


def redirect(path, target):
    with open(path, "w", encoding="utf-8") as f:
        f.write(f'<!DOCTYPE html><html><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url={target}">'
                f'<link rel="canonical" href="{target}"><title>Keepsight</title></head>'
                f'<body><a href="{target}">Keepsight</a></body></html>\n')


def root_index():
    links = " · ".join(f'<a href="{code}/">{C[code].UI["name"]}</a>' for code in LANGS)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(f"""<!DOCTYPE html>
<html lang="{FALLBACK}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Keepsight</title>
<script>
// Sprache: zuerst die gemerkte Wahl, dann die Sprachen des Browsers, sonst Englisch
(function () {{
  var available = {LANGS!r}, chosen = null;
  try {{ chosen = localStorage.getItem('ks-lang'); }} catch (e) {{}}
  if (available.indexOf(chosen) < 0) {{
    chosen = null;
    var wanted = navigator.languages && navigator.languages.length ? navigator.languages : [navigator.language || ''];
    for (var i = 0; i < wanted.length && !chosen; i++) {{
      var tag = String(wanted[i]).toLowerCase(), code = tag.split('-')[0];
      if (code === 'zh') chosen = /hant|tw|hk|mo/.test(tag) ? 'zh-Hant' : 'zh-Hans';
      else if (code === 'pt') chosen = 'pt-BR';
      else if (available.indexOf(code) >= 0) chosen = code;
      if (available.indexOf(chosen) < 0) chosen = null;
    }}
  }}
  location.replace((chosen || '{FALLBACK}') + '/' + location.hash);
}})();
</script>
<noscript><meta http-equiv="refresh" content="0; url={FALLBACK}/"></noscript>
</head>
<body><p>Keepsight: {links}</p></body>
</html>
""")


def shots(lang, names, up):
    """Bildschirmfotos nebeneinander. Bild der Sprache, wenn vorhanden, sonst das englische."""
    caps = C[lang].SHOTS
    out = []
    for name in names:
        file = f"{name}-{lang}.webp" if os.path.exists(f"img/{name}-{lang}.webp") else f"{name}-en.webp"
        cap = html.escape(caps[name])
        out.append(f'<figure><img src="{up}img/{file}" width="600" height="1300" loading="lazy" alt="{cap}">'
                   f"<figcaption>{cap}</figcaption></figure>")
    return f'<div class="shots n{len(names)}">' + "".join(out) + "</div>"


def wide(lang, name, up):
    """Ein Bild im Querformat über die Textbreite.

    Bilder mit eingebettetem englischem Text gibt es als `<name>-en`; alle anderen Sprachen bekommen
    dann die Fassung ohne Text (`<name>-intl`). Illustrationen liegen in drei Breiten vor.
    """
    cap = html.escape(C[lang].SHOTS[name])
    variant = name
    if os.path.exists(f"img/{name}-en-1100.webp"):
        variant = f"{name}-en" if lang == "en" else f"{name}-intl"
    if os.path.exists(f"img/{variant}-1100.webp"):
        srcset = ", ".join(f"{up}img/{variant}-{w}.webp {w}w" for w in (640, 1100, 1672))
        img = (f'<img src="{up}img/{variant}-1100.webp" srcset="{srcset}" sizes="(max-width: 860px) 100vw, 760px" '
               f'width="1672" height="941" loading="lazy" decoding="async" alt="{cap}">')
    else:
        file = f"{name}-{lang}.webp" if os.path.exists(f"img/{name}-{lang}.webp") else f"{name}-en.webp"
        img = f'<img src="{up}img/{file}" width="1672" height="941" loading="lazy" alt="{cap}">'
    return f'<figure class="wide">{img}<figcaption>{cap}</figcaption></figure>'


def expand(lang, text, up):
    text = re.sub(r"\[\[wide ([^\]]+)\]\]", lambda m: wide(lang, m.group(1).strip(), up), text)
    return re.sub(r"\[\[shots ([^\]]+)\]\]", lambda m: shots(lang, m.group(1).split(), up), text)


def main():
    for lang in LANGS:
        shutil.rmtree(lang, ignore_errors=True)
        home(lang)
        docs(lang)
        simple(lang, "support.html", C[lang].SUPPORT, "support")
        simple(lang, "privacy.html", C[lang].PRIVACY, None)
        simple(lang, "imprint.html", C[lang].IMPRINT, None)
    root_index()
    # Alte Adressen weiterleiten
    redirect("datenschutz.html", "de/privacy.html")
    redirect("impressum.html", "de/imprint.html")
    for line in PROBLEMS:
        print("Übersetzung:", line)
    print("Sprachen:", len(LANGS))
    print("Seiten:", sum(len(files) for lang in LANGS for _, _, files in os.walk(lang)) + 3)


if __name__ == "__main__":
    main()
