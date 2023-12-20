import random
from random import randint, choice

resources = 200
life = 100
arrow = 10

# ---------------------------------------------


def get_user_choice():
    print("Wybierz: kamień, papier, czy nożyce?")
    user_choice = input().lower()
    while user_choice not in ["kamień", "papier", "nożyce"]:
        print("Nieprawidłowy wybór. Spróbuj ponownie: kamień, papier, czy nożyce?")
        user_choice = input().lower()
    return user_choice


def get_computer_choice():
    return random.choice(["kamień", "papier", "nożyce"])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Remis!"
    elif (
        (user_choice == "kamień" and computer_choice == "nożyce")
        or (user_choice == "papier" and computer_choice == "kamień")
        or (user_choice == "nożyce" and computer_choice == "papier")
    ):
        return "Gratulacje! Wygrałeś! Możesz iść dalej"
    else:
        print("Przegrałeś, koniec gry")
        exit()


# ---------------------------------------------


def zwykly_atak():
    return randint(5, 10)


def fire_ball():
    global resources
    if resources < 10:
        print("-" * 40)
        print("Nie masz wystarczającej ilości resources!")
        return 0
    resources -= 5
    return randint(13, 25)


def wybierz_atak():
    print("a/A - Wykonaj Normalny Atak")
    print("b/B - Fire ball!")
    co = input().upper()
    if co == "A":
        return zwykly_atak()
    elif co == "B":
        return fire_ball()
    else:
        print("Nie wybrano akcji")
        return 0


def random_oponent():
    opponents = [["Jadowita kobra", 12, 5, 0], ["Szkielet", 8, 5, 0]]
    return choice(opponents)


# --------------------------------


def magiczny_atak():
    global resources
    if resources < 10:
        print("-" * 40)
        print("Nie masz wystarczającej ilości resources!")
        return
    resources -= 5
    return randint(13, 14)


def bow_szot():
    global arrow
    if arrow < 1:
        print("-" * 40)
        print("Nie masz wystarczającej ilości arrow!")
        return 0
    arrow -= 1
    return randint(19, 22)


def wybierz_atak_2():
    print("a/A - magiczny atak")
    print("b/B - bow_szot")
    co = input().upper()
    if co == "A":
        return magiczny_atak()
    elif co == "B":
        return bow_szot()
    else:
        print("Nie wybrano akcji")
        return 0


def random_oponent_2():
    opponents_2 = [["Smok", 17, 5, 10], ["Wiedzma", 15, 19, 5]]
    return choice(opponents_2)


# -----------------------------------


def wybierz_slowo():
    slowa = ["python", "wisielec", "programowanie", "projekt"]
    return random.choice(slowa)


def rysuj_wisielca(bledy):
    if bledy == 0:
        print(" -----\n |   |\n |\n |\n |\n |\n-+-")
    elif bledy == 1:
        print(" -----\n |   |\n |   O\n |\n |\n |\n-+-")
    elif bledy == 2:
        print(" -----\n |   |\n |   O\n |   |\n |\n |\n-+-")
    elif bledy == 3:
        print(" -----\n |   |\n |   O\n |  /|\n |\n |\n-+-")
    elif bledy == 4:
        print(" -----\n |   |\n |   O\n |  /|\\\n |\n |\n-+-")
    elif bledy == 5:
        print(" -----\n |   |\n |   O\n |  /|\\\n |  /\n |\n-+-")
    else:
        print(" -----\n |   |\n |   O\n |  /|\\\n |  / \\\n |\n-+-")


def ukryj_slowo(slowo, odgadniete_litery):
    ukryte_slowo = ""
    for litera in slowo:
        if litera in odgadniete_litery:
            ukryte_slowo += litera
        else:
            ukryte_slowo += "_"
    return ukryte_slowo
