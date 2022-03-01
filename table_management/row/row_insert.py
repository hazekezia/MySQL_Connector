import mysql.connector
import sys
sys.path.insert(0, "../MySQL Python Connector")
from connecting import connecting_db

db = connecting_db()

cursor = db.cursor()

# Isi command SQL disini
# INSERT INTO <nama tabel> (<nama, kolum)>) VALUES (%s, %s, %s)
SQLCommand = "INSERT INTO nama_table (name, id_ext, age) VALUES (%s, %s, %s)"
Data = [
    ('haze', '2', '18'),
    ('kezia', '4', '20'),
    ('kezia', '4', '20'),
]

for value in Data:
    cursor.execute(SQLCommand, value)
    db.commit()

print("{} baris data telah ditambahkan".format(len(value)))