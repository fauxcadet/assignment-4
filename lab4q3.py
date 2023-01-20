import random

a=0
while a<11:
    a=a+1
    x,y=random.randint(1,10),random.randint(1,10)
    print("Question",a,":",x,"x",y )
    m=int(input("enter ur answer:-"))
    if m==x*y:
        print ("correct")
    else:
        print("wrong")
        
