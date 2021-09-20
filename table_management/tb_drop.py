import sys
sys.path.insert(0, "../MySQL Python Connector")
from connecting import connecting_db1

db = connecting_db1()

cursor = db.cursor()

# Destroy Table
# DROP TABLE <nama tabel>

# Delete all content inside a table
# TRUNCATE TABLE <nama tabel>;

SQLCommand = "DROP TABLE IF EXISTS two;"
cursor.execute(SQLCommand)

print("Tabel berhasil dihapus!")