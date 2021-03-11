def txt1(forsearch):
    print("        litera 'a' występuje: {}", forsearch.count("a"))
    print("        litera 'a' i 'A' występuje: {}", (forsearch.count("a") + forsearch.count("A")))
    print()

def txt2(text):
    print("       ", text.lower())
    print("       ", text.upper())
    print("       ", text.title())
    print("       ", text.swapcase())
    print()

def txt4( where, splits):
    if where == 1:
        for i in splits.split(" "):
            print("           ", i)
    if where == 2:
        for i in splits.split("."):
            print("           ", i)

def kontynowac():
    a = input("        jeścli chcesz kntynuować wpisz 'y' lub 'Y': ")
    if a == "y" or a == "Y":
        return True
    else:
        return False

if __name__ == '__main__':
    txt = input("\n        podaj text: ")
    ite = True
    while ite:
        co = int(input("""
        wybiesz co chcesz zrobić:
        1 - policzenie ile liter 'a' i 'A' występuje
        2 - zamiana wielkośći liter
        3 - podaiał textu na wyrazy lub zdania 
        """))
        if co == 1:
            txt1(txt)
            ite = kontynowac()
        elif co == 2:
            txt2(txt)
            ite = kontynowac()
        elif co == 3: 
            kto = int(input("""
            wybiesz co chcesz zrobić:
            1 - podziel na wyrazy 
            2 - podziel na zdania
            """))   
            txt4(kto, txt)
            ite = kontynowac()
        else:
            print("     podałeś złą liczbę")    