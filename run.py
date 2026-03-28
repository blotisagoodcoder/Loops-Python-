num = input("HELLO MORTAL! Enter the number that you seek to know the total digits of that I will fulfill!: ")

count = 0

while num != "":
    count += 1
    num = num[1:]

print("Total digits:", count)