import json, csv

def csv_to_json():
    """
    Fonction qui transforme les données .csv en .json dans le fichier "données.json"

    Args:
        Pas de paramètres

    Returns:
        Pas de paramètres de retour 
    """
    données: dict = {} 

    try:
        #TO DO
        with open("nom_du_fichier.csv") as mon_fichier:
            lecteur_csv = csv.DictReader(mon_fichier)
            for id, ligne in enumerate(lecteur_csv):
                données[id] = ligne
    except FileNotFoundError:
        "Pas de tel fichier dans notre base de données"

    with open("données.json", "w", encoding='utf-8') as mon_fichier:
        mon_fichier.write(json.dumps(données, ensure_ascii=False, indent=4))