from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("500x500")

def msg():

    messagebox.showwarning("Alert!","STOP IT U IDIOT THERES A VIRUS IN UR COMPUTER!!111")
def msg1():

    messagebox.showerror("ERROR","ERROR FOUND. CHECK DEVICE.")

def msg2():
    messagebox.showinfo("Info", "DISPLAY INFO: Nothing")

def msg3():

    messagebox.askquestion("Ask  ", "Are you reaady for a daaaree???")


button = Button(root, text="Scan for Virus", command=msg)
button.place(x=40, y=50)
button = Button(root, text="ERROR MSSG", command=msg1)
button.place(x=40, y=100)
button = Button(root, text="SHOW INFO", command=msg2)
button.place(x=40, y=200)
button = Button(root, text="ASK", command=msg3)
button.place(x=40, y=250)
root.mainloop()
