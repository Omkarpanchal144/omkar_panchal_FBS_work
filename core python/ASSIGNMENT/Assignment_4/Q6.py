#6. WAP to check if a given number is prime number or not. 


num=int(input("gfee:"))
for i in range(2,num):
    if(num%i==0):
        print("Not prime number")
        break
    else:
        print("prime number")