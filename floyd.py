print("A Pyramid: BUT NUMBERS?")
n = int(input("ENTER NUMBER. "))
for i in range (n+1):
  for j in range (i):
     print(j, end=" ")
  print()