from abc import ABC, abstractmethod

class Absclass(ABC):
    def print (seld, x):
        print("Yo lowkey the passed value is =", x)
    @abstractmethod
    def task(self):
        print("YOO WE ARE INSIDE THE ABSCLASS BRO")

class test_class(Absclass):
    def task (self):
        print("WE ARE NOW INSIDE TEST_CLASS TASK, BEWARE FOR MONSTER-")

test_obj = test_class()
test_obj.task()
test_obj.print(100)