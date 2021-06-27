'''
For an list, inversion count indicates how far (or close) the list is from being sorted. 
If list is already sorted then the inversion count is 0. 
If an list is sorted in the reverse order then the inversion count is the maximum. 
'''
list_input = [2, 4, 1, 3, 5]
def find_inversion_count(list) :
    count = 0
    i = 0
    while i < len(list)-1 :
        j = i + 1
        while j < len(list) - 1 :
            if list[i] > list[j] :
                count+=1
            j+=1
        i+=1
    return count
print(find_inversion_count(list_input))
