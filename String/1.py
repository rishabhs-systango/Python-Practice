#Longest Substring Without Repeating Characters
str = input("Enter the string\n")
def findLongestSubstring(str) :
    #creating dictionary which will tract character and its index as key value pair
    dict = {}
    str_longest_Substring = ""
    str_check = ""
    i = 0
    while i < len(str) :
        #checking is character is presnt in our dictionary
        if str[i] in dict.keys() :
            i = dict[str[i]]
            dict.clear()
            str_check = ""
        else :
            dict[str[i]] = i
            str_check = str_check + str[i]
            if len(str_check) > len(str_longest_Substring) :
                str_longest_Substring = str_check   
        i+=1
    print(str_longest_Substring)
findLongestSubstring(str)