subject1=int(input("Enter mark of subject 1:"))
subject2=int(input("Enter mark of subject 2:"))
subject3=int(input("Enter mark of subject 3:"))
subject4=int(input("Enter mark of subject 4:"))
subject5=int(input("Enter mark of subject 5:"))

total_mark=subject1+subject2+subject3+subject4+subject5
percentage=(total_mark/500)*100
print("total mark=",total_mark,"/500")
print("percentage =",percentage,"%")