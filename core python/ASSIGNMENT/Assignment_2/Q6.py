# DA=Dearness Allowance
# TA=traveling allowance
# HRA =house rent Allowance

basic=float(input("Enter the salary ="))
da=0.10*basic
ta=0.12*basic
hra=0.15*basic

total_salary=basic+da+ta+hra
print("DA :",da)
print("TA :",ta)
print("HRA :",hra)
print("Total salary :",total_salary)