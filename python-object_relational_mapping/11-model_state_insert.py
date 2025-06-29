#!/usr/bin/python3
"""
Adds the State "Louisiana" to the database and prints its id.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Check argument count
    if len(sys.argv) != 4:
        print("Usage: ./11-model_state_insert.py <user> <password> <database>")
        sys.exit(1)

    # Create engine and session
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create new state object
    new_state = State(name="Louisiana")

    # Add new state to session and commit to DB
    session.add(new_state)
    session.commit()

    # Print the new state's id
    print(new_state.id)

    # Close session
    session.close()
