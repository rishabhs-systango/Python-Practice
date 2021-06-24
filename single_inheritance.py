class Father :
    money = 1000
    def __init__(self) :
        print("Hello i m father constructor")
    def show(self) :
        print("Hello i m father Instance method")
    @classmethod
    def showMoney(cls) :
        print("Hello i m father classMethod",cls.money)
    @staticmethod
    def start() :
        print("Hello i m father staticmethod")

class Son(Father) :
    def display(self) :
        print("Hello i m son Instance method")
son = Son()
son.show()
son.showMoney()
son.start()
son.display()