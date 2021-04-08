from zad1 import ciagsumy
from zad2 import choinka3
from zad3 import kwadrat, kwadrata, kwadratb

if __name__ == '__main__':

    czy = True
    while czy:
        a = int(input("podaj które zadanie chcesz wyswietlić\nzad1: 1\nzad2: 2\nzad3: 3\n"))
        if(a == 1):
            ile = int(input("podaj jaka długość ma mieć ciag: "))
            ciagsumy(ile)
        if(a == 2):
            ile = int(input("podaj jakie wymiary ma mieć choinka: ")) 
            choinka3(ile) 
        if(a == 3):
            b = int(input("podaj ktorym sposobem narysować wadrat\npierwszy: 1\ndrugi: 2\ntrzeci: 3\n"))
            if(b == 1):
                ile = int(input("podaj jakie wymiary ma mieć kwadrat: \n"))
                kwadrat(ile)
            if(b == 2):
                ile = int(input("podaj jakie wymiary ma mieć kwadrat: \n"))
                kwadrata(ile)  
            if(b == 3):
                ile = int(input("podaj jakie wymiary ma mieć kwadrat: \n"))
                kwadratb(ile)
            else:
                print("podałeś zła wartość")
        else:
            print("podałeś zła wartość")              
        c = input("jesli chcesz kontynuowac wpisz 'Y' lub 'y': ")
        if(c == "Y" or c == "y"):
            czy = True
        else:
            czy = False                         

