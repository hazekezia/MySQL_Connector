import mysql.connector
import sys
sys.path.insert(0, "../MySQL Python Connector")
from connecting import connecting_db

db = connecting_db()

cursor = db.cursor()
database_input = input("Masukkan nama database : ")
cursor.execute("DROP DATABASE %s" %database_input)
print("Database %s selesai dihapus!" %database_input)