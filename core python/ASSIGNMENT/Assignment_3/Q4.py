#Write a program to input all sides of a triangle and check whether triangle is valid or not.

a=int(input("Enter the Frist side ="))
b=int(input("Enter the second side ="))
c=int(input("Enter the thried side ="))

#calculate the vaild side
if(a+b > c) and (a+c > b) and (b+c > a):
    print("triangle vaild side.")
else:
    print("Triangle not vaild side.")