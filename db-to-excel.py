import tkinter as tk
from tkinter import filedialog
import pandas as pd
import sqlite3

def select_db_file():
    filepath = filedialog.askopenfilename(title="Select Database File", filetypes=[("Database Files", "*.db")])
    db_entry.delete(0, tk.END)
    db_entry.insert(0, filepath)

def convert_to_excel():
    db_path = db_entry.get()
    if not db_path:
        tk.messagebox.showerror("Error", "Please select a database file")
        return

    conn = sqlite3.connect(db_path)
    # cursor = conn.cursor()

    query = "SELECT * FROM sqlite_master WHERE type='table';"
    df = pd.read_sql_query(query, conn)

    conn.close()

    output_file = "output.xlsx"
    df.to_excel(output_file, index=False)
    tk.messagebox.showinfo("Conversion complete.", f"Output saved as {output_file}")

root = tk.Tk()
root.title("Database to Excel Converter")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

db_label = tk.Label(frame, text="Select Database File:")
db_label.grid(row=0, column=0)

db_entry = tk.Entry(frame, width=40)
db_entry.grid(row=0, column=1, padx=5)

db_button = tk.Button(frame, text="Browse", command=select_db_file)
db_button.grid(row=0, column=2, padx=5)

convert_button = tk.Button(frame, text="Convert to Excel", command=convert_to_excel)
convert_button.grid(row=1, columnspan=3, pady=10)

root.mainloop()
