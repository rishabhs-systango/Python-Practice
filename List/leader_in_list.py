'''
Given an list A of positive integers. 
Your task is to find the leaders in the list. 
An element of list is leader if it is greater than or 
equal to all the elements to its right side. The rightmost element is always a leader. 
'''
import sys
list_input = [16,17,4,3,5,2]
def findLeader(list) :
    max = -sys.maxsize - 1
    list_leader = []
    i = len(list) - 1
    while i >= 0 :
        if list[i] >= max :
            max = list[i]
            list_leader.append(max)
        i-=1
    return list_leader
print(findLeader(list_input))