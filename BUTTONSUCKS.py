from tkinter import*
window = Tk()
window.title("EVENT HANDLER")
window.geometry("100x100")

def handle_click(event):
    print("\nTHE BUTTON WAS CLOCKED!111")

button = Button(text="ClICK ME NOw!!")
button.pack()

button.bind("<Button-1>",handle_click)
window.mainloop()