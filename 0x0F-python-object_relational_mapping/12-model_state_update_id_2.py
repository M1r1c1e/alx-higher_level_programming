#!/usr/bin/python3
""" a script that is changing the name of a State object
    from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Creating all the Base metadata table
    Base.metadata.create_all(engine)

    # Creating a new Session instance for the engine created
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying State object from the database and updating value
    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()

    session.close()
