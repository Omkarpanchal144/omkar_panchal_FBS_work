# calculate cost  of paint the buildig wall (both interior And exterior) , you need area of one wall 
# total walls to paint = 8-1=7

# area in sq.m

area=float(input("Enter the area of one wall : "))
interior=float(input("Enter interior wall cost:"))
exterior=float(input("Enter the exterior wall cost:"))

total_walls=7
int_walls=5
ext_walls=2

total_int_area=int_walls*area
total_ext_area=ext_walls*area

# calculate the cost of wall
total_cost=(total_int_area*interior)+(total_ext_area*exterior)
print("Total interior painting cost =",total_int_area*interior)
print("Total exterior painting cost =",total_ext_area*exterior)
print("Total painting cost =",total_cost)