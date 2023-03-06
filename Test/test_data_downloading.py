import pytest

@pytest
def test_url_weather_data(url: str):
    assert url == "https://donneespubliques.meteofrance.fr/?fond=produit&id_produit=90&id_rubrique=32"

@pytest 
def test_data_in_database():
    assert True

