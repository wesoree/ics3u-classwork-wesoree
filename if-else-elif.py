name = input("what's your name")
print("hello, " + name)
age = input("how old are you?")
age = int(age)
if age <= 12:
    print('you can\'t use Discord')
    print("!ban " + name)
elif age == 13:
    print("you can use Discord")
elif age == 16:
    print("you can drive")
elif age == 18:
    print("you can vote")
elif age == 21:
    ans = input('you\'re stupid, what\'s 9+10?')
    ans = int(ans)
    if ans ==21:
        print("you're stupid")
    elif ans ==19:
        print("you can rent a car")
    else:
        print("!ban" + name)
    