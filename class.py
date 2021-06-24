class Car :
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    def display(self) :
        print("I m in instance method")
        print(f"Car is of Brand {self.brand} and color is {self.color}")
    
car = Car("BMW","Black")
print(car.brand)
car.display()
#changing color of a car
car.color = "Blue"
car.display()
#dleting object propert
del car.color
