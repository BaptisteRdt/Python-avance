from fastapi import FastAPI
import uvicorn
from website.router import configuration_route
import data_loading.get_data as dl_data
import data_loading.transform_csv_to_json as to_json
import data_loading.transform_dataframe as transform_df
import data_loading.graphs as graphs
import pandas as pd

# Get weather data
weather_url:str = "https://donneespubliques.meteofrance.fr/donnees_libres/Txt/Synop/Archive/synop.{year}{month}.csv.gz"
dl_data.run(weather_url)

# Transform csv files to json files
to_json.run()

# Transforme dataframe
df = pd.DataFrame()
df = transform_df.openCSVandConcat(df)
df = transform_df.treatment_csv(df)
df = transform_df.convertIntOrFloat(df)

# Load graphs
graphs.dix_annee_chaudes(df)
graphs.evolution_temperature(df)
no_wind_day_number = graphs.nombre_jour_eolienne(df)

# Applying configuration to the FastAPI app
app = FastAPI()
app = configuration_route(app, no_wind_day_number)

# Run website
if __name__ == '__main__':
    uvicorn.run(app)