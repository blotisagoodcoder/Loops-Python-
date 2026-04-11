valid = False
while not valid:
    try:
        n=int(input("ENTER A NUMBER. PLEAASEE! "))
        while n%2==0:

            print("Farewell mortal human! We will meet again once I, Fischl. The Prinssezin of this world will make a name for myself!")

        valid = True
    except ValueError:
        print("Ahem!? Excuse me!? Hath you not have any dignity!? Get your puny being out of my sight!")