#!/usr/bin/python3
"""
Changes the name of the State object with id = 2
to 'New Mexico' in the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Récupération des arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Création de l'engine SQLAlchemy
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{db_name}",
        pool_pre_ping=True
    )

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Recherche de l'état avec id=2
    state = session.query(State).get(2)

    if state:
        state.name = "New Mexico"
        session.commit()

    session.close()
