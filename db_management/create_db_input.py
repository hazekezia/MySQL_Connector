from connecting import connecting_db
import mysql.connector

db = connecting_db()

cursor = db.cursor()
database_input = input("Masukkan nama database : ")
cursor.execute("CREATE DATABASE %s" %database_input)
print("Database %s selesai dibuat!" %database_input)