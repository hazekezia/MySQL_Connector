import mysql.connector
import sys
sys.path.insert(0, "../MySQL Python Connector")
from connecting import connecting_db

db = connecting_db()

cursor = db.cursor()

# UPDATE <nama tabel> SET <nama kolom=%s> WHERE <id = %s>
SQLCommand = "UPDATE nama_table2 SET name=%s, age=%s WHERE id=%s"
value = ("Alex", "20", 4)

cursor.execute(SQLCommand, value)
db.commit()

# print("{} data diubah".format(cursor.rowcount))
print("Changed.")