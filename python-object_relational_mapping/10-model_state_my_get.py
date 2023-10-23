#!/usr/bin/python3
"""prints the State object with the name
passed as argument from the database"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=eng)
    session = Session()
    identify = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            identify = True
            break
    if identify is False:
        print("Not Found")
    session.close() 
