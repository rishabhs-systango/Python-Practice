#else block when exception dosent occur
a = 10
b = 5
try :
    d = a/b
    print(d)
except ZeroDivisionError as obj:
    print(obj)
else :
    print("Division succesfully")
finally :
    print("I m in final block")

print("##########################")
# except block
a = 10
b = 0
try :
    d = a/b
    print(d)
except ZeroDivisionError :
    print('Division by zero not allowed')
else :
    print("Division succesfully")
finally :
    print("I m in final block")