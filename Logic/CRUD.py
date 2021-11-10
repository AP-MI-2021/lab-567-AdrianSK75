from Domain.carte import *

def verificaLista(lista, id):
    for carte in lista:
        if getId(carte) == id:
            return carte
    return None

def afiseazaLista(lista):
    print("\n")
    for carte in lista:
        print(getCarte(carte))
    print("\n")

def adaugaCarte(lista, id, titlu, gen, pret, tip_reducere):
    if verificaLista(lista, id) is not None:
        raise ValueError("Cartea exista deja in lista")
    
    puneInLista = scrieCarte(id, titlu, gen, pret, tip_reducere)
    return lista + [puneInLista]

def modificaCarte(lista, id, titlu, gen, pret, tip_reducere):
    if verificaLista(lista, id) is None:
        raise ValueError("Cartea nu exista in lista")
    
    carte_actualizata = scrieCarte(id, titlu, gen, pret, tip_reducere)
    for carte in lista:
        if getId(carte) == id:
            lista.append(carte_actualizata)
        else:
            lista.append(carte)
    return lista

def stergeCarte(lista, id):
    if verificaLista(lista, id) is None:
        raise ValueError("Cartea nu exista in lista")
    
    return [carte for carte in lista if getId(carte) != id]
    