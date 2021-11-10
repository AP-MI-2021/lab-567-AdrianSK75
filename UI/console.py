from Logic.CRUD import *
from Logic.discount import *
from Logic.modificare_gen import *
from Logic.gasire_minim_dupa_gen import *
from Logic.ordonare_crescatoare import *

def adauga(lista):
    try:
        id = int(input("ID: "))
        titlu = input("Titlu: ")
        gen = input("Gen: ")
        pret = float(input("Pret: "))
        tip_reducere = input("Tip reducere (none, silver, gold): ")
        lista = adaugaCarte(lista, id, titlu, gen, pret, tip_reducere)
        return lista
    except ValueError as error:
        print(error)
        return lista

def modifica(lista):
    try:
        id = int(input("ID: "))
        titlu = input("Titlu: ")
        gen = input("Gen: ")
        pret = float(input("Pret: "))
        tip_reducere = input("Tip reducere (none, silver, gold): ")
        lista = modificaCarte(lista, id, titlu, gen, pret, tip_reducere)
        return lista
    except ValueError as error:
        print(error)
        return lista

def stergere(lista):
    try:
        id = int(input("ID: "))
        return stergeCarte(lista, id)
    except ValueError as error:
        print(error)
        return lista
    
def operatii_crud(lista):
    while True:
        print("1. Vezi lista cu carti")
        print("2. Adauga o carte")
        print("3. Editeaza o carte")
        print("4. Sterge o carte")
        print("5. Iesire din CRUD")
        option = int(input("Introduceti optiunea: "))
        if option == 1:
            afiseazaLista(lista)
        elif option == 2:
            lista = adauga(lista)
        elif option == 3:
            lista = modifica(lista)
        elif option == 4:
            lista = stergere(lista)
        else:
            print("Ai iesit din interfata CRUD")
            break

def schimbareaGenuluiDupaTitlu(lista):
        try:
            titlu = input("Introduceti titlul: ")
            lista = gasesteCarteDupaTitlu(lista, titlu)
            return lista
        except ValueError as error:
            print(error)
        return lista
                
def determinareMinimDupaGen(lista):
        try:
            gen = input("Introduceti genul: ")
            return afiseazaMinimul(lista, gen)
        except ValueError as error:
            print(error)

def uiOrdonareDupaPret(lista):
    lista = ordonareCrescatoare(lista)
    return afiseazaLista(lista)


def meniu_consola(lista):
    while True:
        print("1. Operatiile CRUD.")
        print("2. Aplicarea unui discount de 5% pentru toate reducerile silver și 10% pentru toate reducerile gold.")
        print("3. Modificarea genului pentru un titlu dat.")
        print("4. Determinarea prețului minim pentru un gen.")
        print("5. Ordonarea vânzărilor crescător după preț.")
        option = int(input("Introduceti optiunea: "))
        if option == 1:
            operatii_crud(lista)
        elif option == 2:
            lista = aplicareDiscount(lista)
            afiseazaLista(lista)
        elif option == 3:
            lista = schimbareaGenuluiDupaTitlu(lista)
            afiseazaLista(lista)
        elif option == 4:
            print(determinareMinimDupaGen(lista))
        elif option == 5:
            print(ordonareCrescatoare(lista))
        else:
            print("Ai iesit din consola!")
            break