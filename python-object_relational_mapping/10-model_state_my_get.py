#!/usr/bin/python3
"""
Prints the State id with the name passed as argument from the database.
If no state found, prints 'Not found'.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Check argument count
    if len(sys.argv) != 5:
        print("Usage: ./10-model_state_my_get.py "
              "<user> <password> <db> <state_name>")
        sys.exit(1)

    # Setup connection to MySQL
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Search for the state by name (SQL injection safe)
    state_name = sys.argv[4]
    state = session.query(State).filter(State.name == state_name).first()

    # Output results
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
