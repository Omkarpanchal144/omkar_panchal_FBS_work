length=float(input("Enter the length = "))
breadth=float(input("Enter the breadth = "))
radius=float(input("Enter the radius = "))

# caclulate the perimeter
area=length*breadth
peri_rectangle=2*(length+breadth)

area_cir =3.14*radius*radius
peri_cir=2*3.14*radius

total_area=peri_rectangle+1/2*peri_cir

print("area of rectangle =",area)
print("perimeter =",peri_rectangle)
print("area of circle = ", area_cir)
print("perimeter =",peri_cir)

print("total aera =",total_area)
