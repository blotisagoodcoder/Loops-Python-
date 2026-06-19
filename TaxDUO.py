import tkinter as tk
from tkinter import messagebox
 
 
def calculate_interest():
    try:
        p = float(entry_principal.get())
        t = float(entry_time.get())
        r = float(entry_rate.get())
 
        simple_interest = (p * r * t) / 100
        compound_interest = p * ((1 + r / 100) ** t) - p
 
        label_simple.config(text=f"Simple Interest: {simple_interest:.2f}")
        label_compound.config(text=f"Compound Interest: {compound_interest:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")
 
 
root = tk.Tk()
root.title("Interest Calculator")
root.geometry("320x300")
 
tk.Label(root, text="Principal Amount:").pack(pady=5)
entry_principal = tk.Entry(root)
entry_principal.pack(pady=5)
 
tk.Label(root, text="Time (years):").pack(pady=5)
entry_time = tk.Entry(root)
entry_time.pack(pady=5)
 
tk.Label(root, text="Rate of Interest (%):").pack(pady=5)
entry_rate = tk.Entry(root)
entry_rate.pack(pady=5)
 
tk.Button(root, text="Calculate", command=calculate_interest).pack(pady=10)
 
label_simple = tk.Label(root, text="Simple Interest: ", font=("Arial", 10, "bold"))
label_simple.pack(pady=5)
 
label_compound = tk.Label(root, text="Compound Interest: ", font=("Arial", 10, "bold"))
label_compound.pack(pady=5)
 
root.mainloop()