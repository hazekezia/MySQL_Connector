import sys
sys.path.insert(0, "../MySQL Python Connector")
from connecting import connecting_db1

db = connecting_db1()
cursor = db.cursor()

# ALTER TABLE <nama tabel>
#   ADD <nama kolom> <tipedata>;
#   DROP COLUMN <nama kolom>;
#   MODIFY COLUMN <nama kolom> <tipedata>;

SQLCommand = """ALTER TABLE two 
    ADD umur CHAR(3) NOT NULL;
"""
cursor.execute(SQLCommand)

print("Tabel berhasil dimodifikasi!")