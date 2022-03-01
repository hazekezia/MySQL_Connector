import sys
sys.path.insert(0, "../MySQL Python Connector")
from connecting import connecting_db

db = connecting_db()
cursor = db.cursor()

# ALTER TABLE <nama tabel>
#   ADD COLUMN product_id VARCHAR(255) NOT NULL;
#   DROP COLUMN <nama kolom>;
#   MODIFY COLUMN <nama kolom> <tipedata>;

SQLCommand = """ALTER TABLE nama_table
ADD COLUMN id_ext INT(11) NOT NULL,
ADD COLUMN age VARCHAR(2) NOT NULL
"""
cursor.execute(SQLCommand)

print("Tabel berhasil dimodifikasi!")