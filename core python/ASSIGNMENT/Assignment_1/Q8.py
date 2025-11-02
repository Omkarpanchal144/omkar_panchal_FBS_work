days=int(input("Enter the Number of day ="))

# caculate year ,week,days
years=days // 365
remaiing_day=days % 365
weeks=remaiing_day // 7
day_left=remaiing_day % 7

print("year=",years)
print("weeks=",weeks)
print("days=",day_left)
