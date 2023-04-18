from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import csv

# Créer un moteur SQLAlchemy pour la base de données SQLite
engine = create_engine("sqlite:///weather_data.db", echo=True)

# Créer une classe de base SQLAlchemy pour définir les modèles de données
Base = declarative_base()

# Définir un modèle de données pour les données météorologiques
class WeatherData(Base):
    __tablename__ = "weather_data"

    numer_sta = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(String(14))
    pmer = Column(String(6))
    tend = Column(Integer)
    cod_tend = Column(Integer)
    dd = Column(Integer)
    ff = Column(Float)
    t = Column(Float)
    td = Column(Float)
    u = Column(Integer)
    pres = Column(Integer)

    def __repr__(self):
        return f"WeatherData(date='{self.date}', pmer='{self.pmer}', tend='{self.tend}', cod_tend={self.cod_tend}, dd={self.dd}, ff={self.ff},t={self.t},td={self.td},u={self.u},pres={self.pres})"


# Créer les tables dans la base de données s'ils n'existent pas déjà
Base.metadata.create_all(bind=engine)

# Fonction pour insérer les données dans la base de données
def insert_data(session, filename):
    with open(filename, newline="", encoding="iso-8859-1") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        next(reader)  # skip header
        for row in reader:
            numer_sta, date, pmer, tend, cod_tend, dd, ff, t, td, u, pres = row
            weather_data = WeatherData(
                numer_sta=numer_sta,
                date=date,
                pmer=pmer,
                tend=tend,
                cod_tend=cod_tend,
                dd=dd,
                ff=ff,
                t=t,
                td=td,
                u=u,
                pres=pres,
            )
            session.add(weather_data)


# Insertion de toutes les données dans la base de données
Session = sessionmaker(bind=engine)
session = Session()
for year in range(1996, 2021):
    for month in range(1, 13):
        filename = f"synop.{year}{month:02}.csv"
        insert_data(session, filename)
        session.commit()
    print(f"Inserted data for year {year}")

# Fermeture de la session
session.close()
