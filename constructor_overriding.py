#constructor overriding
class Father :
    def __init__(self) :
        print("Hello i m father constructor")

class Son(Father) :
    def __init__(self) :
        print("Hello i m son constructor")

    def display(self) :
        print("Hello i m son Instance method")
son = Son()

#constructor with super keyword to call both the contsructor father and son

class Son1(Father) :
    def __init__(self) :
        super().__init__()
        print("Hello i m son1 constructor")

    def display(self) :
        print("Hello i m son Instance method")
son1 = Son1()