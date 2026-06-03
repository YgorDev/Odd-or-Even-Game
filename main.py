# odd or even game
from math import radians
import random
from unittest import result

w = 0
while True:
    player = int(input("Choose one number: "))
    computer = random.randint(0, 10)
    resulta = player + computer
    typeOE = " "
    while typeOE not in "OE":
        typeOD = str(input("Odd Or Even:[O/E] ")).strip().upper()[0]
    print(f"You chose {player} and machine chose {computer} the result is {resulta}")
    print("It s Even" if resulta % 2 == 0 else "It s Odd")
    if typeOE == "E":
        if resulta % 2 == 0:
            print("You Win!!")
            w += 1
        else:
            print("You Lose...")
            break
    elif typeOE == "O":
        if resulta % 2 == 1:
            print("You Win!!")
            w += 1
        else:
            print("You Lose...")
            break
    print("Lets play again...")
print(f"Game Over! You Won {w} times!! ")
