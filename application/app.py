from fastapi import FastAPI
import uvicorn
from website.router import configuration_route
import get_data
import transform_csv_to_json

# Applying configuration to the FastAPI app
app = FastAPI()
app = configuration_route(app)

# Get weather data
weather_url = "https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/Archive/synop.{year}{month}.csv.gz"
get_data.run(weather_url)

# transform_csv_to_json.run()

if __name__ == '__main__':
    uvicorn.run(app)