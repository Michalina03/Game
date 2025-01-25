from characters.basic_character import BasicCharacter
from random import randint


class Witch(BasicCharacter):
    def __init__(self) -> None:
        super().__init__()
        self.basic_attack = randint(20, 40)
        self._max_hp = 150
        self._hp = 150
        self._max_mana = 100
        self._mana = 95

    def faight(self):
        print("==" * 10)
        print("--------- Watch out for witch !!! ---------")
        super().print_basic_statistic()
        return self.basic_attack

    def drop(self):
        return randint(100, 200)
