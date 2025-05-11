def weryfikuj_pesel(pesel: str) -> int:
    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    suma = sum(int(pesel[i]) * wagi[i] for i in range(10))
    kontrolna = (10 - (suma % 10)) % 10
    return 1 if kontrolna == int(pesel[10]) else 0


if __name__ == "__main__":
    pesel_input = input("Podaj numer PESEL: ")
    print(weryfikuj_pesel(pesel_input))
