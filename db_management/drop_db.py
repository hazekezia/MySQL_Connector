import mysql.connector

db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd=""
)

cursor = db.cursor()
database_input = input("Masukkan nama database : ")
cursor.execute("DROP DATABASE %s" %database_input)
print("Database %s selesai dihapus!" %database_input)