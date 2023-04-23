import pandas as pd
import matplotlib.pyplot as plt

def dix_annee_chaudes(df:pd.DataFrame):
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
    plt.savefig('data/graphs/dix_annees_les_plus_chaudes.png')

def evolution_temperature(df:pd.DataFrame):
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
    plt.savefig('data/graphs/evolution_temperature_dans_le_temps.png')

def nombre_jour_eolienne(df:pd.DataFrame):
    no_wind_days = 0
    for x in df.itertuples():
        if x.ff < 4.1:
            no_wind_days = no_wind_days + 1
        if x.ff >= 25:
            no_wind_days = no_wind_days + 1
    return no_wind_days