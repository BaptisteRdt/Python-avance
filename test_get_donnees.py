import os
import pytest
from datetime import date

from get_donnees import (
    construct_url,
    construct_filename,
    download,
    decompress,
    delete_gzip,
)


@pytest.fixture(scope="module")
def test_data():
    test_url = "https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/Archive/synop.202201.csv.gz"
    test_year = 2022
    test_month = 1
    test_filename = "synop.202201.csv"

    yield (test_url, test_year, test_month, test_filename)

    os.remove(test_filename)


def test_construct_url():
    assert (
        construct_url(
            2022,
            1,
            url_pattern="https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/Archive/synop.{year}{month}.csv.gz",
        )
        == "https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/Archive/synop.202201.csv.gz"
    )


def test_construct_filename():
    assert construct_filename(2022, 1) == "synop.202201.csv"


def test_download(test_data):
    url, year, month, filename = test_data
    download(url, year, month, filename)
    assert os.path.exists(filename + ".gz")


def test_decompress(test_data):
    url, year, month, filename = test_data
    decompress(filename)
    assert os.path.exists(filename)


def test_delete_gzip(test_data):
    url, year, month, filename = test_data
    delete_gzip(filename)
    assert not os.path.exists(filename + ".gz")
