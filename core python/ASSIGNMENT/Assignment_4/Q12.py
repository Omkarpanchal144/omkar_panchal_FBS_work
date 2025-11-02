#12. WAP to print Armstrong number within a given range

lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))
print("Armstrong numbers between", lower, "and", upper, "are:")
for i in range(lower, upper + 1):
    digits = str(i)
    power = len(digits)
    sum_pow = 0
    for j in digits:
        sum_pow += int(j) ** power

    if sum_pow == i:
        print(i)
