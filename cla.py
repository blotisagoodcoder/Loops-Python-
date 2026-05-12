class myHiro:
    __privateVar = 27;

    def _privMeth(self):
        print("I am INSIDE a TIME MACHINE HELP ME")
    def hello(self):
        print("Value right now or uh save Hiro:",myHiro.__privateVar)
foo = myHiro()
foo.hello()
foo._privMeth