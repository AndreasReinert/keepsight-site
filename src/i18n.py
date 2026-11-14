"""Übersetzungen der Webseite.

Englisch und Deutsch sind vollständige Inhaltsmodule. Alle anderen Sprachen bestehen aus einer
Datei `src/i18n/<code>.txt` mit Zeilen `Nummer|Text`: je eine Zeile pro Textstück des englischen
Inhalts. Hier werden die Textstücke nummeriert und für eine Sprache wieder eingesetzt.
"""
import json
import os
import re
import types

BLOCK = re.compile(r"<(h2|h3|p|li|th|td)(\s[^>]*)?>(.*?)</\1>", re.S)
KBD = re.compile(r"<kbd>(.*?)</kbd>")
TAG = re.compile(r"<[^>]+>")

# Muttersprachliche Namen für die Sprachwahl
NAMES = {
    "en": "English", "de": "Deutsch", "fr": "Français", "it": "Italiano", "es": "Español",
    "pt-BR": "Português (Brasil)", "nl": "Nederlands", "sv": "Svenska", "pl": "Polski",
    "ru": "Русский", "uk": "Українська", "tr": "Türkçe", "ar": "العربية", "hi": "हिन्दी",
    "id": "Bahasa Indonesia", "vi": "Tiếng Việt", "th": "ไทย", "ja": "日本語", "ko": "한국어",
    "zh-Hans": "简体中文", "zh-Hant": "繁體中文",
}
RTL = {"ar"}


def _fixed(text, en):
    """Textstücke ohne übersetzbaren Inhalt (Adresse, reine E-Mail-Verknüpfung, Zahlen)."""
    plain = TAG.sub("", text).replace("&nbsp;", " ").strip()
    if not plain or text.strip() == en.ADDRESS:
        return True
    if plain == en.MAIL:
        return True
    return not re.search(r"[A-Za-z]{2}", plain)


class Walker:
    """Geht den englischen Inhalt in fester Reihenfolge durch und ruft `leaf` für jedes Textstück."""

    def __init__(self, en, leaf):
        self.en, self.leaf = en, leaf

    def text(self, value):
        return value if _fixed(value, self.en) else self.leaf(value)

    def html(self, value):
        if not BLOCK.search(value):
            return self.text(value)

        def block(m):
            inner = m.group(3)
            if re.search(r"<(p|li|ul|ol|table|tr|td|th|h2|h3|div)\b", inner):
                return m.group(0)[: m.start(3) - m.start(0)] + BLOCK.sub(block, inner) + f"</{m.group(1)}>"
            return f"<{m.group(1)}{m.group(2) or ''}>{self.text(inner)}</{m.group(1)}>"

        return BLOCK.sub(block, value)

    def any(self, value):
        if isinstance(value, str):
            return self.html(value)
        if isinstance(value, bool) or value is None:
            return value
        if isinstance(value, dict):
            return {k: self.any(v) for k, v in value.items()}
        if isinstance(value, tuple):
            return tuple(self.any(v) for v in value)
        if isinstance(value, list):
            return [self.any(v) for v in value]
        return value

    def run(self):
        en = self.en
        out = types.SimpleNamespace(MAIL=en.MAIL, ADDRESS=en.ADDRESS)
        out.UI = {k: (v if k == "name" else self.any(v)) for k, v in en.UI.items()}
        out.HOME = self.any(en.HOME)
        out.DOCS = [(slug, self.text(title), self.text(short), self.html(text)) for slug, title, short, text in en.DOCS]
        out.SUPPORT, out.PRIVACY, out.IMPRINT = self.any(en.SUPPORT), self.any(en.PRIVACY), self.any(en.IMPRINT)
        out.SHOTS = self.any(en.SHOTS)
        return out


def segments(en):
    """Alle Textstücke des englischen Inhalts, ohne Doppelte, in fester Reihenfolge."""
    seen = {}

    def leaf(value):
        seen.setdefault(value, len(seen))
        return value

    Walker(en, leaf).run()
    return list(seen)


def tags(text):
    return sorted(re.sub(r"<kbd>.*?</kbd>", "<kbd></kbd>", t) for t in TAG.findall(KBD.sub("<kbd></kbd>", text)))


def load(code, en, app_strings=None, keep=()):
    """Inhalt einer Sprache: englische Struktur mit den Texten aus `src/i18n/<code>.txt`."""
    source = segments(en)
    path = os.path.join(os.path.dirname(__file__), "i18n", f"{code}.txt")
    lines = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line.strip():
                continue
            number, text = line.split("|", 1)
            lines[int(number)] = text.strip()
    problems = []
    table = {}
    for i, text in enumerate(source):
        if i not in lines:
            # Wörter, die genau so in der App stehen, kommen von dort; Eigennamen bleiben stehen
            value = (app_strings or {}).get(text, {}).get(code)
            if value:
                table[text] = value
            elif i not in keep:
                problems.append(f"{code}: Textstück {i} fehlt")
            continue
        if tags(lines[i]) != tags(text):
            problems.append(f"{code}: Textstück {i} hat andere Auszeichnungen als das Original")
        table[text] = lines[i]
    extra = set(lines) - set(range(len(source)))
    if extra:
        problems.append(f"{code}: überzählige Nummern {sorted(extra)[:5]}")

    def button(m):
        # Namen von Knöpfen kommen aus der App, damit Webseite und App gleich lauten
        label = m.group(1)
        value = (app_strings or {}).get(label, {}).get(code)
        return f"<kbd>{value or label}</kbd>"

    def leaf(value):
        return KBD.sub(button, table.get(value, value))

    out = Walker(en, leaf).run()
    out.UI["name"] = NAMES[code]
    return out, problems


def app_strings(path):
    """Texte der App je Sprache, für die Namen von Knöpfen."""
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as f:
        catalog = json.load(f)["strings"]
    return {key: {lang: unit["stringUnit"]["value"] for lang, unit in entry.get("localizations", {}).items()}
            for key, entry in catalog.items()}
