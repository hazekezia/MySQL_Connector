import mysql.connector
import sys
sys.path.insert(0, "../MySQL Python Connector")
from connecting import connecting_db

db = connecting_db()

cursor = db.cursor()

#Select * FROM <nama table>
SQLCommand = "SELECT * FROM nama_table"
cursor.execute(SQLCommand)

# fetchall() -> ambil semua data
# fetchmany(int) -> ambil beberapa data int mis: 10
# fetchone() -> ambil satu data pertama

hasil = cursor.fetchall()

for value in hasil:
  print(value)