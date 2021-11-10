from Domain.carte import *

def aplicareDiscount(lista):
    for carte in lista:
        tip_reducere = getTipReducere(carte)
        pret = getPret(carte)
        if tip_reducere == "silver":
            setPret(carte, pret - (pret * float(5 / 100)))
        elif tip_reducere == "gold":
            setPret(carte, pret - (pret * float(10 / 100)))
    return lista