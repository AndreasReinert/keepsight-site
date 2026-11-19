# keepsight-site

Öffentliche Webseite zur iPhone-App **Keepsight: AI Gimbal Tracking**: Übersicht, Dokumentation, Support,
Datenschutzerklärung und Impressum. Veröffentlicht mit GitHub Pages aus dem Branch `main`:
<https://andreasreinert.github.io/keepsight-site/>

Keepsight hält Menschen und andere Motive automatisch im Bild und filmt dabei. Menschen filmen ist gratis
(ohne Gimbal oder mit einem DockKit-Gimbal); Keepsight Pro bringt 4K ohne Logo, weitere Motive, den
FeiyuTech AK4500 und die Profi-Werkzeuge.

## Aufbau

- `src/content_en.py`, `src/content_de.py`: vollständige Inhalte auf Englisch und Deutsch
- `src/i18n/<Sprache>.txt`: 19 weitere Sprachen als nummerierte Textstücke (`Nummer|Text`), nummeriert nach
  den Textstücken des englischen Inhalts
- `src/app_strings.json`: Kopie der App-Texte (`Localizable.xcstrings`). Knopfnamen in `<kbd>…</kbd>` und
  Textstücke, die es wörtlich in der App gibt, werden daraus übersetzt
- `img/`: Bilder. Bildschirmfotos heissen `<name>-<sprache>.webp`; fehlt die Sprache, wird das englische Bild
  benutzt, fehlt auch das, entfällt das Bild
- `build.py`: erzeugt alle Seiten

## Erzeugen

```sh
python3 build.py
```

Schreibt je Sprache einen Ordner (`en/`, `de/`, …) sowie `index.html`. Die Startadresse leitet auf die
Sprache des Browsers weiter, sonst auf Englisch. Fehlt in einer Sprache ein Textstück, meldet `build.py` es.

## Ändern

- Text ändern: zuerst in `content_en.py` und `content_de.py`, dann die betroffenen Textstücke in allen
  Dateien unter `src/i18n/` nachziehen (die Nummern verschieben sich, wenn Textstücke hinzukommen oder wegfallen)
- Nach Änderungen an den App-Texten `src/app_strings.json` neu aus der App kopieren
