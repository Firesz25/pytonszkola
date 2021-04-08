def choinka3(ile):
    a = 0
    for x in range(0, 3):
        for y in range(0, ile):
            for i in range(0, y):
                print("#", end="")
                a = i
            if(a < y):    
                print(end="\n") 
    i = x