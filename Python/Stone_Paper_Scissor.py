import random


def checkwin(player, comp):
    if comp == player:
        print("Tie")
    elif comp == "s":
        if player == "w":
            print("You Lose")
        elif player == "g":
            print("You Win")
    elif comp == "w":
        if player == "g":
            print("You Lose")
        elif player == "s":
            print("You Win")
    elif comp == "g":
        if player == "s":
            print("You Lose")
        elif player == "w":
            print("You Win")


a = random.choice(["s", "w", "g"])
player = input("Enter Snake(s),Water(w) and Gun(g)")
print(f"player's choice :{player}")
print(f"Computer's choice :{a}")
checkwin(player, a)
