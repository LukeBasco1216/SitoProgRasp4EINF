
import pymssql

# Crea una connessione al database SQL Server
conn = pymssql.connect(server='192.168.40.16', database='cilibeanu.nicolae', user='cilibeanu.nicolae', password='xxx123##')

def execute_query(query, values=None):
    cursor = conn.cursor()
    if values:
        cursor.execute(query, values)
    else:
        cursor.execute(query)
    conn.commit()
