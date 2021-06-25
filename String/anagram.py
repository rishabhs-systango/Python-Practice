# tWo strings are anagram or not
'''
task is to check whether two given strings are an anagram of each other or not.
 An anagram of a string is another string that contains the same characters,
 only the order of characters can be different.
'''
str1 = input("Enter 1st string\n")
str2 = input("Enter 2nd string\n")
def checkAnagram(str1,str2) :
    dict = {}
    for item in str1 :
        if item in dict :
            dict[item] = dict[item] + 1
        else :
            dict[item] = 1
    for item in str2 :
        if item in dict :
            if dict[item] == 1 :
                del dict[item]
            else :
                dict[item] = dict[item] - 1
    if len(dict) == 0 :
        return "Both string are anagrams"
    else :
        return "Both string are not anagrams" 
print(checkAnagram(str1,str2))