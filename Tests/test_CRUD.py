from Domain.carte import *
from Logic.CRUD import *

def test_create(lista):
    print("CREATE")
    print("1. Verificare eroare")
    print("2. Adaugare lista")
    option = int(input("Introduceti optiunea: "))

    if option == 1:
        lista = adaugaCarte(lista, 1, "ksjdlskd", "klkds", 99, "silver")
        lista = adaugaCarte(lista, 2, "ksjdlskd", "klkds", 99, "silver")
        lista = adaugaCarte(lista, 1, "ksjdlskd", "klkds", 99, "silver")
    else:
        lista = adaugaCarte(lista, 1, "ksjdlskd", "klkds", 99, "silver")
        lista = adaugaCarte(lista, 2, "ksjdlskd", "klkds", 99, "silver")
        lista = adaugaCarte(lista, 3, "ksjdlskd", "klkds", 99, "silver")
        print(lista)

def test_update(lista):
    print("UPDATE")
    lista = adaugaCarte(lista, 1, "ksjdlskd", "klkds", 99, "silver")
    print("1. Verificare eroare")
    print("2. Modifica lista")
    option = int(input("Introduceti optiunea: "))

    if option == 1:
        lista = modificaCarte(lista, 2, "ksjdlskd", "klkds", 99, "silver")
    else:
        lista = modificaCarte(lista, 1, "Puterea prezentului", "Spiritualitate", 99, "silver")
        print(lista)

def test_delete(lista):
    print("DELETE")
    lista = adaugaCarte(lista, 1, "ksjdlskd", "klkds", 99, "silver")
    print("1. Verificare eroare")
    print("2. Modifica lista")
    option = int(input("Introduceti optiunea: "))
    if option == 1:
        lista = stergeCarte(lista, 2)
    else:
        lista = stergeCarte(lista, 1)
        print(lista)
        
def test_all():
    test_create([])
    test_update([])
    test_delete([])

