#7. Write a program to check if user has entered correct userid and password. 
UI="Omkar8999"
Pw="Omkar@123"

Uid=input("Enter the user ID :")
Password=input("Enter the password :")
if(UI==Uid and Pw==Password):
    print("login successfully")
else:
    print("worng username and password")
