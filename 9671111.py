age=input('how old are you?')
age=int(age)

if age >= 5:
    height=input('how tall are you?')
    height=int(height)
    if height == 21:
        ans=input('you stupid, what\'s 9+10?')
        ans=int(ans)
        if ans == 21:
            print ('you stupid')
        elif ans == 19:
            print("goodbye")
    elif height >= 100:
        print("you can ride")
    else:
        print("you cannot ride")
else:
    print("you cannot ride")