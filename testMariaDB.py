# Test MariaDB class
import MariaDB as maria

db = maria.MariaDB("user", "ust62kjy", "user")

# query()
rows = db.query("SELECT id, title FROM Pictures WHERE id > 23000")
for row in rows:
  print(str(row[0]) + ", " + row[1])
# getValue()
n = db.getValue("SELECT MIN(id) FROM Pictures")
print("minn = " + str(n))
# getRow()
row = db.getRow(f"SELECT id, title FROM Pictures WHERE id={n}")
print(str(row[0]) + ", " + row[1])
# execute()
db.execute("INSERT INTO colors VALUE('001122', 'test')")
db.execute("INSERT INTO colors VALUE(?, ?)", ["221100", "test2"])
rows = db.query("SELECT * FROM colors")
for row in rows:
  print(str(row[0]) + ", " + row[1])
