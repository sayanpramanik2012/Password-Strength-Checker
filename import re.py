import re
v=input("Enter the password:")
if(len(v)>=8):
    if(bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,30})',v))==True):
        print("The password entered is strong")
        print("Try to have different password for different application")
    elif(bool(re.match('((\d*)([a-z]*)([A-Z]*)([!@#$%^&*]*).{8,30})',v))==True):
        print("The password is weak")
        print("Try to use some special codes, Numerics and Caps words")
else:
    print("You have entered an invalid password, Use more than 8 letters")