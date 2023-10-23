#!/usr/bin/python3
"""prints the State object with the name
passed as argument from the database"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True)
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    state = session.query(State).filter(State.name == sys.argv[4]).first()
    if state is None:
        print("Not Found")
    else:
        print("{}".format(state.id))
    session.close()
