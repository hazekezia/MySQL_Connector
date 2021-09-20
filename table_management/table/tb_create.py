import mysql.connector
import sys
sys.path.insert(0, "../MySQL Python Connector")
from connecting import connecting_db1

db = connecting_db1()

cursor = db.cursor()

# Isi command SQL disini
# CREATE TABLE <nama tabel> (
#   id INT AUTO_INCREMENT PRIMARY KEY,
#   name VARCHAR(255),
# )

SQLCommand = """CREATE TABLE two (
  id_two INT AUTO_INCREMENT PRIMARY KEY,
  harga VARCHAR(255) NOT NULL,
  deksripsi TEXT NOT NULL
)
"""
cursor.execute(SQLCommand)

print("Tabel berhasil dibuat!")