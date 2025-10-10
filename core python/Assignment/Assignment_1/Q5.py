P=float(input("Enter the principle amount ="))
T=float(input("Enter the time of year ="))
R=float(input("Enter the rate of interest ="))

# Compound interest
final_amount=P*(1+R/100)**T
CI=final_amount-P
print("final amount =",final_amount)
print("compound interest =",CI)