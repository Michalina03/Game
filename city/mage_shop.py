from city.basic_shop import BasicShop
from characters.elemental_magic_book import elemental_magic_book


class MageShop(BasicShop):

    def __init__(self) -> None:
        super().__init__()

    def choose_modification(self, character):
        while True:
            try:
                print(f"a \t Add health ? | - 40 gold | + {self.add_health} hp")
                print(f"b \t Add mana ? | - 30 gold | + {self.add_mana} mana")
                print(f"c \t Add spell")
                print(f"d \t Add mana potion | - 200 gold | + 100 hp | ")
                print(f"e \t Add health potion | - 200 gold | + 100 hp |")
                print(f"x \t Quit the shop")
                inp = input().lower()
                if inp == "a" and character._gold > 40:
                    character._gold -= 40
                    character._max_hp += self.add_health

                elif inp == "b" and character._gold > 30:
                    character._gold -= 30
                    character._max_mana += self.add_mana
                elif inp == "c":
                    character._spell_book.unlock_spells(character)
                elif inp == "d" and character._gold > 200:
                    character._gold -= 200
                    character._mana_potion += 1
                elif inp == "e" and character._gold > 200:
                    character._gold -= 200
                    character._health_potion += 1
                elif inp == "x":
                    print("--- Quit the shop ---")
                    break
                else:
                    print("--- Not enough gold ---")
            except Exception as e:
                print(f"An error occurred: {e}")
