import urllib.request
import gzip
import shutil
from datetime import date
import os


def construct_url(year, month, url_pattern):
    """
    Construct the URL for the current year and month
    
    Args:
        - year:int -> year of the weather data we need
        - month:int -> month of the weather data we need

    Returns:
        - str -> the URL with the month and year of the data needed
    """
    url = url_pattern.format(year=year, month=str(month).zfill(2))
    return url


def construct_filename(year, month):
    """
    Construct the filename for the current year and month
    
    Args:
        - 
  
    Returns:
        -
    """
    filename = "./application/data/csv/synop.{year}{month}.csv".format(
        year=year, month=str(month).zfill(2)
    )
    return filename


def download(url, filename):
    """Downlaod the gzip file
    
    Args:
        - 

    Returns:
        -
    """
    with urllib.request.urlopen(url) as response:
        with open(filename + ".gz", "wb") as outfile:
            outfile.write(response.read())


def decompress(filename):
    """Decompress the gzip file
    
    Args:
        - 

    Returns:
        -
    """
    with gzip.open(filename + ".gz", "rb") as f_in:
        with open(filename, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)


def delete_gzip(filename):
    """Delete the gzip file to save disk space 
    
    Args:
        - 

    Returns:
        -
    """
    os.remove(filename + ".gz")

def run(weather_url):
    """Construct url & filename, download the gzip file and decompress. Then delete the gzip
    
    Args:
        - url:str -> 

    Returns:
        No returns 
    """
    for year in range(1996, date.today().year + 1):
        for month in range(1, 13):
            url = construct_url(year, month, weather_url)
            filename = construct_filename(year, month)
            download(url, filename)
            decompress(filename)
            delete_gzip(filename)