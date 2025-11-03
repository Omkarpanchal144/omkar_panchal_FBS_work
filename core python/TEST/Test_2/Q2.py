#Q2Write a program to accept 3 digit number. If first digit is double of second digit and half of
#third digit then display “Yes, you have done it”, otherwise display “Please try next time”.
#Eg : - 428 , 214 etc.


num=int(input("Enter the num"))

a=num%10

num=num//10
b=num%10

c=num//10

if(c>b and c<a):
    print("yes")
else:
    print("try next time")