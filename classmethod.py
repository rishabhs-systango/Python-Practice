class Car :
    cls_var = "hy"
    @classmethod
    def change(cls) :
        cls.cls_var = "Hello"
    
alto = Car()
nano = Car()
alto.cls_var = "Bye"         #create new variable not change the actual class variable
print(Car.cls_var)           #hy
print(alto.cls_var)          #Bye
print(nano.cls_var)           #hy
Car.change()
print("###########")
maruti = Car()
audi = Car()
print(Car.cls_var)           
print(maruti.cls_var)          
print(audi.cls_var)  
