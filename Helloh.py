class Dog:
    species = "Canine"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def show(self):
        print("Name:", self.name)
        print("Breed:", self.breed)
        print("Species:", Dog.species)
        print()

dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")

dog1.show()
dog2.show()