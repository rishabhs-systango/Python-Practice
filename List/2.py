#Longest Substring Without Repeating Characters
str = input("Enter the string\n")
def findLongestSubstring(str) :
    dict = {}
    str_longest_Substring = ""
    str_check = ""
    i = 0
    while i < len(str) :
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
                                                                                          