num = int(input("Hello, enter a number."))
sum=0
temp=num
while temp > 0:
    digit = temp %10 
    print(digit)
    sum += digit ** 3
    temp //= 10
if num==sum:
 print(num,"This is an armstrong number!")
else:
   print(num,"Is NOT an armstrong number!")