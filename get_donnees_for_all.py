import urllib.request
import gzip
import shutil
from datetime import date


# Specify the URL pattern
url_pattern = "https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/Archive/synop.{year}{month}.csv.gz"

# Loop over the years and months
for year in range(1996, date.today().year + 1):
    for month in range(1, 13):
        # Construct the URL for the current year and month
        url = url_pattern.format(year=year, month=str(month).zfill(2))

        # Construct the filename for the current year and month
        filename = "synop.{year}{month}.csv".format(
            year=year, month=str(month).zfill(2)
        )

        # Download the gzip file
        with urllib.request.urlopen(url) as response:
            with open(filename + ".gz", "wb") as outfile:
                outfile.write(response.read())

        # Decompress the gzip file
        with gzip.open(filename + ".gz", "rb") as f_in:
            with open(filename, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)

        # Optional: delete the gzip file to save disk space
        import os

        os.remove(filename + ".gz")
