from fastapi import FastAPI
import uvicorn
from website.router import configuration_route
import data_loading.get_data as dl_data
import data_loading.transform_csv_to_json as to_json

# Applying configuration to the FastAPI app
app = FastAPI()
app = configuration_route(app)

# Get weather data
weather_url:str = "https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/Archive/synop.{year}{month}.csv.gz"
dl_data.run(weather_url)

# to_json.run()

if __name__ == '__main__':
    uvicorn.run(app)