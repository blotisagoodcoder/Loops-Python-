class fruit:
    taste = "Sweet"
    def __init__(self,name,color):
        self.name = name
        self.color = color

KilaFruit = fruit('Kila', 'Yellowish-Brown')
Guavea = fruit('Guave', 'Green-Turtle')

print(KilaFruit.taste)
print(KilaFruit.name, KilaFruit.color)
print(Guavea.name, Guavea.color)
