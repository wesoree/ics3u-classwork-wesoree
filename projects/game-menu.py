import random

print("Welcome to Fix the Wiring!")
print()
print("In this game you will connect the wires to the ")

# PLAY GAME THREE

while True:
    print("Playing game THREE")
    wirelist=[]
    for i in range(6):
        r=random.randrange(1,4)
        if r not in wirelist:
            wirelist.append(r)
    print("the faulty wires are")
    print(wirelist)
    print("the wire connectors are")
    print("1, 2, 3, 4")
    printed=1
    input()
    