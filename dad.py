class dad:
    def __init__(self,eyes,aggressive):
        self.eyes = eyes
        self.aggressive = aggressive
    
    def display(self):
        print("YOUR EYE COLOR IS...", self.eyes)
        print("YOU ARE ALSO AGGRESSIVE", self.aggressive)

class son(dad):
    def __init__(self,name,age,eyes,aggressive):
        self.name = name
        self.age = age

        dad.__init__(self,eyes,aggressive)

obj = son("Dannie", 9, "Green", True)
obj.display()