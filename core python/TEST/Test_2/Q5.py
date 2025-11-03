#5. A man goes for shopping. He buys 5 products. Accept the price of all products and display
#the total bill after adding 18% GST

p1=int(input("Enter the p1 price : "))
p2=int(input("Enter the p2 price : "))
p3=int(input("Enter the p3 price : "))
p4=int(input("Enter the p4 price : "))
p5=int(input("Enter the p5 price : "))
shoping=input("you are shoping")
if(shoping=="yes"):
    c=p1+p2+p3+p4+p5
    print(c)
    price=0.18*c
    price1=price+c
    print(price1)