rows = int(input("ENTER ROW SIZE"))
for i in range(1, rows +1):
    for j in range (rows - i):
        print(" ", end=" ") 
    for k in range(1,2*i):
        print("*", end=" ")
    print()
 