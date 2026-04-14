import random 
while True:
    user_action = input("ENTER! ROCK, PAPER, SCISSORS!  ")
    possible_actions = ["ROCK","PAPER","SCISSORS"]

    computer_action = random.choice(possible_actions)
    print(f"\nYou CHOSE... {user_action}, I CHOSE...{computer_action}.\n")

    if user_action == computer_action:
        print(f"BOTH HAVE CHOSEN THE SAME ONE! A TIE!")
    elif user_action =="ROCK":
        if computer_action == "SCISSORS":
            print("ROCK SMASHES THE SCISSORS! YOUU WIN!")
        else:
            print("PAPER COVERSS ROCK! YOUU LOSE!")
            
    elif user_action =="PAPER":
        if computer_action == "ROCK":
            print("PAPER COVERS ROCK1! YOUU WIN!")
        else:
            print("SCISSORS SLICES THROUGH THE PAPER!! YOUU LOSE!")

    elif user_action =="SCISSORS":
        if computer_action == "paper":
            print("SCISSORS SLICES PAPER!! YOUU WIN!")
        else:
            print("ROCK SMAASHES SCISSORS!!! YOUU LOSE!")

    play_again = input("PLAY AGAIN!? (y/n  )")
    if play_again != "y":
        break



