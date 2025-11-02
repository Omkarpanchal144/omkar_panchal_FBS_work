#. Accept age of five people and also per person ticket amount and then calculate total 
# amount to ticket to travel for all of them based on following condition : 
#a. Children below 12 = 30% discount 
#b. Senior citizen (above 59) = 50% discount 
#c. Others need to pay full. 

ticket_price = float(input("Enter ticket price per person: "))

total_amount = 0

# Person 1
age1 = int(input("Enter age of person 1: "))
if age1 < 12:
    final_price = ticket_price - (0.30 * ticket_price)
elif age1 > 59:
    final_price = ticket_price - (0.50 * ticket_price)
else:
    final_price = ticket_price
total_amount += final_price

# Person 2
age2 = int(input("Enter age of person 2: "))
if age2 < 12:
    final_price = ticket_price - (0.30 * ticket_price)
elif age2 > 59:
    final_price = ticket_price - (0.50 * ticket_price)
else:
    final_price = ticket_price
total_amount += final_price

# Person 3
age3 = int(input("Enter age of person 3: "))
if age3 < 12:
    final_price = ticket_price - (0.30 * ticket_price)
elif age3 > 59:
    final_price = ticket_price - (0.50 * ticket_price)
else:
    final_price = ticket_price
total_amount += final_price

# Person 4
age4 = int(input("Enter age of person 4: "))
if age4 < 12:
    final_price = ticket_price - (0.30 * ticket_price)
elif age4 > 59:
    final_price = ticket_price - (0.50 * ticket_price)
else:
    final_price = ticket_price
total_amount += final_price

# Person 5
age5 = int(input("Enter age of person 5: "))
if age5 < 12:
    final_price = ticket_price - (0.30 * ticket_price)
elif age5 > 59:
    final_price = ticket_price - (0.50 * ticket_price)
else:
    final_price = ticket_price
total_amount += final_price

print("\nTotal amount to pay for all 5 people =", total_amount)
