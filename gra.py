from game.defgry import (
    get_user_choice,
    get_computer_choice,
    determine_winner,
    wybierz_atak,
    random_oponent,
    wybierz_atak_2,
    random_oponent_2,
    fire_ball,
    zwykly_atak,
    bow_szot,
    magiczny_atak,
    wybierz_slowo,
    rysuj_wisielca,
    ukryj_slowo,
    arrow,
    life,
    resources,
)
import random

name = input("Podaj imie twojego bohatera: ")
print("-" * 40)
print(
    f"{name} pewnego dnia postanowiłeś odwiedzić miejscowość towich przodków. Wiedzma którą tu spotkałeś powiedziała Ci o ukrytym przez Twoich przodków skarbie. Postanowiłes go odnaleść i nagle znajdujesz się w tajemniczym tunelu ukrytym pod miastem"
)
# -----------------------------------------
print("-" * 40)
print(
    f"{name} W oddali zauważasz drzwi, idziesz w ich strone. Aby przedostać sie dalej musisz wpisać właściwą cyfre. Uważaj za każdą nie udaną prube tracisz 5 HP!"
)


def gra_liczbowa():
    liczba_do_odgadniecia = random.randint(1, 10)  # Losujemy liczbę od 1 do 10
    liczba_prob = 0
    life = 100

    while life > 0:
        strzal = int(input("Podaj liczbę: "))
        liczba_prob += 1

        if strzal == liczba_do_odgadniecia:
            print(
                f"Brawo! Odgadłeś liczbę {liczba_do_odgadniecia} w {liczba_prob} próbach."
            )
            break
        elif strzal < liczba_do_odgadniecia:
            print("Za mało! Spróbuj ponownie.")
            life -= 5
            print(f"Pozostało Ci {life}HP")
        else:
            print("Za dużo! Spróbuj ponownie.")
            life -= 5
            print(f"Pozostało Ci {life}HP")
    if life == 0:
        print("Przegrałeś")


if __name__ == "__main__":
    gra_liczbowa()
# -----------------------------------------
print("-" * 40)
print(
    f"{name} za drzwiami widzisz goblina, siedzi on przy stole i zwraca sie do Ciebie tymi słowami: Jesli uda Ci sie mnie pokonać w grze papier, kamień, nozyce to przepuszcze Cię dalej, lecz jeśli nie zginiesz"
)


def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"Twój wybór: {user_choice}")
        print(f"Wybor komputera: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        print("Czy chcesz zagrać ponownie? (tak/ nie ide dalej)")
        play_again = input().lower()
        if play_again != "tak":
            break


play_game()

# -----------------------------------------
print("-" * 40)
print(f"{name} idziesz dalej tunelem ale, uwaga zbliżają sie potwory !")

liczba_pokonanych_przeciwników = 0

while life > 50:
    opponent = random_oponent()

    while opponent[1] > 0 and life > 0:
        print(f"{name} walczy teraz z {opponent[0]}")
        print(f"Przeciwnik ma {opponent[1]} HP i zadaje Ci {opponent[2]} obrażeń")

        life -= opponent[2]
        if life <= 0:
            break

        print(f"Masz {life} HP i {resources} resources")
        atak = wybierz_atak()
        opponent[1] -= atak
        print(f"Zadałeś {atak} obrażeń")

    if opponent[1] <= 0:
        print("Zabiłeś przeciwnika!!!")
        liczba_pokonanych_przeciwników += 1
print(f"Brawo pokonałeś wszystkich {liczba_pokonanych_przeciwników} przeciwników")

# -----------------------------------------
print("-" * 40)
print("Wchodzisz na wyższy poziom! Teraz walcz z przeciwnikami 2 poziomu")

liczba_pokonanych_przeciwników_2 = 0

while life > 20:
    opponent_2 = random_oponent_2()

    while opponent_2[1] > 0 and life > 0:
        print(f"{name} walczy teraz z {opponent_2[0]}")
        print(f"Przeciwnik ma {opponent_2[1]} HP i zadaje Ci {opponent_2[2]} obrażeń")

        life -= opponent_2[2]
        if life <= 0:
            break

        print(f"Masz {life} HP i {resources} resources")
        atak_2 = wybierz_atak_2()
        opponent_2[1] -= atak_2
        print(f"Zadałeś {atak_2} obrażeń")

    if opponent_2[1] <= 0:
        print("Zabiłeś przeciwnika!!!")
        liczba_pokonanych_przeciwników_2 += 1

print(f"Brawo pokonałeś wszystkich {liczba_pokonanych_przeciwników_2} przeciwników")

# -------------------------------------
print("-" * 40)
print(f"{name} straciłeś dużo HP, ale masz szanse to nadrobić !")


def main():
    slowo = wybierz_slowo()
    odgadniete_litery = []
    bledy = 0
    lifee = life

    print("Witaj w grze Wisielec!")

    while True:
        rysuj_wisielca(bledy)

        ukryte = ukryj_slowo(slowo, odgadniete_litery)
        print("Odgadłeś już litery: ", ", ".join(odgadniete_litery))
        print("Słowo: ", ukryte)

        if ukryte == slowo:
            print("Gratulacje! Odgadłeś słowo: ", slowo)
            lifee += 50
            break

        if bledy == 6:
            print("Przegrałeś! Wisielec został ukończony. Prawidłowe słowo to: ", slowo)
            break

        guess = input("Podaj literę: ").lower()

        if guess in odgadniete_litery:
            print("Już odgadłeś tę literę. Spróbuj ponownie.")
            continue

        odgadniete_litery.append(guess)

        if guess not in slowo:
            bledy += 1


if __name__ == "__main__":
    main()

# -------------------------------------
print("-" * 40)
print(f"{name} przed tobą już ostatnie wyzwanie")
print(
    " W tej grze twoim zadaniem bedzie odnalezienie jak największej ilości wyrazow w danym wyrazie"
)
while True:
    print("tulipan")
    wyraz = input("Podaj wyraz: ")

    if wyraz == "pan":
        print("Brawo! Odgadłeś słowo.")
    elif wyraz == "lipa":
        print("Brawo! Odgadłeś słowo.")
    elif wyraz == "ul":
        print("Brawo! Odgadłeś słowo.")
    elif wyraz == "tu":
        print("Brawo! Odgadłeś słowo.")
    elif wyraz == "to wszystko":
        print(
            "Brawo! Odgadłeś wszystkie słowa !!! Wygrałeś gre, odnalazłeś SKARB oto on: UMIESZ PROGRAMOWAĆ :)"
        )
    else:
        print("Złe słowo.")
