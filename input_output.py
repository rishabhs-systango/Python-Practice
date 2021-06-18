# program to calculate BMR
'''
BMR for Men = 66.47 + (13.75 * weight [kg]) + (5.003 * size [cm]) − (6.755 * age [years])
BMR for Women = 655.1 + (9.563 * weight [kg]) + (1.85 * size [cm]) − (4.676 * age [years])
'''
gender = input("Enter male or Female\n")
if gender.upper() == 'MALE' :
    age = float(input("Enter Your age in years\n"))
    weight = float(input("Enter Your weight in KG\n"))
    height_in_feet = float(input("Enter Your height in feet\n"))
    # converting height in cm
    height_in_cm = height_in_feet/0.032808
    # calculating BMR
    bmr = 66.47 + (13.75 * weight) + (5.003 * height_in_cm) - (6.755 * age)
    print(f"YOUR BMR IS {bmr}\n")
elif gender.upper() == 'FEMALE' :
    age = int(input("Enter Your age in years\n"))
    weight = int(input("Enter Your weight in KG\n"))
    height_in_feet = float(input("Enter Your height in feet\n"))
    # converting height in cm
    height_in_cm = height_in_feet/0.032808
    # calculating BMR
    bmr = 655.1 + (9.563 * weight) + (1.85 * height_in_cm) - (4.676 * age)
    print(f"YOUR BMR IS {bmr}\n")
else : 
    print('Wrong Input')
