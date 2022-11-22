while True:
    try:
        age=int(input('how old are you?'))
        break
    except ValueError:
        print("invalid age, please try again")
while True:
    if age >= 5:
        try:
            height=int(input('how tall are you?'))
            break
        except ValueError:
            print("invalid height, please try again")
    else:
        print('you are too young to ride')
        height = 0
        break
if height == 21:
    ans=input('you stupid, what\'s 9+10?')
    ans=int(ans)
    if ans == 21:
        print ('you stupid')
    elif ans == 19:
        print("you are too short to ride")
elif height >= 100:
    print("you can ride")
elif height < 100 and height != 0:
    print("you are too short to ride")