#!/usr/bin/python3
"""printing the first State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Creating all the  Base metadata tables
    Base.metadata.create_all(engine)

    # Creating a new Session instance for the engine  created
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying the first State object from the database
    first_state = session.query(State).first()

    # Printing the State objects in the right format
    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))

    session.close()
