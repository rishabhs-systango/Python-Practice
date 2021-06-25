# Reverse a input string
str = input("Enter the string\n")
def reverse(str):
    str1 = str[-1:-len(str)-1:-1]
    return str1
print(reverse(str))