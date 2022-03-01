import sys
sys.path.insert(0, "../MySQL Python Connector")
from connecting import connecting_db

db = connecting_db()

cursor = db.cursor()

# Destroy Table
# DROP TABLE <nama tabel>

# Delete all content inside a table
# TRUNCATE TABLE <nama tabel>;

SQLCommand = "DROP TABLE IF EXISTS nama_table"
cursor.execute(SQLCommand)

print("Tabel berhasil dihapus!")