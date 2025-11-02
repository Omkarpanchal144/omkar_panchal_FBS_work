# write a program to accept year form user and check if is a leap year or not 

year =int(input("Enter the leap year :-"))

if(year%4==0):
    if(year% 100==0 ):
        if(year%40==0):
           print("is a leap year.",year)
        else:
            print("is not leap year.",year)        
    else:
        print(" is a leap year.",year)
else:
    print("is not a leap year.",year)