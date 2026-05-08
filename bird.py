class Bird:
    def __init__(self):
        print("The Bird is READY")
    def whoisThis(self):
        print("BIRD")
    def swim(self):
        print("SWIM FASTER MORON")

class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("PENGUIN IS READY HEHEH")
    def whoisThis(self):
        print("Penguin")
    def run(self):
        print("RUN FASTER FATTY")
peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()