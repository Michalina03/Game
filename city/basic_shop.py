class BasicShop:

    def __init__(self) -> None:
        self.add_health = 25
        self.add_mana = 50

    def choose_modification(self, character):
        while True:
            try:
                print(f"a \t Add health ? {self.add_health}")
                print(f"b \t Add mana ? {self.add_mana}")
                print(f"d \t Add mana potion ")
                print(f"e \t Add health potion ")
                print(f"x \t Quit the shop")
                inp = input().lower()
                if inp == "a" and character._gold > 100:
                    character._gold -= 100
                    character._max_hp += self.add_health

                elif inp == "b" and character._gold > 100:
                    character._gold -= 100
                    character._max_mana += self.add_mana
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
