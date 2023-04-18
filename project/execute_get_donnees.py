from datetime import date
from get_donnees import (
    construct_filename,
    construct_url,
    download,
    decompress,
    delete_gzip,
)

url_pattern = "https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/Archive/synop.{year}{month}.csv.gz"


def execute_data(url_pattern):
    """Construct url & filename, download the gzip file and decompress. Then delete the gzip"""
    for year in range(1996, date.today().year + 1):
        for month in range(1, 13):
            url = construct_url(year, month, url_pattern)
            filename = construct_filename(year, month)
            download(url, year, month, filename)
            decompress(filename)
            delete_gzip(filename)


execute_data(url_pattern)
