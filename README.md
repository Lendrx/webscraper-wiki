# Wikipedia Scraper

## 🎯 Was macht es?
Automatisierter Scraper für Wikipedia-Artikel. Extrahiert strukturierte Daten aus Wikipedia-Seiten für Analysen und Datensätze.

## 🛠️ Wie ist es gebaut?
### Tech Stack:
- Python 3.x
- BeautifulSoup4
- Pandas
- Requests
- MongoDB

### Architektur-Highlights:
1. Intelligentes Rate-Limiting
2. Strukturierte Datenextraktion
3. Kategoriebasierte Filterung

## 📊 Technische Features
```python
def extract_article_data(url):
    content = fetch_wikipedia_page(url)
    data = {
        'title': extract_title(content),
        'sections': parse_sections(content),
        'references': extract_references(content)
    }
    return clean_and_validate(data)
```

Key Features:
- Parallele Artikel-Extraktion
- Automatische Kategorisierung
- Export in verschiedene Formate