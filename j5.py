import random
r=random.randint(1,5)
b=1
m=0
while(b<=5):
    y=int(input("guess the Number"))
    if(y==r):
        print("you have gussed is right")
        m=m+1
        break
    elif(y>r):
        print("the actual number is smaller")
        b=b+1
    elif(y<r):
        print("the actual number is greater")
        b=b+1
if(m==0):
    print("your chance got over")
    print("failed")
if(m==1):
    print("you success guessed")
