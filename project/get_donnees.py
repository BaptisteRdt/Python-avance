import urllib.request
import gzip
import shutil
from datetime import date
import os


def construct_url(year, month, url_pattern):
    """Construct the URL for the current year and month"""
    url = url_pattern.format(year=year, month=str(month).zfill(2))
    return url


def construct_filename(year, month):
    """Construct the filename for the current year and month"""
    filename = "./data/csv/synop.{year}{month}.csv".format(
        year=year, month=str(month).zfill(2)
    )
    return filename


def download(url, year, month, filename):
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

