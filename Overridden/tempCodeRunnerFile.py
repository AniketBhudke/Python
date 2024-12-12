
class c1:
    def __init__(self):
        print("It is C1 class constructor")

class c2():
    def __init__(self):
        print("It Is C2 class Constructor")

class c3(c2,c1):
    def __init__(self):
        print("It Is C3 class Constructor")
        super().__init__()
        c1.__init__(self)

c=c3()
