import pandas as pd
import matplotlib.pyplot as plt

def dixanneechaudes(df:pd.DataFrame):
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
    plt.savefig('dix_annees_les_plus_chaudes.png')

def evolutiontemperature(df:pd.DataFrame):
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
    plt.savefig('evolution_temperature_dans_le_temps.png')

def nombrejoureolienne(df:pd.DataFrame):
    j = 0
    for x in df.itertuples():
        if ((x.ff) < 4.1):
            j = j + 1
        if ((x.ff) >= 25):
            j = j + 1
    message = "Le nombre de jour depuis 1996 où les éoliennes n'ont pas pu tourner est de : "
    print(message + str(j))