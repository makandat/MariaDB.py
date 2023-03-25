# MariaDB.py v1.1.0 2023-03-25
import mariadb
import json

# MariaDB class
class MariaDB:
  # コンストラクタ
  def __init__(self, user="", password="", database="", host="localhost"):
    if user == "":
      self._conf = MariaDB.getConf()
      self._conn = mariadb.connect(user=self._conf["user"], password=self._conf["password"], host=self._conf["host"], database=self._conf["database"])
    else:
      self._conf = {"user":user, "password":password, "host":host, "database":database}
      self._conn = mariadb.connect(user=user, password=password, host=host, database=database)
    self._cur = self._conn.cursor()
    return
  
  @staticmethod
  def getConf():
    conf = {}
    with open("MariaDB.json", "r") as f:
      conf = json.load(f)
    return conf


  # SELECT クエリー
  def query(self, sql):
    self._cur.execute(sql)
    return self._cur.fetchall()

  # 値を１つだけ返すクエリー
  def getValue(self, sql):
    self._cur.execute(sql)
    row = self._cur.fetchone()
    return row[0]

  # 行を１つだけ返すクエリー
  def getRow(self, sql):
    self._cur.execute(sql)
    row = self._cur.fetchone()
    return row

  # 非SELECTクエリー
  def execute(self, sql, data=None):
    self.conn.autocommit = True
    if data is None:
      self._cur.execute(sql)
    else:
      self._cur.execute(sql, data)
    return

  # 接続を閉じる
  def close(self):
    self._cur.close()
    self._conn.close()
    return
  
  # データベースの変更
  def use(self, database):
    self.close()
    self._conf["database"] = database
    self._conn = mariadb.connect(user=self._conf["user"], password=self._conf["password"], host=self._conf["host"], database=self._conf["database"])
    self._cur = self._conn.cursor()
    return

  # 接続情報
  @property
  def conf(self):
    return self._conf
  
  # カーソル
  @property
  def cursor(self):
    return self._cur
  
  # 接続オブジェクト
  @property
  def conn(self):
    return self._conn
