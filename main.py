
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from typing import Set, Any


def openCSVandConcat():
    synop = "synop."
    csv = ".csv"
    meteo_df_list = []
    for a in range(1996, 1997):
        for m in range(1, 4):
            m = f'{m:02d}'
            nomfichierlist = (synop, a, m, csv)
            nomfichier = ''.join(map(str, nomfichierlist))
            meteo = pd.read_csv(nomfichier, sep='\;')
            meteo_df_list.append(meteo)
    df_final = pd.concat(meteo_df_list)


def remove_others(df, columns: Set[Any]):
    cols_total: Set[Any] = set(df.columns)
    diff: Set[Any] = cols_total - columns
    df.drop(diff, axis=1, inplace=True)


def traitement_csv(df):
    df.rename(columns={'t': 'temperature', 'tn12': 'Température min 12 heure', 'tn24': 'Température min 24 heure',
                       'tx12': 'Température max 12 heure', 'tx24': 'Température max 24 heure'}, inplace=True)
    remove_others(df, {'numer_sta', 'date', 'temperature', 'dd', 'Température min 12 heure', 'Température min 24 heure',
                       'Température max 12 heure', 'Température max 24 heure'})
    df['annee'] = df['date'].astype(str).str[:4]
    df['mois'] = df['date'].astype(str).str.slice(4, 6) + df['date'].astype(str).str.slice(2, 4)
    df['jour'] = df['date'].astype(str).str.slice(6, 8) + df['date'].astype(str).str.slice(4, 6) + df['date'].astype(
        str).str.slice(2, 4)
    return df


def convertIntOrFloat(df):
    df['temperature'] = df['temperature'].astype(str).str[:6]
    df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')
    df['Température min 12 heure'] = df['Température min 12 heure'].astype(str).str[:6]
    df['Température min 12 heure'] = pd.to_numeric(df['Température min 12 heure'], errors='coerce')
    df['Température min 24 heure'] = df['Température min 24 heure'].astype(str).str[:6]
    df['Température min 24 heure'] = pd.to_numeric(df['Température min 24 heure'], errors='coerce')
    df['Température max 12 heure'] = df['Température max 12 heure'].astype(str).str[:6]
    df['Température max 12 heure'] = pd.to_numeric(df['Température max 12 heure'], errors='coerce')
    df['Température max 24 heure'] = df['Température max 24 heure'].astype(str).str[:6]
    df['Température max 24 heure'] = pd.to_numeric(df['Température max 24 heure'], errors='coerce')
    df['dd'] = df['dd'].astype(str).str[:6]
    df['dd'] = pd.to_numeric(df['dd'], errors='coerce')
    df['annee'] = df['annee'].astype(str).str[:6]
    df['annee'] = pd.to_numeric(df['annee'], errors='coerce')
    df['annee'].astype(int)
    df['mois'] = df['mois'].astype(str).str[:6]
    df['mois'] = pd.to_numeric(df['mois'], errors='coerce')
    df['mois'].astype(int)
    df['jour'] = df['jour'].astype(str).str[:6]
    df['jour'] = pd.to_numeric(df['jour'], errors='coerce')
    df['jour'].astype(int)


def temperatureMoisGraph(df):
    dfTannee = df.groupby('annee').agg({'temperature': 'mean'})
    dfTannee.sort_values(by='temperature')
    dfTannee.reset_index(inplace=True)
    plt.figure(figsize=(5, 5))
    plt.barh(dfTannee["annee"], dfTannee["temperature"], color='red')
    plt.title("Les 10 années les plus chaudes en températures")
    plt.xlabel("Temperature (en Kalvin)")
    plt.ylabel("Année")

    dfTmois = df.groupby('mois').agg({'temperature': 'mean'})
    dfTmois.reset_index(inplace=True)
    figure = plt.figure(figsize=(10, 5))
    ax = sns.lineplot(x="mois", y="temperature", data=dfTmois)
    ax.set_ylim(260, 300)
    plt.title("Evolution de la temperature au fil des années (de 1996 à 2022)")
    plt.show()