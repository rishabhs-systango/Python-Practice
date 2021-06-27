'''
Given a list of size N-1 such that it only contains distinct integers in the range of 1 to N. 
Find the missing element.
'''
#taking input
list_input = []
no_of_element = int(input("Enter no. of element in list\n"))
i = 0
while i < no_of_element :
    element = int(input("Enter number\n"))
    list_input.append(element)
    i+=1

def findMissing(list) :
    check = 1
    for item in list :
        if item != check :
            return check
        else :
            check = check + 1
print(findMissing(list_input))