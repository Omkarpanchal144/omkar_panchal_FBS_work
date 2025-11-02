# convert distance eform feet and inches to metres and cm 

feet = float(input("Enter distance in feet: "))
inches = float(input("Enter distance in inches: "))

# Convert feet and inches to centimeters
total_inches = (feet * 12) + inches
centimeters = total_inches * 2.54
meters = centimeters / 100

print("Distance in meters:", meters)
print("Distance in centimeters:",centimeters)