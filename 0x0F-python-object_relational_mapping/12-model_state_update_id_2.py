#!/usr/bin/python3

""" 12-model_state_update_id_2.py """


if __name__ == "__main__":

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    inp = sys.argv
    if len(inp) < 4:
        exit(1)

    conn_str = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn_str.format(inp[1], inp[2], inp[3]))
    Session = sessionmaker(engine)

    Base.metadata.create_all(engine)

    session = Session()

    my_query = session.query(State).filter(State.id == 2).all()
    if len(my_query) != 0:
        my_query[0].name = 'New Mexico'

    session.commit()

    session.close()
