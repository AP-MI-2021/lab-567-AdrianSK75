from Domain.carte import *

def ordonareCrescatoare(lista):
    return sorted(lista, key = lambda carte: getPret(carte))