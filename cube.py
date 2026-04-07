def cube(number):
    return number*number*number

def by_three(number):
    if number %3 ==0:
        return cube(number)
    else:
        return False

n=int(input("ENTER YOUR NUMBER"))
print(by_three(n))
