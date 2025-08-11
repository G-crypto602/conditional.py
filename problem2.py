marks1 = int(input("enter your marks :"))
marks2 = int(input("enter your marks :"))
marks3 = int(input("enter your marks :"))
marks4 = int(input("enter your marks :"))

# check for total percentage
total_percentage = (100*(marks1 + marks2 + marks3)/300)

if (total_percentage >=40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
    print("You passed",total_percentage, '%')
else:
    print("You failed",total_percentage, '%')
