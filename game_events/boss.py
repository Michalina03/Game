from characters.basic_character import BasicCharacter
from random import randint


class Boss(BasicCharacter):
    def __init__(self) -> None:
        super().__init__()
        self.basic_attack = randint(40, 50)
        self._max_hp = 100000
        self._hp = 100000
        self._max_mana = 100000
        self._mana = 100000

    def faight(self):
        print("==" * 10)
        print("--------- Watch out for BOSS !!! ---------")
        super().print_basic_statistic()
        return self.basic_attack

    def drop(self):
        return randint(10000, 200000)
