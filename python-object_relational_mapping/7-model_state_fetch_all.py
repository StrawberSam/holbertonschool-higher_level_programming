#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.

Connects to a MySQL server running on localhost at port 3306.
Takes 3 arguments: mysql username, mysql password, and database name.
Results are sorted in ascending order by states.id.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get credentials from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Set up SQLAlchemy engine and session
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{db_name}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects ordered by id
    states = session.query(State).order_by(State.id).all()

    # Print results
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
