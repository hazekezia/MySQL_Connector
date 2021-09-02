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

SQLCommand = """CREATE TABLE karyawan (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nama VARCHAR(255) NOT NULL,
  email VARCHAR(30) NOT NULL,
  umur VARCHAR(2) NOT NULL,
  gaji VARCHAR(10) NOT NULL
)
"""
cursor.execute(SQLCommand)

print("Tabel berhasil dibuat!")