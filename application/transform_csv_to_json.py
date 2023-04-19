import csv
import json
import os

def csv_to_json(input_filename:str, output_filename:str):
    """Convert file.csv to file.json"""
    with open(input_filename, "r") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        data = [row for row in csv_reader]

    # Écrire les données dans un fichier JSON
    with open(output_filename, "w") as jsonfile:
        json.dump(data, jsonfile)


def move_and_transform(name_csv:str, name_json:str):
    """
    
    
    Args:
        - 
  
    Returns:
        -
    """
    # Chemin d'accès au fichier CSV d'entrée
    input_file = os.path.join(os.getcwd(), "data", name_csv)

    # Chemin d'accès au fichier JSON de sortie
    output_file = os.path.join(os.getcwd(), "data_json", name_json)

    # Convertir le fichier CSV en JSON
    csv_to_json(input_file, output_file)


def execute_all():
    """
    
    
    Args:
        - 
  
    Returns:
        -
    """
    for filename in os.listdir("data"):
        if filename.endswith(".csv"):
            output_filename = os.path.splitext(filename)[0] + ".json"
            move_and_transform(filename, output_filename)