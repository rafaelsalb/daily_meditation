from settings import database_name, TABLE_MODELS, TABLE_COUNT
import sqlite3


con = sqlite3.connect(database_name + ".db.sqlite3")
cur = con.cursor()
for i in range(TABLE_COUNT):
    cur.execute(f"CREATE TABLE IF NOT EXISTS {TABLE_MODELS[i]().name} ({TABLE_MODELS[i]().create_columns_to_str()});")
con.close()
