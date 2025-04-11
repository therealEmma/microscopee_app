import sqlite3
from microsope_calculator import calculate_real_size

# Connect or create the database
conn = sqlite3.connect("specimen_data.db")
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS specimen (
    username TEXT,
    microscope_size REAL,
    magnification REAL,
    actual_size REAL
)''')

# Save data
username = input("Enter your username: ")
microscope_size = float(input("Enter microscope size (in µm): "))
magnification = float(input("Enter magnification: "))
actual_size = calculate_real_size(microscope_size, magnification)

cursor.execute("INSERT INTO specimen VALUES (?, ?, ?, ?)", 
               (username, microscope_size, magnification, actual_size))

conn.commit()
conn.close()

print(f"Data saved! Real-life size is {actual_size:.2f} µm")
