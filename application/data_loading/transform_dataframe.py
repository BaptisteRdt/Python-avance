import pandas as pd
from typing import Set, Any

def openCSVandConcat(df:pd.DataFrame):
    directory_path = "data/csv/"
    synop = "synop."
    csv = ".csv"
    meteo_df_list = []
    for year in range(1996, 1997):
        for month in range(1, 4):
            month = f'{month:02d}'
            filename = ''.join(map(str, (directory_path, synop, year, month, csv)))
            meteo = pd.read_csv(filename, sep='\;')
            meteo_df_list.append(meteo)
    df = pd.concat(meteo_df_list)
    return df

def remove_others(df:pd.DataFrame, columns: Set[Any]):
    cols_total: Set[Any] = set(df.columns)
    diff: Set[Any] = cols_total - columns
    df.drop(diff, axis=1, inplace=True)

def treatment_csv(df:pd.DataFrame):
    df.rename(columns={'t': 'temperature'}, inplace=True)
    remove_others(df, {'numer_sta', 'date', 'temperature', 'ff'})
    df['year'] = df['date'].astype(str).str[:4]
    df['month'] = df['date'].astype(str).str.slice(4, 6)
    df['day'] = df['date'].astype(str).str.slice(6, 8)
    df['date2'] = pd.to_datetime(df[['year', 'month', 'day']])
    return df

def convertIntOrFloat(df:pd.DataFrame):
    df['temperature'] = df['temperature'].astype(str).str[:6]
    df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')
    df['ff'] = df['ff'].astype(str).str[:6]
    df['ff'] = pd.to_numeric(df['ff'], errors='coerce')
    df['year'] = df['year'].astype(str).str[:6]
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    df['year'].astype(int)
    df['month'] = df['month'].astype(str).str[:6]
    df['month'] = pd.to_numeric(df['month'], errors='coerce')
    df['month'].astype(int)
    df['day'] = df['day'].astype(str).str[:6]
    df['day'] = pd.to_numeric(df['day'], errors='coerce')
    df['day'].astype(int)
    return df