import math

def circumference(radius):
    return 2 * math.pi * radius

r = float(input("Enter the radius: "))
c = circumference(r)

print("The circumference is:", c)