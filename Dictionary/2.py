#Sorting Elements of an list by Frequency 
list = [1,5,6,1,2,4,1,2,4,6,1]
def sortByFrequency(list) :
    list.sort()
    dictionary = {}
    list_output = []
    for item in list :
        if item in dictionary :
            dictionary[item] = dictionary[item] + 1
        else :
            dictionary[item] = 1
    for item in dict( sorted(dictionary.items(),
                           key=lambda item: item[1],
                           reverse=True)) :
        frequency = dictionary[item]
        while frequency > 0 :
            list_output.append(item)
            frequency-=1
    return list_output
print(sortByFrequency(list))