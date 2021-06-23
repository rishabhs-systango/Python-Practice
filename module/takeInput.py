import calculateBmiModule as module
def takeInput() : 
    #function to take input from users
    weight = float(input('Enter your weight in kg\n'))
    height_in_feet = float(input("Enter Your height in feet\n"))
    module.calculateBMI(weight,height_in_feet)
takeInput()