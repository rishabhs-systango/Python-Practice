# longest pallindrome
str = input("Enter the string\n")

def reverse(str):
    str1 = str[-1:-len(str)-1:-1]
    return str1

str_reverse = reverse(str)
def longestPallindrome(str) :
    i = 0
    j = 0
    str_pallindrome = ""
    while i < len(str)-1:
        j = i + 1
        while j <= len(str) :
            str_check = str[i:j]
            if len(str_check) > len(str_pallindrome) and str_check in str_reverse :
                str_pallindrome = str_check
            j+=1
        i+=1
    return str_pallindrome

print(longestPallindrome(str))