import json, csv

def csvToJson(nom_dossier: str):    
    """
    Fonction qui transforme les données .csv en .json dans le fichier "données.json"

    Args:
        nom_dossier:str -> Nom du dossier dans lequel les fichiers csv sont rangés.

    Returns:
        Pas de paramètres de retour 
    """
    données: dict = {}
    
    try:
        with open("nom_du_fichier.csv") as mon_fichier:
            lecteur_csv = csv.DictReader(mon_fichier)
            for id, ligne in enumerate(lecteur_csv):
                données[id] = ligne
    except FileNotFoundError:
        "Nom du fichier inconnu dans ce projet"

    with open("application/données.json", "w", encoding='utf-8') as mon_fichier:
        mon_fichier.write(json.dumps(données, ensure_ascii=False, indent=4))