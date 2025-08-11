# write a programme to find the greater of four numbers entered by the user

a = int(input("enter the first number :"))
b = int(input("enter trhe second number :"))
c = int(input("enter the third number :"))
d = int(input("enter the fourth number :"))

if(a>b) and (a>c) and (a>d):
    print("The greater number is :", a)
elif (b>a) and (b>c) and (b>d):
    print("the greater number is:", b)
elif(c>a) and (c>b) and (c>d):
    print("The greater number is :", c)
elif (d>a) and (d>b) and (d>c):
    print("The greater number is :",d)