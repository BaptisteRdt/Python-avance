import urllib.request
import gzip
import shutil
from datetime import date
import os

def construct_url(year:int, month:int, url_pattern:str):
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

def construct_filename(year:int, month:int):
    """
    Construct the filename for the current year and month
    
    Args:
        - year:int -> year of the weather data we need
        - month:int -> month of the weather data we need
  
    Returns:
        - str -> filename.csv
    """
    filename = "./data/csv/synop.{year}{month}.csv".format(
        year=year, month=str(month).zfill(2)
    )
    return filename

def download(url:str, filename:str):
    """
    Downlaod the gzip file
    
    Args:
        - url:str -> url where we need to download data
        - filename:str -> filename.csv
    Returns:
        No returns
    """
    with urllib.request.urlopen(url) as response:
        with open(filename + ".gz", "wb") as outfile:
            outfile.write(response.read())

def decompress(filename:str):
    """
    Decompress the gzip file
    
    Args:
        - filename:str -> filename.csv
    Returns:
        No returns
    """
    with gzip.open(filename + ".gz", "rb") as f_in:
        with open(filename, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)

def delete_gzip(filename:str):
    """
    Delete the gzip file to save disk space 
    
    Args:
        - filename:str -> filename.csv
    Returns:
        No returns
    """
    os.remove(filename + ".gz")

def run(weather_url:str):
    """
    Construct url & filename, download the gzip file and decompress. Then delete the gzip
    
    Args:
        - url:str -> URL where we download the data
    Returns:
        No returns 
    """
    # Create a list with filename.csv 
    list_filenames:list = []
    for filename in os.listdir("data/csv"):
        list_filenames.append(filename)

    for year in range(1996, date.today().year + 1):
        for month in range(1, 13):
            url:str = construct_url(year, month, weather_url)
            filename:str = construct_filename(year, month)

            # If filename isn't in the list we download the file or the date of the file is in the current month we download, 
            # else we continue
            if filename[11:] not in list_filenames or (date.today().year == year and (date.today().month == month or date.today().month == month - 1)):
                download(url, filename)
                decompress(filename)
                delete_gzip(filename)