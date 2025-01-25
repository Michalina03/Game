from characters.basic_character import BasicCharacter
from characters.magic_sword.magic_sword import MagicSword


class Warrior(BasicCharacter):
    def __init__(self) -> None:
        super().__init__()
        self._basic_attack += 10
        self._max_hp = 125
        self._hp = 125
        self._hp_regeneration = 1
        self._max_mana = 700
        self._mana = 700
        self._mana_regeneration = 5
        self._health_potion = 0
        self._mana_potion = 0
        # --------------------------
        self._spell_book = MagicSword()
        self._equipment = []

    def inf(self):
        print("===" * 10)
        print("Your character")
        print(f"max_hp: {self._max_hp} \t max_mana: {self._max_mana}")
        print(f"hp: {self._hp} \t mana: {self._mana}")
        print(f"GOLD:  {self._gold}")
        print("===" * 10)

    def use_health_potion(self):
        if self._health_potion > 0:
            self._health_potion -= 1
            self._hp += 100
        else:
            print("You don't have health potion")

    def use_mana_potion(self):
        if self._mana_potion > 0:
            self._mana_potion -= 1
            self._mana += 200
        else:
            print("You don't have mana potion")

    def faight(self):
        while True:
            self.inf()
            print("a - basic_attack ( - 10 hp )")
            print("b - open MagicSword")
            print("c - use mana potion")
            print("d - use health potion")
            damage = 0

            inp = input().lower()

            if inp == "c":
                self.use_mana_potion()
            elif inp == "d":
                self.use_health_potion()
            if inp == "a":
                damage = self._basic_attack
            elif inp == "b":
                damage = self._spell_book.choose_spels(self)

            else:
                print("--- There is no such attack ---")

            return damage
