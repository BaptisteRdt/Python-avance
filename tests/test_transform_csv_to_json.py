import os
import json
import pytest

from application.data_loading.transform_csv_to_json import (
    csv_to_json,
    move_and_transform,
)


@pytest.fixture
def csv_data():
    return [
        {"Name": "Simon", "Age": "21", "City": "Perigueux"},
        {"Name": "Quentin", "Age": "21", "City": "Bordeaux"},
    ]


def test_csv_to_json(tmpdir, csv_data):
    # Créer un fichier CSV temporaire
    csv_file = tmpdir.join("test_data.csv")
    with csv_file.open("w") as f:
        f.write("Name,Age,City\n")
        f.write("Simon,21,Perigueux\n")
        f.write("Quentin,21,Bordeaux\n")

    # Convertir le fichier CSV en JSON
    json_file = tmpdir.join("test_data.json")
    csv_to_json(str(csv_file), str(json_file))

    # Vérifier que le fichier JSON est créé et contient les données attendues
    assert os.path.isfile(str(json_file))
    with json_file.open("r") as f:
        data = json.load(f)
    assert data == csv_data


def test_move_and_transform(tmpdir, csv_data):
    # Créer un fichier CSV temporaire
    csv_file = tmpdir.join("test_data.csv")
    with csv_file.open("w") as f:
        f.write("Name,Age,City\n")
        f.write("Simon,21,Perigueux\n")
        f.write("Quentin,21,Bordeaux\n")

    # Déplacer et transformer le fichier CSV en JSON
    move_and_transform(str(csv_file), "test_data.json")

    # Vérifier que le fichier JSON est créé et contient les données attendues
    json_file = tmpdir.join("data_json", "test_data.json")
    assert os.path.isfile(str(json_file))
    with json_file.open("r") as f:
        data = json.load(f)
    assert data == csv_data
