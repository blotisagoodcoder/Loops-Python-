def factorial(x):
    '''this is a recursive function to find the factorial of an integer'''
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)

print(factorial.__doc__)
print("the factorial of 0",factorial(0))
print("the factorial of 5",factorial(5))



def fact(num):
    f=1
    for i in range(1,num+1):
        f=f*1
    print("Factorial of a number is ",f)
num=int(input("ENTER A NUMBER HOOMAN! "))
fact(num)