#!/usr/bin/python3
"""lists all State objects that contain the letter a from the database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=eng)
    session = Session()
    for state in session.query(State).order_by(State.id):
        if "a" in state.name:
            print("{}: {}".format(state.id, state.name))
    session.close()
