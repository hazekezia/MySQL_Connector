import mysql.connector
import sys
sys.path.insert(0, "../MySQL Python Connector")
from connecting import connecting_db1

db = connecting_db1()

cursor = db.cursor()

# Isi command SQL disini
# INSERT INTO <nama tabel> (<nama, kolum)>) VALUES (%s, %s, %s)
SQLCommand = "INSERT INTO customers (name, harga) VALUES (%s, %s)"
Data = [
    ("Nama", "Kelas"),
    ("Namas", "Kelass")
]

for value in Data:
    cursor.execute(SQLCommand, value)
    db.commit()

print("{} baris data telah ditambahkan".format(len(value)))