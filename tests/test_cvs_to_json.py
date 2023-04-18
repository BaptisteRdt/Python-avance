import json, csv, pytest

@pytest
def test_file_names():
    données: dict = {}
    
    try:
        with open("nom_du_fichier.csv") as mon_fichier_csv:
            lecteur_csv = csv.DictReader(mon_fichier_csv)
            for id, ligne in enumerate(lecteur_csv):
                données[id] = ligne
    except FileNotFoundError:
        "Nom du fichier inconnu dans ce projet"

    with open("données.json", "w", encoding='utf-8') as mon_fichier_json:
        mon_fichier_json.write(json.dumps(données, ensure_ascii=False, indent=4))

    