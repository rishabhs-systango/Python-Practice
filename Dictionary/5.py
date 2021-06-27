# Check if two list are equal or not
'''
Two list are said to be equal if both of them contain same set of elements, 
arrangements (or permutation) of elements may be different though.
''' 
l1 = [1,2,5,4,0]
l2 = [2,4,5,0,1]
def check(l1,l2) :
    dict = {}
    for item in l1 :
        if item not in dict :
            dict[item] = 1
        else :
            dict[item] = dict[item] + 1
    for item in l2 :
        if item in dict :
            if dict[item] == 1 :
                del dict[item]
            else :
                dict[item] = dict[item] - 1
    if len(dict) == 0 :
        return True
    else :
        False
print(check(l1,l2))
                    