import tkinter as tk
from tkinter import messagebox
 
 
def calculate_product():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 * num2
        label_result.config(text=f"Product: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")
 
 
root = tk.Tk()
root.title("Product Calculator")
root.geometry("300x220")
 
tk.Label(root, text="Enter first number:").pack(pady=5)
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)
 
tk.Label(root, text="Enter second number:").pack(pady=5)
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)
 
tk.Button(root, text="Calculate Product", command=calculate_product).pack(pady=10)
 
label_result = tk.Label(root, text="Product: ", font=("Arial", 12, "bold"))
label_result.pack(pady=10)
 
root.mainloop()
