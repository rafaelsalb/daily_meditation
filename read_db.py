import sqlite3
import sys


con = sqlite3.connect("meditations.db.sqlite3")
cur = con.cursor()

print()
elements = cur.execute(f"SELECT * FROM {sys.argv[1]}").fetchall()
for line in elements:
    print(line)
print()
con.close()
