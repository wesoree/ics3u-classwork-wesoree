while True:
    try:
        age=int(input('how old are you?'))
    except ValueError:
        print("invalid age, please try again")
        age = 1000
        break
    if age != 0:
        break
while age != 1000:
    if age >= 5:
        try:
            height=float(input('how tall are you?'))
        except ValueError:
            print("invalid height, please try again")
            break
        if height == 21:
            ans=input('you stupid, what\'s 9+10?')
            ans=int(ans)
            if ans == 21:
                print ('you stupid')
                break
            elif ans == 19:
                print("goodbye")
                break
        elif height >= 100:
            print("you can ride")
            break
        else:
            print("you cannot ride bc u too short")
            break
    else:
        print("you cannot ride bc underage")