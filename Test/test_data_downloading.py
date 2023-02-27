import pytest

@pytest
def test_url_valide(url: str):
    assert url == "https://donneespubliques.meteofrance.fr/?fond=produit&id_produit=90&id_rubrique=32"

