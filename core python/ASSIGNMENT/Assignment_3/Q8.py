#8. Write a program to prompt user to enter userid and password. After verifying 
#userid and password display a 4 digit random number and ask user to enter the 
#same. If user enters the same number then show him success message otherwise 
#failed. (Something like captcha) ?

import random
UI="Omkar8999"
Pw="Omkar@123"

Uid=input("Enter the user ID :")
Password=input("Enter the password :")

if(UI==Uid and Pw==Password):

    captcha=random.randint(1111,9999)
    print("captcha=",captcha)
    
    user_captcha = input("Enter the CAPTCHA shown above: ")
    
    if(user_captcha == str(captcha)):
        print("login successfully.")
    else:
        print("Failed CAPTCHA did not match.")
    
else:
    print("worng username and password")
