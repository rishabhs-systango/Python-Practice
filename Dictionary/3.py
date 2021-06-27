# Largest sublist with 0 sum
list = [15,-2,2,-8,1,7,10,23]
def subList(list) :
    sum = 0 
    len = 0
    dict = {}
    for item in list :
        sum = sum + item
        if sum == 0 and len == 0 :
            len = 1
        if sum == 0 :
            len = list.index(item) + 1
        if sum not in dict :
            dict[sum] = list.index(item)
        else :
            '''
            if the same value appears twice in the list,
            it will be guaranteed that the particular list will be a zero-sum sub-list
            '''
            len = max(len,list.index(item) - dict[sum])
    return len
print(subList(list))