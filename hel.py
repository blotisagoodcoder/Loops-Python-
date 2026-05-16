class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+'('+self.meaning+')'
flash=[]
print("WELCOME.")
while (True):
    word = input("Enter name you wanna add to a flashcard")
    meaning = input("Enter meaning of the word")
    flash.append(flashcard(word,meaning))
    option = int(input("Enter 0, if u want to add another flashcard otherwise enter 1"))
    if option:
        break
print("\nYour flashcards")
for i in flash:
    print(">",i)
