import random
x = random.randrange(1,15)
guess=input("pick a number from 1 - 15")
guess=int(guess)

if x==guess:
    print("you guessed the number")
elif guess==21:
    ans=input('you stupid, what\'s 9+10')
    ans=int(ans)
    if ans==19:
        print("the number was ", +x)
    elif ans==21:
        print('you stupid, the number was ', +x)
    else:
        print("you are guessing randomly, the number was ", +x)
else:
    print("the number was ", +x)
