from characters.hero.mage import Mage
from characters.hero.warrior import Warrior
from characters.hero.ninja import Ninja
from characters.hero.hunter import Hunter
from characters.hero.monk import Monk
from characters.opponent.goblin import Goglin
from characters.opponent.skeleton import Skeleton
from characters.opponent.revenant import Revenant
from characters.opponent.witch import Witch
from characters.opponent.ghost import Ghost
from city.mage_shop import MageShop
from city.warrior_shop import WarriorShop
from city.ninja_shop import NinjaShop
from city.hunter_shop import HunterShop
from city.monk_shop import MonkShop
from game_events.boss import Boss
from mission.mission import maze_game
import os

# =======================================================================

selected_characters = ["Mage"]
unlocked_characters = {
    "Mage": True,
    "Warrior": False,
    "Ninja": False,
    "Hunter": False,
    "Monk": False,
}


def one_on_one_fight(hero: Mage | Warrior | Ninja | Hunter | Monk, enemy):
    if enemy == "a":
        opponent = Goglin()
    elif enemy == "b":
        opponent = Skeleton()
    elif enemy == "c":
        opponent = Revenant()
    elif enemy == "d":
        opponent = Witch()
    elif enemy == "e":
        opponent = Ghost()
    elif enemy == "h":
        opponent = Boss()
    opponent.regeneration()
    hero.regeneration()
    while hero.is_alive() and opponent.is_alive():
        os.system("cls" if os.name == "nt" else "clear")
        hero.reduce_hp(opponent.faight())
        opponent.reduce_hp(hero.faight())

    if not (hero.is_alive()):
        print("---- You gave your all today !!! ----")
        return None
    hero.add_gold(opponent.drop())


def chose_shop(my_hero):
    try:
        if isinstance(my_hero, Mage):
            shop = MageShop()
        elif isinstance(my_hero, Warrior):
            shop = WarriorShop()
        elif isinstance(my_hero, Ninja):
            shop = NinjaShop()
        elif isinstance(my_hero, Hunter):
            shop = HunterShop()
        elif isinstance(my_hero, Monk):
            shop = MonkShop()
        return shop
    except UnboundLocalError:
        print("--- Check korekt option ---")


def chose_class():
    print("=====  Select a Character Class  =====")
    if unlocked_characters["Mage"]:
        print(" a - mage ")
    if unlocked_characters["Warrior"]:
        print(" b - warrior")
    if unlocked_characters["Ninja"]:
        print(" c - ninja")
    if unlocked_characters["Hunter"]:
        print(" d - hunter")
    if unlocked_characters["Monk"]:
        print(" e - monk")

    inp = input().lower()
    try:
        if inp == "a" and unlocked_characters["Mage"]:
            my_hero = Mage()
        elif inp == "b" and unlocked_characters["Warrior"]:
            my_hero = Warrior()
        elif inp == "c" and unlocked_characters["Ninja"]:
            my_hero = Ninja()
        elif inp == "d" and unlocked_characters["Hunter"]:
            my_hero = Hunter()
        elif inp == "e" and unlocked_characters["Monk"]:
            my_hero = Monk()
        else:
            print("Character is not available or invalid option. Try again.")
            return chose_class()
        return my_hero
    except UnboundLocalError:
        print("--- Check correct option ---")
        return chose_class()


