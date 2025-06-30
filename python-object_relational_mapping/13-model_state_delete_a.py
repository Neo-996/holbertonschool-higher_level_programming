#!/usr/bin/python3
"""
Deletes all State objects with a name 
containing the letter 'a' from the database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Check for correct arguments count
    if len(sys.argv) != 4:
        print("Usage: ./13-model_state_delete_a.py "
              "<username> <password> <database>")
        sys.exit(1)

    # Connect to the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for states containing 'a' in their name
    states_to_delete = session.query(State).filter(
        State.name.like('%a%')).all()

    # Delete all the states found
    for state in states_to_delete:
        session.delete(state)

    session.commit()
    session.close()
