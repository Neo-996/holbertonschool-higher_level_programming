#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./14-model_city_fetch_by_state.py "
              "<username> <password> <database>")
        sys.exit(1)

    # Connect to MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities, join with states to get state name,
    # order by city id ascending
    cities = session.query(City, State).join(
        State,
        City.state_id == State.id
    ).order_by(City.id).all()

    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
