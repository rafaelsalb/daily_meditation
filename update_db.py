import sys
import sqlite3
from settings import database_name
import models


con = sqlite3.connect(database_name + ".db.sqlite3")
cur = con.cursor()
cur.execute(f"INSERT INTO {models.Test().name} ({models.Test().columns_to_str()}) VALUES ('teste')")
con.commit()
res = cur.execute(f"SELECT * FROM test")
print(res.fetchall())
con.close()
