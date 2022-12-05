#!/usr/bin/python3
"""This is a model city fetch by state script"""

import sys
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(State, City).\
        filter(State.id == City.state_id).order_by(City.id)
    for state, city in rows:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
