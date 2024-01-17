"""
Script that lists all state objects containing the letter a from the database
Also takes 3 arguments...
"""
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping = True))

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id)

    for state in states:
        if "a" in state.name:
            print("{}: {}".format(state.id, state.name))
              
