def scrieCarte(id: int, titlu, gen, pret: float, tip_reducere):
    return [
        id,
        titlu,
        gen,
        pret,
        tip_reducere
    ]
def getId(carte):
    return carte[0]

def getTitlu(carte):
    return carte[1]

def setTitlu(carte, titlu_nou):
    carte[1] = titlu_nou

def getGen(carte):
    return carte[2]

def setGen(carte, gen_nou):
    carte[2] = gen_nou

def getPret(carte):
    return carte[3]

def setPret(carte, pret_nou):
    carte[3] = pret_nou

def getTipReducere(carte):
    return carte[4]

def setTipReducere(carte, tip_reducere_nou):
    carte[4] = tip_reducere_nou

def getCarte(carte):
    return "ID: {} , titlu: {}, gen: {}, pret: {}, tip reducere: {}".format(
        getId(carte),
        getTitlu(carte),
        getGen(carte),
        getPret(carte),
        getTipReducere(carte)
    )