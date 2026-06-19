import tkinter as tk
import random

CHOICES = ["Rock", "Paper", "Scissor"]


def play(user_choice):
    computer_choice = random.choice(CHOICES)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissor")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissor" and computer_choice == "Paper")
    ):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    label_computer.config(text=f"Computer chose: {computer_choice}")
    label_result.config(text=result)


root = tk.Tk()
root.title("Rock Paper Scissor")
root.geometry("320x220")

tk.Label(root, text="Choose your move:", font=("Arial", 12)).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Button(frame, text="Rock", width=8, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Paper", width=8, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Scissor", width=8, command=lambda: play("Scissor")).grid(row=0, column=2, padx=5)

label_computer = tk.Label(root, text="Computer chose: ", font=("Arial", 11))
label_computer.pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 14, "bold"))
label_result.pack(pady=10)

root.mainloop()