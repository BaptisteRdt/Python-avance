import csv
import json
import os
from datetime import date


def csv_to_json(path_filename_csv: str, path_filename_json: str):
    """Convert file.csv to file.json
    
    Args:
        - input_filename:str -> file.csv path
        - output_filename:str -> file.json path
  
    Returns:
        No returns
    """
    # Open file.csv and fill python objet row per row
    with open(path_filename_csv, "r") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        data = [row for row in csv_reader]

    # Write python objet in json file
    with open(path_filename_json, "w") as jsonfile:
        json.dump(data, jsonfile)


def move_and_transform(name_csv: str, name_json: str):
    """
    Find the file.csv path and create a file.json path
    
    Args:
        - name_csv:str -> file.csv's name
        - name_json:str -> file.json's name
  
    Returns:
        No returns
    """
    # Path to file.csv
    path_filename_csv = os.path.join(os.getcwd(), "data/csv", name_csv)

    # Path to file.json
    path_filename_json = os.path.join(os.getcwd(), "data/json", name_json)

    # Convert file.csv to file.json
    csv_to_json(path_filename_csv, path_filename_json)


def run():
    """
    Create a file.json per file.csv
    
    Args:
        No args
  
    Returns:
        No returns
    """
    list_files: list = []
    for filename in os.listdir("data/json"):
        list_files.append(filename)

    for filename in os.listdir("data/csv"):
        output_filename = os.path.splitext(filename)[0] + ".json"
        year = output_filename[6:10]
        month = output_filename[10:12]
        
        if output_filename not in list_files or (date.today().year == year and date.today().month == month):
            move_and_transform(filename, output_filename)