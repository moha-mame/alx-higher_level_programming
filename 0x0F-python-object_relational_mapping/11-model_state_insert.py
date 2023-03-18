#!/usr/bin/python3

""" 11-model_state_insert module """

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

    louisiana = State('Louisiana')
    session.add(louisiana)
    session.commit()

    print(louisiana.id)

    session.close()
