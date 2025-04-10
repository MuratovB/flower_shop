import sqlite3 as sql

def db(query="", params=()):
    conn = sql.connect('MuratovBektur.db')
    curs = conn.cursor()
    result = curs.execute(query, params).fetchall()
    return result