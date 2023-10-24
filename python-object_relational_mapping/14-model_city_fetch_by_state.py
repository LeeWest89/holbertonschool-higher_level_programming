#!/usr/bin/python3
"""deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City


if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True)
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    c = session.query(City, State).join(State).all()
    for city, state in c:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.commit()
    session.close()
