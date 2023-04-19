import json
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from typing import List
from datetime import datetime

# Création de la base de données
engine = create_engine("sqlite:///weather_data.db", echo=True)
Base = declarative_base()

# Création de la session
Session = sessionmaker(bind=engine)
session = Session()

# Définition de la classe de données météorologiques
class WeatherData(Base):
    __tablename__ = "weather_data"

    # id = Column(Integer, primary_key=True)
    numer_sta = Column(String, primary_key=True)
    date = Column(datetime)
    pmer = Column(Float)
    tend = Column(Float)
    cod_tend = Column(Integer)
    dd = Column(Integer)
    ff = Column(Float)
    t = Column(Float)
    td = Column(Float)
    u = Column(Integer)
    vv = Column(Float)
    ww = Column(String)
    w1 = Column(Integer)
    w2 = Column(Integer)
    n = Column(Integer)
    nbas = Column(Integer)
    hbas = Column(Float)
    cl = Column(Integer)
    cm = Column(Integer)
    ch = Column(Integer)
    pres = Column(Integer)
    niv_bar = Column(Integer)
    geop = Column(Float)
    tend24 = Column(Float)
    tn12 = Column(Float)
    tn24 = Column(Float)
    tx12 = Column(Float)
    tx24 = Column(Float)
    tminsol = Column(Float)
    sw = Column(Float)
    tw = Column(Float)
    raf10 = Column(Integer)
    rafper = Column(Integer)
    per = Column(Integer)
    etat_sol = Column(String)
    ht_neige = Column(Float)
    ssfrai = Column(Float)
    perssfrai = Column(Float)
    rr1 = Column(Float)
    rr3 = Column(Float)
    rr6 = Column(Float)
    rr12 = Column(Float)
    rr24 = Column(Float)
    phenspe1 = Column(Integer)
    phenspe2 = Column(Integer)
    phenspe3 = Column(Integer)
    phenspe4 = Column(Integer)
    nnuage1 = Column(Integer)
    ctype1 = Column(Integer)
    hnuage1 = Column(Float)
    nnuage2 = Column(Integer)
    ctype2 = Column(Integer)
    hnuage2 = Column(Float)
    nnuage3 = Column(Integer)
    ctype3 = Column(Integer)
    hnuage3 = Column(Float)
    nnuage4 = Column(Integer)
    ctype4 = Column(Integer)
    hnuage4 = Column(Float)

    def __repr__(self):
        return f"WeatherData(date='{self.date}', pmer={self.pmer}, tend={self.tend}, cod_tend={self.cod_tend}, dd={self.dd}, ff={self.ff}, t={self.t}, td={self.td}, u={self.u}, pres={self.pres})"


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


def insert_data_from_file(file_path: str):
    with open(file_path, "r") as f:
        data = json.load(f)

    for row in data["data"]:
        # Conversion de la date au format ISO 8601
        date_str = row["date"]
        date = datetime.fromisoformat(date_str)
        row["date"] = date.strftime("%Y%m%d%H%M%S")

        # Insertion des données dans la base de données
        weather_data = WeatherData(**row)
        session.add(weather_data)
    session.commit()


# Utilisation de la fonction
insert_data_from_file("data_json.json")


# Lecture des données depuis un fichier JSON
# with open("data_json.json") as f:
# data = json.load(f)

# Insertion des données dans la base de données
# insert_data(data)
