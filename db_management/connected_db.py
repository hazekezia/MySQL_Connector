from connecting import connecting_db
import mysql.connector

db = connecting_db()

if db.is_connected():
  print("Connected to mySQL!")