#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a' from the database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Connect to the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query states containing letter 'a'
    states = session.query(State).filter(
        State.name.like('%a%')
    ).order_by(State.id).all()

    # Print states in the required format
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
