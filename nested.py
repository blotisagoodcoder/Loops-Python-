word = (input("Please enter a word! "))

character = (input("What character in the word? "))

count=0

for i in word:
   if i == character:
      count= count+1
   
print("The character repeats for ",count)
