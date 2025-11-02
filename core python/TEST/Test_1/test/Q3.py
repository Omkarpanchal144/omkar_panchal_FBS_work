# calculate total cost of painting 

length = float(input("Enter length of wall (in meters): "))
breadth = float(input("Enter breadth of wall (in meters): "))
height = float(input("Enter height of wall (in meters): "))
rate = float(input("Enter painting cost per square meter (Rs): "))

if length > 0 and breadth > 0 and height > 0 and rate > 0:
    area = 2 * height * (length + breadth)
    # Total cost of painting
    total_cost = area * rate

    print("Total cost of painting = Rs.",(total_cost))
else:
   print("Invalid input !")