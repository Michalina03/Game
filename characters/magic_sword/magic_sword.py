from random import randint
import random


class MagicSword:

    def __init__(self) -> None:
        self._unlocked_astral_slash = True
        self._unlocked_shield_bash = False
        self._unlocked_battle_fury = False

    def astral_slash(self, character):
        if character._mana >= 70:
            character._mana -= 70
            return 30
        else:
            print("There wasn't enough mana to complete the attack")
            return 0

    def shield_bash(self, character):
        if character._mana >= 40:
            character._mana -= 40
            base_damage = 40
            shield_damage = 5
            shield_duration = 4
            print(
                f"Shield bash deals {base_damage} damage and poisons the enemy for {shield_damage} damage over {shield_duration} turns."
            )
            return base_damage
        else:
            print("There wasn't enough mana to complete the attack")
            return

    def battle_fury(self, character):
        if character._mana >= 90:
            character._mana -= 90
            base_damage = random.randint(50, 100)
            fury_damage = base_damage // 2
            print(
                f"Battle fury deals {base_damage} damage to the main target and {fury_damage} splash damage to nearby enemies."
            )
            return base_damage
        else:
            print("There wasn't enough mana to complete the attack")
            return 0

    def choose_spels(self, character):
        while True:
            try:
                print(f"a) \t Astral slash available? {self._unlocked_astral_slash}")
                print(f"b) \t Shield bash available? {self._unlocked_shield_bash}")
                print(f"c) \t Battle fury available? {self._unlocked_battle_fury}")
                print(f"e \t Close the sword")
                inp = input().lower()
                if inp == "a" and self._unlocked_astral_slash:
                    return self.astral_slash(character)
                elif inp == "b" and self._unlocked_shield_bash:
                    return self.shield_bash(character)
                elif inp == "c" and self._unlocked_battle_fury:
                    return self.battle_fury(character)
                elif inp == "e":
                    print("Close the sword")
                    return 0
                else:
                    print("This attack has not been unlocked yet or does not exist.")
            except Exception as e:
                print(f"An error occurred: {e}")

    def unlock_spells(self, character):
        while True:
            try:
                print(
                    f"a) free spell! \t Astral slash available? | - 70 mana | you deal - 30 hp | {self._unlocked_astral_slash}"
                )
                print(
                    f"b) -350 gold \t Shield bash available? | - 40 mana | you deal - 40 hp + poison | {self._unlocked_shield_bash}"
                )
                print(
                    f"c) -500 gold \t Battle fury available? | - 90 mana | you deal - 50 to - 100 hp + splash | {self._unlocked_battle_fury}"
                )
                print(f"e \t Close the sword")
                inp = input().lower()
                if (
                    inp == "a"
                    and not self._unlocked_astral_slash
                    and character._gold >= 300
                ):

                    self._unlocked_astral_slash = True
                elif (
                    inp == "b"
                    and not self._unlocked_shield_bash
                    and character._gold >= 350
                ):
                    character._gold -= 350
                    self._unlocked_shield_bash = True
                elif (
                    inp == "c"
                    and not self._unlocked_battle_fury
                    and character._gold >= 500
                ):
                    character._gold -= 500
                    self._unlocked_battle_fury = True
                elif inp == "e":
                    print("You don't have enough gold")
                    break
                else:
                    if inp in ["a", "b", "c"]:
                        print("Not enough gold or you know this attack.")
                    else:
                        print("This option do not exist.")
            except Exception as e:
                print(f"An error occurred: {e}")
