import random

candies=random.randint(1,200)

for i in range(200):
   #sprint(i)
   if i%5==2 and i%6==3 and i%7==2:
      print(i)
   else:
      continue
