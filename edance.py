class Vehicle:
    def __init__ (self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

School_Bus = Bus("SCHOOL VOLVO", 180, 12)
print("VEHICLE NAME:", School_Bus.name, "SPEED:", School_Bus.max_speed, "MILEAGE:", School_Bus.mileage)
