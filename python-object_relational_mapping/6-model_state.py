#!/usr/bin/python3
"""
This script connects to a MySQL database using SQLAlchemy and
creates all tables defined by Base subclasses (here, the states table).
"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    # Validate arguments count
    if len(sys.argv) != 4:
        print("Usage: ./6-model_state.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    # Create the engine to connect to MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create all tables stored in Base's metadata
    Base.metadata.create_all(engine)
