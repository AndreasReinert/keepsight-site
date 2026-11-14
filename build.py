"""Erzeugt die Keepsight-Webseite aus src/content_<sprache>.py.

Aufruf: python3 build.py
Neue Sprache: src/content_xx.py anlegen (Aufbau wie content_en.py) und unten in LANGS eintragen.
"""
import html
import importlib
import os
import shutil
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
LANGS = ["de", "en"]
FALLBACK = "en"
C = {lang: importlib.import_module(f"content_{lang}") for lang in LANGS}

PLANE = ('<svg class="plane" viewBox="0 0 120 50" aria-hidden="true"><path fill="currentColor" d="M4 27l20-4 30-1 '
         '22-18h9l-12 18 30 1c8 0 13 3 13 5s-5 4-13 4l-30 1 12 14h-9L54 33l-30-1-10 9H8l5-11z"/></svg>')


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
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
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
    body = f"""<main class="wrap">
<section class="hero">
<div><h1>{c["h1"]}</h1><p class="lead">{c["lead"]}</p>
<a class="cta" href="docs/index.html">{c["cta"]}</a><span class="note">{c["note"]}</span></div>
<figure class="finder" style="margin:0">
<div class="cloud" style="left:8%;top:18%;width:30%;height:9%"></div>
<div class="cloud" style="left:55%;top:62%;width:38%;height:11%"></div>
<div class="cloud" style="left:62%;top:12%;width:20%;height:7%"></div>
{PLANE}<div class="crop"></div><div class="box"></div>
<div class="pill">{ui["finder_status"]}</div>
<figcaption>{ui["finder_caption"]}</figcaption>
<div class="chips"><span>A</span><span>.5×</span><span>1×</span><span class="on">5×</span></div>
</figure>
</section>
<section class="band"><h2>{c["what_h"]}</h2><div class="rows">{rows}</div></section>
<section class="band"><h2>{c["cam_h"]}</h2><div class="lens">{cam}</div></section>
<section class="band"><h2>{c["price_h"]}</h2><p style="max-width:62ch;color:var(--soft)">{c["price_p"]}</p>
<table><tr><th>{cols[0]}</th><th>{cols[1]}</th><th>{cols[2]}</th></tr>{price}</table>
<p style="color:var(--soft)">{c["price_note"]}</p></section>
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
        return f'<nav class="toc" aria-label="{ui["docs_title"]}"><ol>{items}</ol></nav>'

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
<article class="doc"><h1>{title}</h1><p class="lead">{short}</p>{text}{pager}</article></div></main>"""
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
      var code = String(wanted[i]).toLowerCase().split('-')[0];
      if (available.indexOf(code) >= 0) chosen = code;
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
    print("Seiten:", sum(len(files) for lang in LANGS for _, _, files in os.walk(lang)) + 3)


if __name__ == "__main__":
    main()
