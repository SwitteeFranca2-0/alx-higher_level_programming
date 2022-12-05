#!/usr/bin/python3
"""his ia a stete get """

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
    stateName = sys.argv[4]
    rows = session.query(State.id, State.name).filter_by(name=stateName)
    if len([r[0] for r in rows]) == 0:
        print("Not Found")
    else:
        [print(r[0]) for r in rows]
