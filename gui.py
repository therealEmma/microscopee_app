import tkinter as tk
from tkinter import messagebox
import sqlite3

def save_data():
    try:
        username = username_entry.get()
        microscope = float(microscope_entry.get())
        magnification = float(magnification_entry.get())
        actual = microscope / magnification
        
        # DB stuff
        conn = sqlite3.connect("specimen_data.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO specimen VALUES (?, ?, ?, ?)", 
                       (username, microscope, magnification, actual))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", f"Real-life size: {actual:.2f} µm\nData Saved!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI
root = tk.Tk()
root.title("Microscope Size Calculator")

tk.Label(root, text="Username").grid(row=0)
tk.Label(root, text="Microscope Size (µm)").grid(row=1)
tk.Label(root, text="Magnification").grid(row=2)

username_entry = tk.Entry(root)
microscope_entry = tk.Entry(root)
magnification_entry = tk.Entry(root)

username_entry.grid(row=0, column=1)
microscope_entry.grid(row=1, column=1)
magnification_entry.grid(row=2, column=1)

tk.Button(root, text="Calculate & Save", command=save_data).grid(row=3, column=1)

root.mainloop()
