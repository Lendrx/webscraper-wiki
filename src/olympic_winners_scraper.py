import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import os

# URL der Wikipedia-Seite
url = "https://de.wikipedia.org/wiki/Liste_der_Olympiasieger_im_Fu%C3%9Fball"
response = requests.get(url)

# Sicherstellen, dass die Anfrage erfolgreich war
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
else:
    raise Exception("Fehler beim Laden der Seite.")

# Tabellen extrahieren
tables = soup.find_all("table", class_="wikitable")

# Strukturierte Daten als hierarchisches Dictionary
structured_data = {}

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

            # Initialisiere das Jahr, wenn es nicht existiert
            if year not in structured_data:
                structured_data[year] = {
                    "Gold": [],
                    "Silber": [],
                    "Bronze": []
                }

            # Werte zuordnen
            structured_data[year]["Gold"].append(gold)
            structured_data[year]["Silber"].append(silver)
            structured_data[year]["Bronze"].append(bronze)

# Ordner erstellen, falls nicht vorhanden
os.makedirs("data", exist_ok=True)

# JSON speichern
with open("data/olympic_winners.json", "w", encoding="utf-8") as json_file:
    json.dump(structured_data, json_file, indent=4, ensure_ascii=False)

# Für Übersichtlichkeit auch in einem DataFrame speichern und als CSV exportieren
df = pd.DataFrame([
    {"Jahr": year, "Gold": ", ".join(data["Gold"]), "Silber": ", ".join(data["Silber"]), "Bronze": ", ".join(data["Bronze"])}
    for year, data in structured_data.items()
])
df.to_csv("data/olympic_winners.csv", index=False, encoding="utf-8")
df.to_csv("data/olympic_winners.csv", index=False, encoding="utf-8")

print("Daten erfolgreich exportiert.")
