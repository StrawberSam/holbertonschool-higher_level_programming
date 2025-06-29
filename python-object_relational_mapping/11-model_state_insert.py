#!/usr/bin/python3
"""
Adds the State object 'Louisiana' to the database hbtn_0e_6_usa.
Prints the new state's id after creation.
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

    # Création du nouvel état
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Affichage de son ID
    print(new_state.id)

    session.close()
