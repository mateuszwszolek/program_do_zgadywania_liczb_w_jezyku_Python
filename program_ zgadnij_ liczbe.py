# program zgadnij liczbę

from random import randint

liczba_wylosowana = randint (1, 50)
liczba_uzytkownika = -1
ilosc_prob = 0

nazwa = input ("Podaj nazwe: ")
print("Cześć " + nazwa + " znajdź liczbę o jaką chodzi z przedziału 1 do 50")

while  liczba_uzytkownika != liczba_wylosowana:
    ilosc_prob += 1
    liczba_uzytkownika = int(input("Podaj liczbę od 1 do 50: "))

    if liczba_uzytkownika > liczba_wylosowana:
        print("Niestety, wylosowana liczba jest mniejsza")

    elif liczba_uzytkownika < liczba_wylosowana:
        print("Niestety, wylosowana liczba jest większa")

print("Tak to ta liczba. Gratulacje. Odgadłeś za", ilosc_prob, "próbą. ")
