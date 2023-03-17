#!/usr/bin/python3
""" 0-select_states module """

if __name__ == "__main__":

    import MySQLdb
    import sys

    inp = sys.argv
    if len(inp) < 4:
        exit(1)
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=inp[1],
                           passwd=inp[2],
                           db=inp[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    """cur.execute('''SELECT *
                    FROM states
                    WHERE name LIKE 'N%'
                    ORDER BY id ASC''') """
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    conn.close()
