class LowBalanceException(Exception) :
    def __init__(self, args) :
        self.msg = args

def checkBalance() :
    balance = 1000
    withdrawl_amnt = 1100
    try :
        if withdrawl_amnt > balance :
            raise LowBalanceException("Insufficient amount")
    except Exception as obj :
        print(obj)
    else :
        balance = balance - withdrawl_amnt
        print(balance)
checkBalance()