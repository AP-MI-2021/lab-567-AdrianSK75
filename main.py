from UI.console import meniu_consola
from Logic.CRUD import adaugaCarte
from Tests.test_CRUD import test_all

def main():
    while True:
        print("1. Intrare in consola")
        print("2. Teste functionalitati CRUD")
        print("3. Iesire din din program")
        option = int(input("Introduceti optiunea: "))

        if option == 1:
            lista = []
            lista = adaugaCarte(lista, 1, "Puterea Prezentului", "Spiritualitate", 45.99, "silver")
            lista = adaugaCarte(lista, 2, "Regula 10X", "Mindset", 34.55, "none")
            lista = adaugaCarte(lista, 3, "Limitless", "LifeStyle", 150.99, "gold")
            lista = adaugaCarte(lista, 4, "Start With Why", "Business", 89.45, "silver")
            lista = adaugaCarte(lista, 5, "Arta subtila a nepasarii", "Mindset", 99.99, "gold")
            lista = adaugaCarte(lista, 6, "Gandeste ca un calugar", "Spiritualitate", 73.99, "gold")
            meniu_consola(lista)
        elif option == 2:
                test_all()
        else:
            break


if __name__ == '__main__':
    main()