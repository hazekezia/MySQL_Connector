import mysql.connector
import sys
sys.path.insert(0, "../MySQL Python Connector")
from connecting import connecting_db1

db = connecting_db1()

cursor = db.cursor()

# UPDATE <nama tabel> SET <nama kolom=%s> WHERE <id = %s>
SQLCommand = "UPDATE api_test SET name=%s, harga=%s WHERE id=%s"
value = ("Alex", "29000", 4)

cursor.execute(SQLCommand, value)
db.commit()

# print("{} data diubah".format(cursor.rowcount))
print("Changed.")