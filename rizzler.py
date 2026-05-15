from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can commit taxt fraud")
class Snake(Animal):
    def move(self):
        print("I can poison ur body and u will die in vain")
class Dog(Animal):
    def move(self):
        print("I can bite your legs")
class Lion(Animal):
    def move(self):
        print("I can eat u")

R = Human()
R.move()

K = Snake()
K.move()

R= Dog()
R.move 

K = Lion()
K.move
