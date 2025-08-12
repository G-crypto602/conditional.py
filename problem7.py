# This programme will work on only in that string which is enter in this programme


post = input("Enter your post: ")

if("kartik" in post):
    print("kartik is mentioned in this post")
else:
    print("kartik is not mentioned in this post")



    # This programe is work on all type of strings.
    #  (uppercase, lowercase, titlecase)

post = input("Enter your post: ")

if("kartik".lower() in post.lower()):
    print("kartik is mentioned in this post")
else:
    print("kartik is not mentioned in this post")
