from checkFit import *
def calculateBMI(weight,height_in_feet) :
    '''
    Formula to calculate BMI : weight (kg) / [height (m)]2
    ''' 
    #function to calculate BMI
    # converting height in meter
    height_in_m = height_in_feet/3.2808
    # calculating BMI
    bmi = weight/height_in_m**2
    checkFitOrNot(bmi)