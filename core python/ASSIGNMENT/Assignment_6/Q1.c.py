#Q1.c
#       1   
#     1   1   
#   1   2   1   
# 1   3   3   1

r = 4
for i in range(r):
    for j in range(r - i - 1):
        print(" ", end=" ")

    num = 1
    for j in range(i + 1):
        print(num, end="   ")
        num = num * (i - j) // (j + 1)

    print()

