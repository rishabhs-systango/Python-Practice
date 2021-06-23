#returning anything from function
num1 = int(input("Enter number\n"))
num2 = int(input("Enter number\n"))

def add(num1,num2) :
    return num1+num2
print(f"addition of two number {num1} and {num2} is {add(num1,num2)}")