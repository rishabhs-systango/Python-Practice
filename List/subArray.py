#Subarray with given sum
'''
Given an unsorted List list of size no_of_element that contains only non-negative integers, 
find a continuous sub-list which adds to a given number Sum.
'''
no_of_element = int(input("Enter no. of element in list\n"))
sum = int(input("Enter sum\n"))
list_input = []
list_output = []
# taking flag so that we can change flag to true if we get a sub list
flag = False
i = 0
# taking inputs of list
while i < no_of_element :
    element = int(input("Enter number\n"))
    list_input.append(element)
    i+=1
i = 0
while i < len(list_input) : 
    sum_current = 0
    j = i
    while j < len(list_input) :
        sum_current = sum_current + list_input[j]
        if sum_current == sum :
            list_output.append(i+1)
            list_output.append(j+1)
            flag = True
            break
        j+=1
    i+=1
    if flag :
        break
if flag :
    print(list_output)
else :
    print(-1)

    