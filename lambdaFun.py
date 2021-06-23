# wite same string thrice through lambda function
def writeThrice(string) :
    return lambda : 3*string
lambdafun = writeThrice("Hello\n")
print(lambdafun())

# add two number using lambda fun
addition = lambda num1,num2 : num1 + num2
print(addition(10,20))

#multiply x^y no. using lambda function
exponent = lambda num1,num2 : num1**num2
print(exponent(2,3))