mypoints = input("how many points")
mypoints = int(mypoints)

if mypoints == 21:
    ans = input('you\'re stupid, what\'s 9+10?')
    ans = float(ans)
    if ans == 19:
        print("ok")
    elif ans == 21:
        print("you're stupid")
    else:
        print("why")
else:
    print ("you have", mypoints, "points")