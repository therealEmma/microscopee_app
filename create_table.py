import sqlite3

conn = sqlite3.connect("specimen_data.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS specimen (
        username TEXT,
        microscope_size REAL,
        magnification REAL,
        actual_size REAL
    )
''')

cursor.execute("SELECT * FROM specimen")
rows = cursor.fetchall()

for row in rows:
    print(row)


conn.commit()
conn.close()

print("Table created successfully.")
