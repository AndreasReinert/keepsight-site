# keepsight-site

Öffentliche Webseite zur iOS-App Keepsight: Übersicht, Dokumentation, Support, Datenschutzerklärung und Impressum.
Veröffentlicht mit GitHub Pages aus dem Branch `main`.

- Inhalte: `src/content_de.py`, `src/content_en.py`
- Erzeugen: `python3 build.py` (schreibt die Ordner `de/` und `en/` sowie `index.html`)
- Neue Sprache: `src/content_xx.py` anlegen und in `build.py` unter `LANGS` eintragen
- Die Startadresse leitet auf die Sprache des Browsers weiter, sonst auf Englisch
