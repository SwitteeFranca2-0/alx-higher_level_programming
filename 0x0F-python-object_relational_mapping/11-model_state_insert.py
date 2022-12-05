#!/usr/bin/python3
"""Model state inserts"""


import sys
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name="Louisiana")
    session.add(state)
    session.commit()

    row = session.query(State)
    for r in row:
        print("{}: {}".format(r.id, r.name))
