import random
x = random.randrange(1,15)

while True:
    guess = input("pick number between 1 to 15")
    guess = int(guess)
    if guess == x:
        print ("guess is correct")
        break
    elif guess<1 or guess>15:
        print('invalid guess')
    else:
        print("please try again")

