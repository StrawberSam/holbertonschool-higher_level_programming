#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_14_usa,
displayed as <state name>: (<city id>) <city name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Connexion à la base de données
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{db_name}",
        pool_pre_ping=True
    )

    # Création de session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête pour obtenir toutes les villes triées par city.id
    results = (
        session.query(City, State)
        .join(State, City.state_id == State.id)
        .order_by(City.id)
        .all()
    )

    # Affichage des résultats
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
