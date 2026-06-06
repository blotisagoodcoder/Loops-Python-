from tkinter import *
root = Tk()
root.title('login App!')
root.geometry('400x400')
frame = Frame(master=root,height=200,width=360, bg='#017190')
b1l1 = Label(frame, text = "Full Name", bg="#B0DECE", fg='white', width=12)
b1l2= Label(frame, text="EMAIL ID", bg="#FFB9B9", fg='white', width=12)
b1l3= Label(frame, text="ENTER PASSWORD", bg="#6D1F1F", fg='white', width=12)

name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show="*")

def display():
    name = name_entry.get()
    greet = "HELLO" + name
    message = "\nCongrats for ur new acc lol"
    textbox.insert(END,greet)
    textbox.insert(END,message)


textbox = Text(bg="#BEBEBE", fg='black')
btn = Button(text="CREATE ACC", command=display,bg="red")

frame.place(x=20,y=0)
b1l1.place(x=20, y=20)
name_entry.place(x=150, y=20)
b1l2.place(x=20, y=80)
email_entry.place(x=150, y=80)
b1l3.place(x=20,y=140)
pass_entry.place (x=150, y=140)
btn.place(x=130, y=210)
textbox.place(y=250)

root.mainloop()

