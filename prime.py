lower = int(input("ENTER A LOWER RANGE "))
upper = int(input("ENTER AN UPPERR RANGE "))

print("The prime numbers between", lower,"and", upper, "range are.. ")

for num in range (lower, upper + 1):
    if num > 1:
     for i in range (2, num):
         if (num % i) == 0:
          break
     else:
        print(num)