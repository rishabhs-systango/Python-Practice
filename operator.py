num1 = int(input('enter first no.\n'))
num2 = int(input('enter second no.\n'))
#add two no
print(f"addition of two number {num1} and {num2} is {num1 + num2}")
# subtract
print(f"subtraction of two number {num1} and {num2} is {num1 - num2}")
#multiplication
print(f"multiplication of two number {num1} and {num2} is {num1 * num2}")
# Division
print(f"Division of two number {num1} and {num2} is {num1 / num2}")
#modulus
print(f"modulus of two number {num1} and {num2} is {num1 % num2}")
# exponention
print(f"exponention of two number {num1} and {num2} is {num1 ** num2}")
# floor division
print(f"Floor division of two number {num1} and {num2} is {num1 // num2}")

###identity opertaor
print('-----identity-------')
x = [1,2]
y = [1,2]
z = x           #Assignment operator
print(x is z)
print(x is y)
print(x is not z)
print(x is not y)

# membership operator
print('-----membaership-------')
bike = ['ktm','rs','fz']
print('rs' in bike)
print('rs' not in bike)
