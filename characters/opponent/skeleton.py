from characters.basic_character import BasicCharacter
from random import randint


class Skeleton(BasicCharacter):
    def __init__(self) -> None:
        super().__init__()
        self.basic_attack = randint(10, 15)
        self._max_hp = 70
        self._hp = 70
        self._max_mana = 45
        self._mana = 35

    def faight(self):
        print("==" * 10)
        print("--------- Watch out for skeletons !!! ---------")
        super().print_basic_statistic()
        return self.basic_attack

    def drop(self):
        return randint(20, 40)
