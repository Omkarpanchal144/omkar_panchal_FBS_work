#3. Write a program to input angles of a triangle and check whether triangle is valid or not.

a=int(input("Enter the Frist angle ="))
b=int(input("Enter the second angle ="))
c=int(input("Enter the thried angle ="))

#calculate the vaild side
if((a > 0) and (b>0) and (c > 0) and(a+b+c == 180)):
    print("triangle vaild angle.")
else:
    print("Triangle not vaild angle.")