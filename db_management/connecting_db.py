import mysql.connector

db = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd=""
)

if db.is_connected():
  print("Connected to mySQL!")