import mysql.connector

db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd=""
)

cursor = db.cursor()
database_input = input("Masukkan nama database : ")
cursor.execute("CREATE DATABASE %s" %database_input)
print("Database %s selesai dibuat!" %database_input)