# Program to chcek You are underWeight overWeight or fit
'''
Formula to calculate BMI : weight (kg) / [height (m)]2
'''
def takeInput() : 
    #function to take input from users
    weight = float(input('Enter your weight in kg\n'))
    height_in_feet = float(input("Enter Your height in feet\n"))
    calculateBMI(weight,height_in_feet)

def calculateBMI(weight,height_in_feet) : 
    #function to calculate BMI
    # converting height in meter
    height_in_m = height_in_feet/3.2808
    # calculating BMI
    bmi = weight/height_in_m**2
    checkFitOrNot(bmi)

def checkFitOrNot(bmi) :
    '''
    function to check is user is overWight underWeight or fit
    If your BMI is less than 18.5, it falls within the underweight range. 
    If your BMI is 18.5 to 24.9, it falls within the normal or Healthy Weight range. 
    If your BMI is 25.0 to 29.9, it falls within the overweight range.
    If your BMI is 30.0 or higher, it falls within the obese range.
    '''
    if bmi < 18.5 :
        print("UnderWeight")
    elif bmi >= 18.5 and bmi <= 24.9 :
        print("Healthy Weight")
    elif bmi >= 25.0 and bmi <= 29.9 :
        print("OverWeight")
    elif bmi >= 30.0 :
        print("Obese")

takeInput()
