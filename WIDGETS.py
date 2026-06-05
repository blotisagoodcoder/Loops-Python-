from tkinter import *
from datetime import date

root = Tk()
root.title = ("WIDGETS YEY")
root.geometry('400x300')

b1b = Label(root, text = "SUP BROSKI", bg = '#072F5F', height=1,width = 100)
b1b.pack()

name_b1b = Label(root, text = "ENTER NAME NOW!", bg="#3895D3", width=4000)
name_b1b.pack()

name_entry = Entry(root, width = 30)
name_entry.pack(pady=10)

text_box = Text(root, height = 5, width = 45)
text_box.pack(pady=10)

def display():
    name = name_entry.get()
    if name.strip():
        text_box.delete('1.0',END)
        greet = f'hell {name}\n'
        message = f'WELCOME IDIOT.\n DATE TODAY IS: {date.today()}'
        text_box.insert(END,greet + message)
    else:
        text_box.delete('1.0','ENTER YOUR FULL NAME YOU-')

btn = Button(root, text="START NOW", command=display, bg="#1261A0",fg='white')
btn.pack()

root.mainloop()