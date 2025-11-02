#QWrite a program to check whether the triangle is equilateral, isosceles or scalene triangle.

a=int(input("Enter the Frist side ="))
b=int(input("Enter the second side ="))
c=int(input("Enter the thried side="))

if(a + b > c)and(a + c > b)and( c + b > a):
#if((a > 0) and (b>0) and (c > 0) and(a+b+c == 180)):
#if(a+b+c == 180):
    if(a == b == c):
        print("equilateral triangle.")
    elif (a == b) or (b == c) or (a == c):
        print("isosceles triangle.") 
    else:
        print("scalene triangle.")
else:
    print("Triangle is not vaild")