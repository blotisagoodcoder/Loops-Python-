class Employee:
    def __init__(self):
        print("EMPLOYEE. CREATED (YO WDYM CREATED?)")
    def __del__(self):
        print("Destructor: CALLED")
def Create_obj():
    print('MAKING. OBJECT...')
    obj = Employee()
    print('FUNCTION: END')
    return obj
print('CALLING.. Create_obj() function...')
obj = Create_obj()
print("PROGRAM: DONE")