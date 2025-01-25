from characters.basic_character import BasicCharacter
from random import randint


class Goglin(BasicCharacter):
    def __init__(self) -> None:
        super().__init__()
        self.basic_attack = randint(1, 10)
        self._max_hp = 40
        self._hp = 40
        self._max_mana = 20
        self._mana = 15

    def faight(self):
        print("==" * 10)
        print("--------- Watch out for goblin !!! ---------")
        super().print_basic_statistic()
        return self.basic_attack

    def drop(self):
        return randint(10, 20)
