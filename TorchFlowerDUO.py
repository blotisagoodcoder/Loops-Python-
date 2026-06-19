import tkinter as tk
 
 
def check_strength():
    password = entry_password.get()
    length = len(password)
 
    if length == 0:
        strength = "Please enter a password"
        color = "black"
    elif length < 6:
        strength = "Weak"
        color = "red"
    elif length < 10:
        strength = "Medium"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"
 
    label_result.config(text=f"Strength: {strength}", fg=color)
 
 
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("320x200")
 
tk.Label(root, text="Enter your password:").pack(pady=10)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)
 
tk.Button(root, text="Check Strength", command=check_strength).pack(pady=10)
 
label_result = tk.Label(root, text="Strength: ", font=("Arial", 12, "bold"))
label_result.pack(pady=10)
 
root.mainloop()