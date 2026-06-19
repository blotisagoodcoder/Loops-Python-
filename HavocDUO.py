import tkinter as tk
from tkinter import messagebox
from datetime import date
from calendar import monthrange
 
 
def calculate_age():
    try:
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())
        dob = date(year, month, day)
        today = date.today()
 
        years = today.year - dob.year
        months = today.month - dob.month
        days = today.day - dob.day
 
        if days < 0:
            months -= 1
            prev_month = today.month - 1 or 12
            prev_year = today.year if today.month != 1 else today.year - 1
            days += monthrange(prev_year, prev_month)[1]
 
        if months < 0:
            years -= 1
            months += 12
 
        if years < 0:
            raise ValueError("Date of birth is in the future.")
 
        label_result.config(text=f"Age: {years} years, {months} months, {days} days")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid date of birth.")
 
 
root = tk.Tk()
root.title("Age Calculator")
root.geometry("320x260")
 
tk.Label(root, text="Day:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_day = tk.Entry(root, width=10)
entry_day.grid(row=0, column=1, pady=10)
 
tk.Label(root, text="Month:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_month = tk.Entry(root, width=10)
entry_month.grid(row=1, column=1, pady=10)
 
tk.Label(root, text="Year:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
entry_year = tk.Entry(root, width=10)
entry_year.grid(row=2, column=1, pady=10)
 
tk.Button(root, text="Calculate Age", command=calculate_age).grid(
    row=3, column=0, columnspan=2, pady=15
)
 
label_result = tk.Label(root, text="Age: ", font=("Arial", 11, "bold"))
label_result.grid(row=4, column=0, columnspan=2, pady=10)
 
root.mainloop()