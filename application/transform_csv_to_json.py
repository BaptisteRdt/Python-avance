import csv
import json
import os

def csv_to_json(input_filename:str, output_filename:str):
    """Convert file.csv to file.json
    
    Args:
        - input_filename:str -> file.csv path
        - output_filename:str -> file.json path
  
    Returns:
        No returns
    """
    # Open file.csv and fill python objet row per row
    with open(input_filename, "r") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        data = [row for row in csv_reader]

    # Write python objet in json file
    with open(output_filename, "w") as jsonfile:
        json.dump(data, jsonfile)


def move_and_transform(name_csv:str, name_json:str):
    """
    Find the file.csv path and create a file.json path
    
    Args:
        - name_csv:str -> file.csv's name
        - name_json:str -> file.json's name
  
    Returns:
        No returns
    """
    # Path to file.csv
    input_file = os.path.join(os.getcwd(), "data", name_csv)

    # Path to file.json
    output_file = os.path.join(os.getcwd(), "data/json", name_json)

    # Convert file.csv to file.json
    csv_to_json(input_file, output_file)


def run():
    """
    Create a file.json per file.csv
    
    Args:
        No args
  
    Returns:
        No returns
    """
    for filename in os.listdir("data"):
        if filename.endswith(".csv"):
            output_filename = os.path.splitext(filename)[0] + ".json"
            move_and_transform(filename, output_filename)