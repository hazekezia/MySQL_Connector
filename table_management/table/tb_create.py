import mysql.connector
import sys
sys.path.insert(0, "../MySQL Python Connector")
from connecting import connecting_db

db = connecting_db()

cursor = db.cursor()

# Isi command SQL disini
# CREATE TABLE <nama tabel> (
#   id INT AUTO_INCREMENT PRIMARY KEY,
#   name VARCHAR(255) NOT NULL,
# )

SQLCommand = """CREATE TABLE nama_table (
  id INT(11) AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL
)
"""
cursor.execute(SQLCommand)

print("Tabel berhasil dibuat!")