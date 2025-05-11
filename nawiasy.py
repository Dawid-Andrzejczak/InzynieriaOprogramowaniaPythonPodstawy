def poprawne_nawiasy(tekst: str) -> bool:
    licznik = 0
    for znak in tekst:
        if znak == '(':
            licznik += 1
        elif znak == ')':
            licznik -= 1
            if licznik < 0:
                return False
    return licznik == 0


if __name__ == "__main__":
    tekst = input("Wprowadź tekst: ")
    print(poprawne_nawiasy(tekst))
