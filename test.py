import random
x=random.randint(-2000,2000)
y=random.randint(-2000,2000)

if x>-960 and x<960 and y<-540 and y>540:
    print("point on screen")
else:
    print("point not on screen")
