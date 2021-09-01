import mysql.connector

def connecting_db():
  db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
  )
  return db

def connecting_db1():
  db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="hazekezia"
  )
  return db