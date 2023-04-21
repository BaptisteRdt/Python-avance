
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Set, Any


def openCSVandConcat(df):
    synop = "synop."
    csv = ".csv"
    meteo_df_list = []
    for year in range(1996, 1997):
        for month in range(1, 4):
            month = f'{month:02d}'
            filename = ''.join(map(str, (synop, year, month, csv)))
            meteo = pd.read_csv(filename, sep='\;')
            meteo_df_list.append(meteo)
    df = pd.concat(meteo_df_list)
    return df


def remove_others(df, columns: Set[Any]):
    cols_total: Set[Any] = set(df.columns)
    diff: Set[Any] = cols_total - columns
    df.drop(diff, axis=1, inplace=True)


def treatment_csv(df):
    df.rename(columns={'t': 'temperature'}, inplace=True)
    remove_others(df, {'numer_sta', 'date', 'temperature', 'ff'})
    df['year'] = df['date'].astype(str).str[:4]
    df['month'] = df['date'].astype(str).str.slice(4, 6)
    df['day'] = df['date'].astype(str).str.slice(6, 8)
    df['date2'] = pd.to_datetime(df[['year', 'month', 'day']])
    return df


def convertIntOrFloat(df):
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


def dixanneechaudes(df):
    dfAnnee = df.groupby('year').agg({'temperature': 'mean'})
    dfAnnee.sort_values(by='temperature').head(10)
    dfAnnee.reset_index(inplace=True)
    plt.xticks(rotation='45')
    plt.title("Les 10 années les plus chaudes en températures")
    plt.xlabel('Année')
    plt.ylabel('Temperature (en Kalvin)')
    plt.bar(dfAnnee["year"],
            dfAnnee["temperature"],
            color='blue')


def evolutiontemperature(df):
    dfAnnee = df.groupby('year').agg({'temperature': 'mean'})
    dfAnnee.sort_values(by='temperature').head(10)
    dfAnnee.reset_index(inplace=True)
    x = dfAnnee["year"]
    y = dfAnnee["temperature"]
    plt.rcParams['figure.figsize'] = (30, 30)
    plt.rcParams['font.size'] = '20'
    plt.title('Evolution de la temperature dans le temps')
    plt.xlabel('Années')
    plt.xticks(rotation='90')
    plt.ylabel('Température')
    plt.plot(x, y, linewidth=4)


def nombrejoureolienne(df):
    j = 0
    for x in df.itertuples():
        if ((x.ff) < 4.1):
            j = j + 1
        if ((x.ff) >= 25):
            j = j + 1
    message = "Le nombre de jour depuis 1996 où les éoliennes n'ont pas pu tourner est de : "
    print(message + str(j))
