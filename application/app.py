from fastapi import FastAPI
import uvicorn
from website.router import configuration_route
from get_data import run

# Applying configuration to the FastAPI app
app = FastAPI()
app = configuration_route(app)

# Get weather data
weather_url = "https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/Archive/synop.{year}{month}.csv.gz"
run(weather_url)



if __name__ == '__main__':
    uvicorn.run(app)