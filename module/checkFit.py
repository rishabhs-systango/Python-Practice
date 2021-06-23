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