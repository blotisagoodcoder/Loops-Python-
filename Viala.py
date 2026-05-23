from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def speed(self):
        pass

class BMW(Vehicle):
    def speed(self):
        print("BMW is uh fast")

class Ferrari(Vehicle):
    def speed(self):
        print("Ferrari runs very fast")

car1 = BMW()
car2 = Ferrari()

for car in (car1, car2):
    car.speed()