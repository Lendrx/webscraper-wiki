# Olympic Winners Scraper

![Olympic Winners Scraper](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Football_pictogram.svg/150px-Football_pictogram.svg.png) <!-- Beispiel-Link zu einem Bild, das geändert oder entfernt werden kann -->

## 📖 Übersicht

Der **Olympic Winners Scraper** ist ein Python-Projekt, das die Medaillengewinner der Olympischen Spiele im Fußball von der Wikipedia-Seite scrapt. Die gesammelten Daten werden in verschiedenen Formaten gespeichert, darunter CSV, JSON und Excel, um die Analyse und Visualisierung zu erleichtern.

## 🚀 Funktionen

- Scraping von Medaillengewinner-Daten für Fußball-Olympiaden.
- Speicherung der Daten in den Formaten CSV, JSON und Excel.
- Einfache Erweiterungen zur Anpassung und Verbesserung des Scraping-Prozesses.

## 📦 Voraussetzungen

- Python 3.x muss installiert sein.
- Internetverbindung für den Zugriff auf die Wikipedia-Seite.

## 📥 Installation

1. **Repository klonen:**

   ```bash
   git clone https://github.com/username/Olympic-Winners-Scraper.git
   ```

2. **In das Projektverzeichnis wechseln:**

   ```bash
   cd Olympic-Winners-Scraper
   ```

3. **Virtuelle Umgebung erstellen und aktivieren (optional):**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Auf macOS/Linux
   venv\Scripts\activate      # Auf Windows
   ```

4. **Benötigte Bibliotheken installieren:**

   ```bash
   pip install -r requirements.txt
   ```

## 🛠️ Nutzung

Führen Sie das Skript aus, um die Daten zu scrapen und in den angegebenen Formaten zu speichern:

```bash
python olympic_winners_scraper.py
```

Nach dem Ausführen des Skripts finden Sie die gescrapten Daten im `data/`-Ordner:

- `olympic_winners.csv`
- `olympic_winners.json`

## 📊 Beispielausgabe

Die Medaillengewinner werden in einem DataFrame gespeichert und in den folgenden Formaten bereitgestellt:

| Jahr | Gold          | Silber          | Bronze          |
|------|---------------|-----------------|------------------|
| 1900 | Großbritannien| Frankreich       | USA              |
| 1904 | USA           | Kanada           | Deutschland      |

## 🤝 Mitwirken

Beiträge sind willkommen! Bitte erstellen Sie einen Fork des Repositories, nehmen Sie Ihre Änderungen vor und senden Sie einen Pull-Request. Stellen Sie sicher, dass Ihre Änderungen gut dokumentiert sind und die Tests bestehen.

## 📝 Lizenz

Dieses Projekt ist lizenziert unter der MIT License. Weitere Informationen finden Sie in der [LICENSE](LICENSE)-Datei.
