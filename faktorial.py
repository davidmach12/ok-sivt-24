


def faktorial(cislo):
    if cislo == 1:
        return cislo
    else: return cislo*faktorial(cislo-1)





cislo=10
a=faktorial(cislo)
print(a)