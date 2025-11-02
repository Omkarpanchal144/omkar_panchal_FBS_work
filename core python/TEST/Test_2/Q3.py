#Q3. A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing
#for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle
#length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total
#cost of fencing the field.


circle_redius=20
#rectangle
m=50
b=40
wire_5_time=5
cost=35

circular=2*3.14*circle_redius

c=circular/2

print("circular",c)

rectangle=2*(m+b)
print("rectangle : ",rectangle)

d=rectangle+c
print("rectangle and circular : ",d)
e=d*5
f=e*35
print("total price is ",f)
