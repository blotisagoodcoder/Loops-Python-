import array as arr

G = arr.array('i',[1,3,5,3,7,9,3])
print("Original array: "+str(G))

print("NUMBER OF OCCURENSES: 3"+str(G.count(3)))

G.reverse()
print("REVERSE ORDER:")
print(str(G))