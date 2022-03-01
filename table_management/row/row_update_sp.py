import sys
sys.path.insert(0, "../MySQL Python Connector")
from connecting import connecting_db

db = connecting_db()
cursor = db.cursor()

# UPDATE <nama tabel> 
#   SET <nama kolom> = <var>
#   WHERE <nama tabel>.<id tabel> = <var>;

SQLCommand = """UPDATE nama_table2 
    SET 'age' = '24'
    WHERE 'nama_table2'.'id_two' = 2;
"""
cursor.execute(SQLCommand)

print("Tabel berhasil dimodifikasi!")