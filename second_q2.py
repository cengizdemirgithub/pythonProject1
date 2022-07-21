import random


def neu():
    for i in range(1, 100):
        random_zahl = int(input("Geben Sie ein random Zahl ein: "))
        random_computer=random.randint(1,100)

        print(random_computer)
    if random_computer == random_zahl:
        print("du bist gewinner")
    elif random_computer > random_zahl:
        print("gib gröser zahl")
    elif random_computer < random_zahl:
        print("gib kleiner zahl ")
    else:
        print("ungültig input probier mal")
neu()