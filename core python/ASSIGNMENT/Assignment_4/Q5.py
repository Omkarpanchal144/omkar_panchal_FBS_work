#5. WAP to print Fibonacci series upto n. 

num=int(input("Enter the number of  terms : "))

a , b = 0 , 1
print("Fibonacci series :")

for i in range(num):
    print(a, end=" ")
    c=a+b
    a=b
    b=c

