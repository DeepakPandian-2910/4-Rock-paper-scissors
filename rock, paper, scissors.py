import random
game = ["rock", "paper", "scissors"]
choose = int(input("What do you choose. type '0' for rock, '1' for paper, '2' for scissors: \n"))
if choose>=3 or choose<0:
    print("Incorrect entry.")
else:
    print(f"You chose:\n{game[choose]}")
    computer = random.randint(0,2)
    print(f"Computer chose:\n{game[computer]}")
    if choose == 0:
        if computer == 0:
            print("its draw")
        elif computer == 1:
            print("You lost")
        else:
            print("You won")
    elif choose == 1:
        if computer == 0:
            print("You won")
        elif computer == 1:
            print("its draw")
        else:
            print("You lost")
    else:
        if computer == 0:
            print("You lost")
        elif computer == 1:
            print("You won")
        else:
            print("its draw")
