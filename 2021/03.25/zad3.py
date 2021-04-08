def kwadrat(ile):
    for x in range(0, ile):
        for y in range(0, ile):
            print("X", end="")
        print(end="\n")    
    x = y
    y = x

def kwadrata(ile):
    for x in range(0, ile):
        a = ""
        for y in range(0, ile):
            a = a + "X"
        print(a)  
    x = y
    y = x 

def kwadratb(ile):
    for x in range(0, ile):
        print("X" * ile)
    a = x
    x = a    
 