# alert message

l = ["harry", "priyanka", "kartik", "khushi", "parul", "roshni"]

name =input("Enter your name :")

if ( name in l):
    print("you are allowed to enter in this room")
    print("Welcome", name)
else:
    print("you are not allowed to enter in this room")
    print("please! get out from here")
    print("Alert: Unauthorized access attempt by", name)