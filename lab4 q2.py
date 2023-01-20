y=int(input("ENTER THE YEAR "))
if y%4==0:
    print("you have enter the leap year")
if y%400==0:
    print("you enter the leap year")
elif y%100==0:
    print("not a leap year")
else:
    print("not a leap yeaer")
