from Domain.carte import *

def verificaGenul(lista, gen):
    for carte in lista:
        if getGen(carte) == gen:
            return carte
    return None

def afiseazaMinimul(lista, gen):
    if verificaGenul(lista, gen) is None:
        raise ValueError("Genul nu exista")
    
    minim = 100000000
    for carte in lista:
        pret = getPret(carte)
        genul_cartii = getGen(carte)
        if genul_cartii == gen:
            if minim > pret:
                minim = pret
    return minim

