from random import randint
import random


class HunterKit:

    def __init__(self) -> None:
        self._unlocked_stealth_mastery = True
        self._unlocked_deadly_accuracy = False
        self._unlocked_shadow_camouflage = False

    def stealth_mastery(self, character):
        if character._mana >= 200:
            character._mana -= 200
            return 60
        else:
            print("There wasn't enough mana to complete the power")
            return 0

    def deadly_accuracy(self, character):
        if character._mana >= 100:
            character._mana -= 100
            return 70
        else:
            print("There wasn't enough mana to complete the power")
            return 0

    def shadow_camouflage(self, chatacter):
        atac = 0
        for i in range(chatacter._mana):
            atac = i * 4
        chatacter._mana = 0
        return atac

    def choose_spell(self, character):
        while True:
            try:
                print(
                    f"a \t Stealth mastery available? {self._unlocked_stealth_mastery}"
                )
                print(
                    f"b \t Deadly accuracy available? {self._unlocked_deadly_accuracy}"
                )
                print(
                    f"c \t Shadow camouflage available? {self._unlocked_shadow_camouflage}"
                )
                print(f"e \t Close the kit")
                inp = input().lower()
                if inp == "a" and self._unlocked_stealth_mastery:
                    return self.stealth_mastery(character)
                elif inp == "b" and self._unlocked_deadly_accuracy:
                    return self.deadly_accuracy(character)
                elif inp == "c" and self._unlocked_shadow_camouflage:
                    return self.shadow_camouflage(character)
                elif inp == "e":
                    print("Close the kit")
                    return 0
                else:
                    print("This power has not been unlocked yet or does not exist.")
            except Exception as e:
                print(f"An error occurred: {e}")

    def unlock_spells(self, character):
        while True:
            try:
                print(
                    f"a) free spell! \t Stealth mastery available? | - 200 mana | you deal - 60 hp | {self._unlocked_stealth_mastery}"
                )
                print(
                    f"b) -900 gold \t Deadly accuracy available? | - 100 mana | you deal - 70 hp | {self._unlocked_deadly_accuracy}"
                )
                print(
                    f"c) -1500 gold \t Shadow camouflage available? | all mana | you deal  - 4*mana hp  | {self._unlocked_shadow_camouflage}"
                )
                print(f"e \t Close the kit")
                inp = input().lower()
                if (
                    inp == "a"
                    and not self._unlocked_stealth_mastery
                    and character._gold >= 1000
                ):
                    self._unlocked_stealth_mastery = True
                elif (
                    inp == "b"
                    and not self._unlocked_deadly_accuracy
                    and character._gold >= 900
                ):
                    character._gold -= 900
                    self._unlocked_deadly_accuracy = True
                elif (
                    inp == "c"
                    and not self._unlocked_shadow_camouflage
                    and character._gold >= 1500
                ):
                    character._gold -= 1500
                    self._unlocked_shadow_camouflage = True
                elif inp == "e":
                    print("You don't have enough gold")
                    break
                else:
                    if inp in ["a", "b", "c"]:
                        print("Not enough gold or you know this power.")
                    else:
                        print("This option do not exist.")
            except Exception as e:
                print(f"An error occurred: {e}")
