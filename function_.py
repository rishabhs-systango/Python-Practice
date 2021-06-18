# Program to calculate BMI
'''
Formula: weight (kg) / [height (m)]2
'''
def calculateBMI() : 
    weight = float(input('Enter your weight in kg\n'))
    height_in_feet = float(input("Enter Your height in feet\n"))
    # converting height in meter
    height_in_m = height_in_feet/3.2808
    # calculating BMI
    bmi = weight/height_in_m**2
    print(f"YOUR BMI IS {bmi}\n")
calculateBMI()
