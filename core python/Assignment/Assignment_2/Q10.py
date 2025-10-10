number = int(input(" Enter the three  digit number ="))

rev =(number%10)*100+((number//10)%10)*10+(number//100)

print("Reversed number =",rev)