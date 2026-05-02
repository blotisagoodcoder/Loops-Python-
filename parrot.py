class Parrot:
    species = "bird"

    def __init__(self,name,age):
        self.name = name
        self.age = age

blu = Parrot("Holo-Parrot",12)
Mika = Parrot("Mika",12)

print("Holo-Parrot is a {}".format(blu.species))
print("MIKA is also a {}".format(Mika.species))

print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(Mika.name, Mika.age))