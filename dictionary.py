dict = {
    "Name" : "Rishabh",
    "age" : 22,
    "Roll_No" : "41"
}
print(dict)
#accessing dictionary item
print(dict["Name"])
#accessing all kesy as a list
list_of_keys = dict.keys()
print(list_of_keys)
dict["Location"] = "Ujjain"
print(list_of_keys) 

#accessing all kesy as a list
list_of_values = dict.values()
print(list_of_values)

#accessing all kesy as a list
list_of_items = dict.items()
print(list_of_items)

#Removing item from a list
dict.pop("Location")
print(dict)

#loops
for item in dict.keys() :
    print(item)

for item in dict.values() :
    print(item)

for item in dict.items() :
    print(item)
print("\ndictionary\n")
for item in dict :
    print(item)
    print(dict[item])
