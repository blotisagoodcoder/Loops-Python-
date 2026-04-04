def add(P,Q):
    return P + Q
def substract(P, Q):
    return P - Q
def multiplication(P, Q):
    return P * Q
def divide(P,Q):
    return P / Q



print("Select you're operation XD")
print("A:ADDITION")
print("S:SUBSTRACTION")
print("M:MULTIPLY")
print("D:DIVIDE")

choice = input("ENTER UR CHOICE: ")
num_1 = int(input("Please enter first number: "))
num_2 = int(input("Please enter second number: "))
if choice =='a':
    print (num_1, '+', num_2,'=', add(num_1,num_2))

elif choice =='b':
    print (num_1, '-', num_2,'=', substract(num_1,num_2))

elif choice =='c':
    print (num_1, '*', num_2,'=', multiply(num_1,num_2))

elif choice =='d':
    print (num_1, '/', num_2,'=', divide(num_1,num_2))

else:
    print('INVALID INPUT')