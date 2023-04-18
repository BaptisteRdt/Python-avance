import json
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from typing import List

# Création de la base de données
engine = create_engine("sqlite:///weather_data.db", echo=True)
Base = declarative_base()

# Création de la session
Session = sessionmaker(bind=engine)
session = Session()

# Définition de la classe de données météorologiques
class WeatherData(Base):
    __tablename__ = "weather_data"

    numer_sta = Column(Integer, primary_key=True)
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

# Fonction pour insérer les données météorologiques dans la base de données
def insert_data(data: dict):
    for row in data["data"]:
        # Conversion de la date au format ISO 8601
        date_str = row["date"]
        date = datetime.fromisoformat(date_str)
        row["date"] = date.strftime("%Y%m%d%H%M%S")

        # Insertion des données dans la base de données
        weather_data = WeatherData(**row)
        session.add(weather_data)
    session.commit()


# Lecture des données depuis un fichier JSON
with open("test.json") as f:
    data = json.load(f)

# Insertion des données dans la base de données
insert_data(data)
