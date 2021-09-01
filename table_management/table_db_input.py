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
# CREATE TABLE <nama tabel> (
#   id INT AUTO_INCREMENT PRIMARY KEY,
#   name VARCHAR(255),
# )

SQLCommand = """CREATE TABLE api_test (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  harga VARCHAR(255)
)
"""
cursor.execute(SQLCommand)

print("Tabel berhasil dibuat!")