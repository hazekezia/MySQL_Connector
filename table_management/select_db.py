import mysql.connector

# database = input("Nama database : ")

db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="",
  database= "uwu"
)

cursor = db.cursor()

#Select * FROM <nama table>
SQLCommand = "SELECT * FROM uwu"
cursor.execute(SQLCommand)

# fetchall() -> ambil semua data
# fetchmany(int) -> ambil beberapa data int mis: 10
# fetchone() -> ambil satu data pertama

hasil = cursor.fetchall()

for value in hasil:
  print(value)