import urllib.request
import gzip
import shutil
from datetime import date
import os


# Specify the URL pattern
url_pattern = "https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/Archive/synop.{year}{month}.csv.gz"


def construct_url(year, month, url_pattern):
    """Construct the URL for the current year and month"""
    url = url_pattern.format(year=year, month=str(month).zfill(2))
    return url


def construct_filename(year, month):
    """Construct the filename for the current year and month"""
    filename = "synop.{year}{month}.csv".format(year=year, month=str(month).zfill(2))
    return filename


def download(url, year, month):
    """Downlaod the gzip file"""
    with urllib.request.urlopen(url) as response:
        with open(filename + ".gz", "wb") as outfile:
            outfile.write(response.read())


def decompress(filename):
    """Decompress the gzip file"""
    with gzip.open(filename + ".gz", "rb") as f_in:
        with open(filename, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)


def delete_gzip(filename):
    """Delete the gzip file to save disk space """
    os.remove(filename + ".gz")


def execute_data(url_pattern):
    """Construct url & filename, download the gzip file and decompress. Then delete the gzip"""
    for year in range(1996, date.today().year + 1):
        for month in range(1, 13):
            url = construct_url(year, month, url_pattern)
            filename = construct_filename(year, month)
            download(url, year, month)
            decompress(filename)
            delete_gzip(filename)

