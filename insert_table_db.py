import mysql.connector

# database = input("Nama database : ")

db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="",
  database= "uwu"
)

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