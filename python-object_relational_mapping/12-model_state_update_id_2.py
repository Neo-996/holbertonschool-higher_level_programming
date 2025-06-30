#!/usr/bin/python3
"""
Changes the name of the State with id=2 to 'New Mexico' in the database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./12-model_state_update_id_2.py "
              "<username> <password> <database>")
        sys.exit(1)

    # Create the engine and bind a session
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State with id=2
    state = session.query(State).filter(State.id == 2).one_or_none()

    # If found, update the name
    if state:
        state.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
