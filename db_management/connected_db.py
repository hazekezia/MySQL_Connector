import mysql.connector
import sys
sys.path.insert(0, "../MySQL Python Connector")
from connecting import connecting_db

db = connecting_db()

if db.is_connected():
  print("Connected to mySQL!")