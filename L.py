L=[27,24,18,25,1000,15]
print("ORIGINAL LIST IS!: ",L)

count = 0
for i in L:
    count+=i
avg = count/len(L)

print("SUM = ",avg)
print("average =", avg)

L.sort()
print("SmallesT ELEMENT ISSSS:", L[0])
print("ON THE OTHER HAND. THE LARGEST IS..:", L[-1])
