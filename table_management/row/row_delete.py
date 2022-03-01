import mysql.connector
import sys
sys.path.insert(0, "../MySQL Python Connector")
from connecting import connecting_db

db = connecting_db()

cursor = db.cursor()

# DELETE FROM <nama tabel> WHERE <id = %s>
SQLCommand = "DELETE FROM nama_table WHERE id=%s"
value = (6,)

cursor.execute(SQLCommand, value)
db.commit()

# print("{} data diubah".format(cursor.rowcount))
print("Changed.")