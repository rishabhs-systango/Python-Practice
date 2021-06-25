#program to interchange first and last elements in a list

#approach1
list1 = [12, 35, 9, 56, 24]
def interChange(list1):
    list1[0] = list1[0] + list1[len(list1)-1]
    list1[len(list1)-1] = list1[0] - list1[len(list1)-1]
    list1[0] = list1[0] - list1[len(list1)-1]
interChange(list1)
print(list1)

#approach2
list2 = [87, 2, 3,77,92]
def interChange1(list2):
    list2[0],list2[-1] = list2[-1],list2[0]
interChange1(list2)
print(list2)