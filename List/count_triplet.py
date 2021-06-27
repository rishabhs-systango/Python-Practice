'''
count all the triplets such that sum of two elements equals the third element.
'''
#taking input
list_input = []
no_of_element = int(input("Enter no. of element in list\n"))
i = 0
while i < no_of_element :
    element = int(input("Enter number\n"))
    list_input.append(element)
    i+=1

def countTriplet(list) :
    dict = {}
    count = 0
    for item in list :
        dict[item] = 1
    i = 0
    while i < len(list) - 1 :
        j = i +1
        while j < len(list) :
            sum = list[i] + list [j]
            if sum in dict :
                count+=1
            j+=1
        i+=1
    return count

print(countTriplet(list_input))
