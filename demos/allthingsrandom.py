import random
x = random.randrange(1,15)
while True:
    try:
        guess=int(input("pick a number from 1 - 15"))
        break
    except ValueError:
        print("invalid guess, please try again")
if x==guess:
    print("you guessed the number")
elif guess==21:
    try:
        ans=int(input('you stupid, what\'s 9+10'))
    except ValueError:
        print("invalid")
        ans = 19
    if ans==19:
        print("the number was ", +x)
    elif ans==21:
        print('you stupid, the number was ', +x)
    else:
        print("you are guessing randomly, the number was ", +x)
else:
    print("the number was ", +x)
