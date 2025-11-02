# 9. Input 5 subject marks from user and display grade(eg.First class,Second class ..) 

subject1=int(input("Enter mark of subject 1:"))
subject2=int(input("Enter mark of subject 2:"))
subject3=int(input("Enter mark of subject 3:"))
subject4=int(input("Enter mark of subject 4:"))
subject5=int(input("Enter mark of subject 5:"))

total_mark=subject1+subject2+subject3+subject4+subject5
print("total mark =",total_mark)
percentage=(total_mark/500)*100
print("percentage :-",percentage)

if(percentage>80):
    print("First class")
elif(percentage>60):
    print("Secound class")
elif(percentage>40):
    print("Third class")
else:
     print("student is fail")

