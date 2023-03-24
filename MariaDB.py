# MariaDB.py v1.0 2023-03-21
import mariadb, json

# MariaDB class
class MariaDB:
  def __init__(self, user="", password="", database="", host="localhost"):
    if user == "":
      with open("MariaDB.json", "r") as f:
        conf = json.load(f)
        self._conn = mariadb.connect(user=conf["user"], password=conf["password"], host=conf["host"], database=conf["database"])
    else:
      self._conn = mariadb.connect(user=user, password=password, host=host, database=database)
    self._cur = self._conn.cursor()
    return

  def query(self, sql):
    self._cur.execute(sql)
    return self._cur.fetchall()

  def getValue(self, sql):
    self._cur.execute(sql)
    row = self._cur.fetchone()
    return row[0]

  def getRow(self, sql):
    self._cur.execute(sql)
    row = self._cur.fetchone()
    return row

  def execute(self, sql, data=None):
    if data is None:
      self._cur.execute(sql)
    else:
      self._cur.execute(sql, data)
