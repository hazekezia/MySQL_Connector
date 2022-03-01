import sys
sys.path.insert(0, "../MySQL Python Connector")
from connecting import connecting_db

db = connecting_db()
cursor = db.cursor()

SQLCommand = """SELECT *
    FROM nama_table
    INNER JOIN nama_table2
    ON nama_table.id = nama_table2.id;
"""
cursor.execute(SQLCommand)

hasil = cursor.fetchall()

for value in hasil:
  print(value)