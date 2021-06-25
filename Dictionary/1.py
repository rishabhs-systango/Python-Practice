'''
Sort the first list l1 such that all the relative positions of the elements in the first list
 are the same as the elements in the second list l2.
'''
l1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
l2 = [2, 1, 8, 3]
list_output = []
def sortList(l1,l2) :
    dict = {}
    for item in l1 :
        if item in dict :
            dict[item] = dict[item] + 1
        else :
            dict[item] = 1
    for item in l2 :
        if item in dict :
            count = dict[item]
            while count > 0 :
                list_output.append(item)
                count-=1
                if count == 0 :
                    del dict[item]
    
    for item in sorted(dict) :
        list_output.append(item)
    return list_output
print(sortList(l1,l2))