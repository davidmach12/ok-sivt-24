def rozhodnuti(slovo:str)->None:
    sude = 0
    liche = 0

    for char in slovo:
        if ord(char.upper())%2:
            sude+=1
        else: liche+=1

    if sude>liche: print("cervene")
    elif liche>sude: print("zelene")
    else: print("ani jedno:D")
    
rozhodnuti("cřenčšě")

vysledky=dict[]








