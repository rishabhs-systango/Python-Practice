# common elements
'''
Given two lists V1 and V2 of sizes n and m respectively. 
Return the list of elements common to both the lists and return the list in sorted order.
Duplicates may be there in the output list.
'''
v1 = [3,4,2,2,4]
v2 = [3,2,2,7]
def commonElements(v1,v2) :
    list_output = []
    dict = {}
    for item in v1 :
        if item not in dict :
            dict[item] = 1
        else :
            dict[item] = dict[item] + 1
    for item in v2 :
        if item in dict :
            count = dict[item]
            if count > 0 :
                list_output.append(item)
                dict[item] = dict[item] - 1
                    
    list.sort(list_output)
    return list_output

print(commonElements(v1,v2))