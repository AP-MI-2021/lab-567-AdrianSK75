from Domain.carte import *

def verificaTitlul(lista, titlu):
    for carte in lista:
        if getTitlu(carte) == titlu:
            return carte
    return None

def gasesteCarteDupaTitlu(lista, titlu):
    if verificaTitlul(lista, titlu) is None:
        raise ValueError("Nu exista titlul")
        
    for carte in lista:
        titlu_gasit = getTitlu(carte)
        gen_precedent = getGen(carte)
        if titlu_gasit == titlu:
            print(titlu_gasit, " ", gen_precedent)
            gen = input("Introduceti un alt gen pentru aceasta carte: ")
            setGen(carte, gen)
    return lista
