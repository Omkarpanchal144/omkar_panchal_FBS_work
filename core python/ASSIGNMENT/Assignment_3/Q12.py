#12. Write a program to check if given 3 digit number is a palindrome or not. 
 
num=int(input("Enter the 3 digit number ="))

a=num //100
b=(num //10) % 10
c=(num % 10)

if(a == c):
    print(f'{num} is a palindrome number.')
else:
    print(f'{num}is a not palindrome number.')