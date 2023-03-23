#!/usr/bin/python3

""" 101-relationship_states_cities_list module """

if __name__ == "__main__":

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    from relationship_city import City
    from relationship_state import Base, State

    inp = sys.argv
    if len(inp) < 4:
        exit(1)

    conn_str = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(conn_str.format(inp[1], inp[2], inp[3]))
    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()
    my_query = session.query(City.id, City.name, State.name) \
                      .join(State.cities) \
                      .order_by(City.id) \
                      .all()
    for row in my_query:
        print("{}: {} -> {}".format(row[0], row[1], row[2]))
    session.close()
