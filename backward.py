print("A Pyramid Pattern:TYPE:STARS")
n = int(input("ENTER NUMBER OF ROWS."))
for i in range(n,0,-1):
  for j in range (i):
    print("* ", end="")
  print()