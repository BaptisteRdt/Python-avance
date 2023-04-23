import os
import pytest
import gzip
from datetime import date

from project.get_donnees import (
    construct_url,
    construct_filename,
    download,
    decompress,
    delete_gzip,
)

with open("file_for_decompress.txt", "w") as f:
    f.write("test")
with open("file_for_decompress.txt", "rb") as f_in:
    with gzip.open("file_for_decompress.txt.gz", "wb") as f_out:
        f_out.writelines(f_in)
os.remove("file_for_decompress.txt")


@pytest.fixture(scope="module")
def test_data():
    test_url = "https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/Archive/synop.202201.csv.gz"
    test_year = 2022
    test_month = 1
    test_filename = "synop.202201.csv"

    yield (test_url, test_year, test_month, test_filename)


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
    assert construct_filename(2022, 1) == "./data/synop.202201.csv"


def test_download(test_data):
    url, year, month, filename = test_data
    download(url, year, month, filename)
    assert os.path.exists(filename + ".gz")


def test_decompress():
    decompress("file_for_decompress.txt")
    assert os.path.exists("file_for_decompress.txt")


def test_delete_gzip():
    with open("file.txt", "w") as f:
        f.write("test")
    with open("file.txt", "rb") as f_in:
        with gzip.open("file.txt.gz", "wb") as f_out:
            f_out.writelines(f_in)
    os.remove("file.txt")
    delete_gzip("file.txt")
    assert not os.path.exists("file.txt" + ".gz")
