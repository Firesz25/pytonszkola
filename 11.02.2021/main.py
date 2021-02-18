def czyjestreszta(a, b):
    reszta = a % b
    if reszta != 0:
        print("    reszta z dzielenia wynosi: ", reszta)
    elif reszta == 0:
        print("    liczby dzielą się bez reszty")
    else:
        print("    błąd")

def kalkulator(znak, a, b):
    if znak == '+':
        return a + b
    if znak == '-':
        return a - b
    if znak == '*':
        return a * b
    if znak == '/':
        return a / b
    else:
        print('podałeś niepoprawny znak')     

if __name__ == '__main__':
    print()
    a = int(input("    podaj pierwszą liczbe: "))
    b = int(input("    podaj drugą liczbe: "))
    co_robisz = int(input("""
    jaką czynność chcesz wykonać
    sprawdzenie czy jest reszta z dzielenia: 1
    użyć kalkulatora: 2\n
    """))
    if co_robisz == 1:
        czyjestreszta(a, b)
    elif co_robisz == 2:
        kalk = True
        while kalk:
            znak = input("     podaj znak ( +, -, *, / ): ")
            a = kalkulator(znak, a, b)
            print("    wynik to: ", a)
            czykalk = input("     jeśli chcesz zakończyć wpisz N jeścli chesz kontynuować wpisz Y: ")
            if czykalk == 'N' or 'n':
                kalk = False
                break
            b = int(input("    podaj drugą liczbe: "))
    else:
        print("    podałeś zła liczbe lub wystąpił błąd")




