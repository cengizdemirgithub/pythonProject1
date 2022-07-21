import random


def neu():
    for i in range(1, 100):
        random_zahl = int(input("Geben Sie ein random Zahl ein: "))
        random_computer = random.randint(1, 5)
        if random_computer == random_zahl:
            print("du bist gewinner")
            break

        elif random_computer > random_zahl:
            print("leider kleiner zahl")
        elif random_computer < random_zahl:
            print("leider gröser zahl ")
        else:
            print("ungültig input probier mal")


neu()
