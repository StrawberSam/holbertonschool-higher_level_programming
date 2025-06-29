#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.

Connects to a MySQL server running on localhost at port 3306.
Takes 3 arguments: mysql username, mysql password, and database name.
Displays 'Nothing' if the table is empty.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line args
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create the SQLAlchemy engine
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{db_name}",
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch the first State object (ordered by id)
    first_state = session.query(State).order_by(State.id).first()

    # Display the result
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    session.close()
