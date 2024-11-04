import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL der Wikipedia-Seite
url = "https://de.wikipedia.org/wiki/Liste_der_Olympiasieger_im_Fu%C3%9Fball"
response = requests.get(url)

# Sicherstellen, dass die Anfrage erfolgreich war
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
else:
    print("Fehler beim Laden der Seite.")

# Tabellen extrahieren
tables = soup.find_all("table", class_="wikitable")

# Liste zur Speicherung der Daten
olympic_data = []

# Daten aus den Tabellen extrahieren
for table in tables:
    rows = table.find_all("tr")
    for row in rows[1:]:  # Überspringen der Header-Zeile
        cells = row.find_all("td")
        if len(cells) >= 4:
            year = cells[0].text.strip()
            gold = cells[1].text.strip()
            silver = cells[2].text.strip()
            bronze = cells[3].text.strip()
            olympic_data.append({"Jahr": year, "Gold": gold, "Silber": silver, "Bronze": bronze})

# DataFrame erstellen und speichern
df = pd.DataFrame(olympic_data)

# Export der Daten
df.to_csv("/Users/lennartdreisbach/Data Science/Github/Olympic-Winners-Scraper/data/olympic_winners.csv", index=False)
df.to_json("/Users/lennartdreisbach/Data Science/Github/Olympic-Winners-Scraper/data/olympic_winners.json", orient="records")
