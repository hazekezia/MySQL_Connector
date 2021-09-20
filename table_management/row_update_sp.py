import sys
sys.path.insert(0, "../MySQL Python Connector")
from connecting import connecting_db1

db = connecting_db1()
cursor = db.cursor()

# UPDATE <nama tabel> 
#   SET <nama kolom> = <var>
#   WHERE <nama tabel>.<id tabel> = <var>;

SQLCommand = """UPDATE two 
    SET `umur` = '24'
    WHERE `two`.`id_two` = 2;
"""
cursor.execute(SQLCommand)

print("Tabel berhasil dimodifikasi!")