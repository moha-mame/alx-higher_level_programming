#!/usr/bin/python3

""" 9-model_state_filter_a module """

if __name__ == "__main__":

    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    import sys
    from model_state import Base, State

    inp = sys.argv
    if len(inp) < 4:
        exit(1)

    conn_str = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn_str.format(inp[1], inp[2], inp[3]))
    Session = sessionmaker(engine)

    Base.metadata.create_all(engine)
    session = Session()

    states = session.query(State) \
                    .filter(State.name.like('%a%')) \
                    .order_by(State.id)
    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
