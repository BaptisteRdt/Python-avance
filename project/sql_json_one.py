import json
from sqlalchemy import create_engine, Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class WeatherData(Base):
    __tablename__ = "weather_data_test_wdata"

    numer_sta = Column(String(14), primary_key=True)
    date = Column(String(14))
    pmer = Column(String(6))
    tend = Column(String(14))
    cod_tend = Column(String(14))
    dd = Column(String(14))
    ff = Column(String(14))
    t = Column(String(14))
    td = Column(String(14))
    u = Column(String(14))
    vv = Column(String(14))
    ch = Column(String(14))
    pres = Column(String(14))


def convert_json_to_db(json_file_path: str, db_file_path: str):
    # Ouverture du fichier JSON
    with open(json_file_path, "r") as f:
        data = json.load(f)

    # Création de la base de données
    engine = create_engine(f"sqlite:///{db_file_path}")
    Base.metadata.create_all(engine)

    # Ajout des données à la base de données
    Session = sessionmaker(bind=engine)
    session = Session()
    for row in data:
        weather_data = WeatherData(**row)
        session.add(weather_data)
    session.commit()


# Exemple d'utilisation
convert_json_to_db("test.json", "data.db")
