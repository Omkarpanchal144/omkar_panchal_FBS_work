#10. Write a program to check if person is eligible to marry or not (male age >=21 and 
#female age>=18) 
gender=input("Enter the person gender (male / female) =")
age=int (input("Enter the age ="))

if(gender == "male" and age >= 21):
    print("Eligible for marriage.")

elif(gender == "female" and age >= 18):
    print("Eligible for marriage.")

else:
    print("Not Eligible in person marriage ")