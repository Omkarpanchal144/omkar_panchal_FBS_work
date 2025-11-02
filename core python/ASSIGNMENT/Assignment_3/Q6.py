#6. Write a program to calculate profit or loss. 

cp=float(input("Enter the cost  prices  ="))
sp=float(input("Enter the selling prices ="))

if(sp > cp):
    profit=sp-cp
    print("profit =",profit)
elif(cp > sp):
    loss=cp-sp
    print("loss =",loss)
else:
    print("not a profit and loss")
