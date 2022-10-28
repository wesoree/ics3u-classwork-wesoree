print("Welcome to my game!")

while True:
    # MENU OPTIONS
    print("Choose what game you want to play.")
    print("[1] Game One")
    print("[2] Game Two")

    # GET CHOICE
    choice = int(input("Choice: "))

    # HANDLE CHOICE
    if choice == 1: # GAME ONE
        print("Welcome to the clapping mini game.")
        print("Clap 5 times to win!")
        claps = 0
        while claps < 5:
            print(f"You have clapped {claps} times.")

            # menu options
            print("[1] Clap")

            # get choice
            choice = int(input("Choice: "))

            # handle choice
            if choice == 1:
                claps += 1
        
        print("YOU DID IT!!!!")
        print()
        input("press ENTER to continue")
    elif choice == 2: # game two
        print("You chose game TWO")