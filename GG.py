from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Denomination Calculator')
root.configure(bg='light blue')
root.geometry('650x400')
label = Label(root, bg='light blue')
label.place(x=180,y=20)

label1 = Label(root,
               text="Hello, User. Welcome to the Denomination Counter Application.",
               bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    Msgbox = messagebox.showinfo(
        "Alert", "Do you want to calculate the denomination count?")
    if Msgbox == 'ok':
       topwin()
    


button1 = Button(root,
                  text="Let's get started.",
                  command=msg,
                  bg='brown',
                  fg='white')

button1.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg='light gray')
    top.geometry("600x350+50+50")

    label = Label(top, text="Enter total amount", bg='light grey')
    entry = Entry(top)
    b1b = Label(top,text="Here are the number of notes for each denomination", bg='light gray')

    d1 = Label(top, text='2000',bg='light gray')
    d2 = Label(top, text='500',bg='light gray')
    d3 = Label(top, text='100',bg='light gray')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note2000= amount // 2000
            amount %=2000
            note500= amount//500
            amount %=2000
            note100 = amount // 100

            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))

        except ValueError:
            messagebox.showerror("ERROR", "Enter a Valid NUmber.")

    btn = Button(top, text="calculate", command=calculator, bg='brown', fg='white')

    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    b1b.place(x=140, y=170)

    d1.place(x=180, y=200)
    d2.place(x=180, y=230)
    d3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    top.mainloop()

root.mainloop()

            
    


            