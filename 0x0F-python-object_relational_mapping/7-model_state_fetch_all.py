#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Creating all the Base metadata tables
    Base.metadata.create_all(engine)

    # Creating new Session instance for engine we created
    Session = sessionmaker(bind=engine)
    session = Session()

    # Quering all State objects from the database and order by states.id
    states = session.query(State).order_by(State.id).all()

    # Printing the State objects in it specific format
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
