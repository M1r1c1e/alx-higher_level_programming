#!/usr/bin/python3
""" printing the State object with the name passed as argument
    from the database hbtn_0e_6_usa. Results must display the states.id
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create all the Base metadata tables
    Base.metadata.create_all(engine)

    # Creating a new Session instance for engine created
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying the State object from the database
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
