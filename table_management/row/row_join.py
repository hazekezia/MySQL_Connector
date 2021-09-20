import sys
sys.path.insert(0, "../MySQL Python Connector")
from connecting import connecting_db1

db = connecting_db1()
cursor = db.cursor()

SQLCommand = """SELECT *
    FROM one
    INNER JOIN two
    ON one.umur = two.umur;
"""
cursor.execute(SQLCommand)

hasil = cursor.fetchall()

for value in hasil:
  print(value)