#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco"
and establishes the relationship between them.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create the engine and connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    # Create a session
    session = Session(engine)

    # Create the State "California"
    california = State(name="California")

    # Create the City "San Francisco" and associate it with the State
    san_francisco = City(name="San Francisco", state=california)

    # Add the State and City to the session
    session.add(california)
    session.add(san_francisco)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
