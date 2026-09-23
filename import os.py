import csv
import json

csv_file = "images_dates.csv"   # ton fichier CSV
output_file = "data.js"

data = []

with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    for row in reader:
        data.append({
            "file": "img/" + row["nom_fichier"],
            "date": row["date"],
            "tags": [],
            "site": "",
            "auteur": "",
            "note": ""
        })

# écriture JS
with open(output_file, "w", encoding="utf-8") as f:
    f.write("const data = ")
    f.write(json.dumps(data, ensure_ascii=False, indent=2))
    f.write(";")

print("✔ data.js généré")