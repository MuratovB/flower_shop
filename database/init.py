import sqlite3 as sql
from query import query

queries = query.split(';')

conn = sql.connect('MuratovBektur.db')
curs = conn.cursor()

for query in queries:
    query = query.strip()
    if query:
        curs.execute(query+';')

conn.commit()
conn.close()