#!/usr/bin/python3

""" 11-model_state_insert module """

if __name__ == "__main__":

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    from relationship_state import Base, State
    from relationship_city import City

    inp = sys.argv
    if len(inp) < 4:
        exit(1)
    conn_str = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn_str.format(inp[1], inp[2], inp[3]))
    Session = sessionmaker(engine)

    Base.metadata.create_all(engine)

    session = Session()

    california = State('California')
    san_fran = City('San Francisco')
    california.cities = [san_fran]
    session.add(california)
    session.commit()

    session.close()
