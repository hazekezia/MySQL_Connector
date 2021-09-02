import mysql.connector
import sys
sys.path.insert(0, "../MySQL Python Connector")
from connecting import connecting_db1

db = connecting_db1()

cursor = db.cursor()

# Isi command SQL disini
# INSERT INTO <nama tabel> (<nama, kolum)>) VALUES (%s, %s, %s)
SQLCommand = "INSERT INTO karyawan (nama, email, umur, gaji) VALUES (%s, %s, %s, %s)"
Data = [
    ("Jonathan Sitohang", "uwu@gmail.com", "20", "1000000"),
    ("Jonathan Situmorang", "uwu4@gmail.com", "24", "2000000"),
    ("Jonathan Siahaan", "uwu3@gmail.com", "21", "3500000"),
    ("Jonathan Simajuntak", "uwu5@gmail.com", "19", "900000")
]

for value in Data:
    cursor.execute(SQLCommand, value)
    db.commit()

print("{} baris data telah ditambahkan".format(len(value)))