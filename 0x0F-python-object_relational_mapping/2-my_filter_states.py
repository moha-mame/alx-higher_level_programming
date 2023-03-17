#!/usr/bin/python3
""" 0-select_states module """

if __name__ == "__main__":

    import MySQLdb
    import sys

    inp = sys.argv
    if len(inp) < 5:
        exit(1)
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=inp[1],
                           passwd=inp[2],
                           db=inp[3],
                           charset="utf8")
    cur = conn.cursor()
    query_str = """SELECT *
                   FROM states
                   WHERE name LIKE BINARY '{}'
                   """.format(inp[4])
    cur.execute(query_str)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
