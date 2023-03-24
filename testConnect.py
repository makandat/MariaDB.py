#!/usr/bin/python3
import mariadb

conn = mariadb.connect(user='user', password='ust62kjy', host='localhost', database='user')
cur = conn.cursor()

cur.execute("select count(*) from Pictures;")

for row in cur.fetchall():
    print(row[0])

cur.close
conn.close
