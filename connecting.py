import mysql.connector

def connecting_db():
  db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="nama_database"
  )
  return db