import random
playing = True
number = str(random.randint(0,9))

print("HEY LOSER, I will summon a number from 0 to 9!")
print("The game ends when you get ONE hero! Hahahha!")

while playing:
    guess=input("GIVE ME YOUR BEST GUESS LOSER! \n")
    if number ==guess:
        print("DAMNI- you win the game nerd! But I will be back!")
        print("The Number was..",number)
        break
    else:
        print("HAHAHA YOU LOSE! TRY AGAIN HAHAHA- (gets hit by a frying pan) \n")