def unlock_character(my_hero):
    print("=====  Unlock a Character Class  =====")
    print(" b - warrior (500 gold)")
    print(" c - ninja (1000 gold)")
    print(" d - hunter (1500 gold)")
    print(" e - monk (2000 gold)")

    inp = input().lower()
    try:
        if inp == "b" and not unlocked_characters["Warrior"]:
            if my_hero._gold >= 500:
                my_hero._gold -= 500
                unlocked_characters["Warrior"] = True
                print("Warrior has been unlocked!")
            else:
                print("You don't have enough gold.")
        elif inp == "c" and not unlocked_characters["Ninja"]:
            if my_hero._gold >= 1000:
                my_hero._gold -= 1000
                unlocked_characters["Ninja"] = True
                print("Ninja has been unlocked!")
            else:
                print("You don't have enough gold.")
        elif inp == "d" and not unlocked_characters["Hunter"]:
            if my_hero._gold >= 1500:
                my_hero._gold -= 1500
                unlocked_characters["Hunter"] = True
                print("Hunter has been unlocked!")
            else:
                print("You don't have enough gold.")
        elif inp == "e" and not unlocked_characters["Monk"]:
            if my_hero._gold >= 2000:
                my_hero._gold -= 2000
                unlocked_characters["Monk"] = True
                print("Monk has been unlocked!")
            else:
                print("You don't have enough gold.")
        else:
            print("Character is already unlocked or invalid option. Try again.")
    except UnboundLocalError:
        print("--- Check correct option ---")


def main_game():
    my_hero = chose_class()
    if my_hero is None:
        my_hero = chose_class()
    shop = chose_shop(my_hero)
    day = 1
    while my_hero.is_alive():
        os.system("cls" if os.name == "nt" else "clear")
        print(f"======================DAY: {day}============================")
        print(
            "a - go to the dark forest"
        )  # goblin: hp: 40 mana: 20 drop: 10-20 attack: 1-10
        print(
            "b - go to the dark castle"
        )  # skeletor: hp: 70 mana: 45 drop: 20-40 attack: 10-15
        print(
            "c - go to the dark cosmos"
        )  # revenant: hp: 120 mana: 80 drop: 40-100 attack: 15-20
        print(
            "d - go to the dark caves"
        )  # witch: hp: 150 mana: 100 drop: 100-200 attack: 20-40
        print(
            "e - go to the haunted house"
        )  # ghost: hp: 200 mana: 160 drop: 200-400 attack: 40-100
        print("f - city")
        print("g - choose a new hero")
        print("h - BOSS !!! ")
        print("i - mission")
        print("r - rest")
        print("x - exit")
        my_hero.inf()
        print("==" * 20)

        inp = input().lower()
        if (
            "a" == inp
            or "b" == inp
            or "c" == inp
            or "d" == inp
            or "e" == inp
            or "h" == inp
        ):
            one_on_one_fight(my_hero, inp)
        elif "f" == inp:
            print("a - buy spells, hp, mana and potion")
            print("b - buy a new hero !!!!")
            inp2 = input().lower()
            if inp2 == "a":
                shop.choose_modification(my_hero)
            elif inp2 == "b":
                unlock_character(my_hero)
        elif "r" == inp:
            my_hero.total_rest()
            day += 1
        elif "g" == inp:
            my_hero = chose_class()
            shop = chose_shop(my_hero)
        elif "i" == inp:
            maze_game(my_hero)
        elif "x" == inp:
            print("------ The program has ended ------")
            my_hero.is_alive = False
        else:
            print("--- There is no such command ---")


# =======================================================================


if __name__ == "__main__":
    print("")
    print(
        "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-  Welcome to Battle Masters.  -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
    )
    print(
        "|                                                                                                        |"
    )
    print(
        "|  Choose better and better but more expensive characters.                                               |"
    )
    print(
        "|  Explore worlds where dangerous goblins and difficult to defeat ghosts await you.                      |"
    )
    print(
        "|  Kill monsters, get gold and go to the city where you can improve your character and buy powers for it |"
    )
    print(
        "|  If your power value is True you can use it,                                                           |"
    )
    print(
        "|  if its value is False go to the city where you can buy it for a certain amount of gold.               |"
    )
    print(
        "|                                                                                                        |"
    )
    print(
        "-------------------------------------          Good luck !          --------------------------------------"
    )
    print("")
    main_game()
print("")
print("=-=-=-=-=-=- Thank you for playing !!! -=-=-=-=-=-=")
