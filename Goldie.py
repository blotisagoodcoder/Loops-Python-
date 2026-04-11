try:
    num1, num2 = eval(input("Enter TWO. Numbers and please seperate them with a coma! "))
    result = num1/num2
    print("The result is....",result)

except ZeroDivisionError:
    print("DIVISION BY ZERO IS ERROR YOU MORON!!")

except SyntaxError:
    print("DUDE I TOLD YOU TO PLACE A COMA TO SEPERATE THEM! DO YOU WANT ME TO PUT YOU IN A COMA!?")

except:
    print("BRO, WRONG INPUT. WHY DO YOU NOT LIKE INSTRUCTIONS YOU IDIOT?!")

else: 
    print("NO EXCEPTIONS, NO FAVOURITISM TODAY!")

finally:
    print("The code is running successfully! ...And uhh, I hope you didn't ragebait BOB")