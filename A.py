class A():
    def __init__(self,a):
        self.a = a
    def __lt__(self, other):
        if(self.a<other.a):
            return "OB1 LESS THAN OB2 IDIOT"
        else:
            return "OB2 IS LESS THAN OB1"
    def __eq__(self, other):
        if(self.a == other.a):
            return "BOTH EQUAL"
        else:
            return "NOT EQUAL"
    
ob1 =A(2)
ob2 = A(3)
print("PASSED VALUES:", ob1.a, ob2.a)
print(ob1<ob2)
