str = '''Hello
Hy
How are Youu
         '''
print(str)
#raw string
str2 = r'hello\nhy'
print(str2)

str3 = "Hy Rishabh here"
print(str3[4])

#for in loop
for item in str3 :
    print(item)

#length of string using f string
print(f"length of string is {len(str2)}")

# concatenation and repetation
print(str2 +" "+ str3)
print(2*str3)

#in operator
print('zs' in str3)

#comparing string
print(str2 == str3)
print(str2>str3)

#string function
print(str2.upper())
print(str2.lower())
print(str2.isdigit())
print(str2.replace('h','z'))
print(str2)
