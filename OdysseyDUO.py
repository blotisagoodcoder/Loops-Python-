import tkinter as tk
from tkinter import messagebox
 
 
def convert_length():
    try:
        inches = float(entry_inches.get())
        cm = inches * 2.54
        label_result.config(text=f"{inches} inches = {cm:.2f} cm")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
 
 
root = tk.Tk()
root.title("Length Converter (Inches to CM)")
root.geometry("320x200")
 
tk.Label(root, text="Enter length in inches:").pack(pady=10)
entry_inches = tk.Entry(root)
entry_inches.pack(pady=5)
 
tk.Button(root, text="Convert to CM", command=convert_length).pack(pady=10)
 
label_result = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"))
label_result.pack(pady=10)
 
root.mainloop()
 