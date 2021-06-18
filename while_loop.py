#program for giving 5 chance to enter your password just like we have in our phone
password = input('Enter Your Password\n')
print('password confrmed\n')
'''
now we will check the password reentering is same or not and giving 5 chance to unclock if
not correct phone will locked for 30 min
'''
count = 5
while count > 0 :
    reEnterPassword = input('Enter password to unlock your Phone\n')
    if password == reEnterPassword :
        print('Phone Unlocked')
        break
    # Checking is uesr entered wrong password for the 5th time
    elif count == 1 :
        print('Phone Locked for 30min')
    else :
        print('Wrong Password Try again')
    count-=1
