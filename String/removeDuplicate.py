#remove duplicate
str = input("Enter the string\n")
def removeDuplicate(str) :
    dict = {}
    for item in str :
        dict[item] = 1
    str_output = ""
    for item in dict :
        str_output = str_output + item
    return str_output
print(removeDuplicate(str))