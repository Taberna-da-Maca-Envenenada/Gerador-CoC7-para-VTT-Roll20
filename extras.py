import random
import time
random.seed(time.time())

def incremento_idade(x):
    i = random.randrange(2)
    if x > 90:
        return x
    if i == 1:
        x += 10
        x = incremento_idade(x)
    return x

#se o genero estiver 'mf' entao ele sorteia, se n n faz nada
def sortear_genero(genero):
    if genero == 'mf':
        genero = random.choice(['m','f'])
    return genero

def atrib_secundarios(pj):
    pj.deriv.san = pj.atrib.pow
    pj.deriv.vda = (pj.atrib.siz + pj.atrib.con) / 10
    pj.deriv.mag = pj.atrib.pow / 5

    # Movimento
    if pj.atrib.dex < pj.atrib.siz and pj.atrib.str < pj.atrib.siz:
        pj.deriv.mov = 7
    elif pj.atrib.dex > pj.atrib.siz and pj.atrib.str > pj.atrib.siz:
        pj.deriv.mov = 9
    else:
        pj.deriv.mov = 8
    
    j = 0
    if pj.idade >= 80:
        pj.deriv.mov = pj.deriv.mov - 5
    elif pj.idade >= 40:
        idade = pj.idade
        for i in range(idade):
            if idade >= 40:
                idade = idade - 10
                j = j + 1
    pj.deriv.mov = pj.deriv.mov - j

    #Combate
    pj.deriv.comb = pj.atrib.str + pj.atrib.siz
    #pj.deriv.dx = '-2'
    #pj.deriv.corp = -2
    print('combate ', pj.deriv.comb)
    if pj.deriv.comb <= 64:
        pj.deriv.dx = '-2'
        pj.deriv.corp = -2
    elif pj.deriv.comb <= 84:
        pj.deriv.dx = '-1'
        pj.deriv.corp = -1
    elif pj.deriv.comb <= 124:
        pj.deriv.dx = '0'
        pj.deriv.corp = 0
    elif pj.deriv.comb <= 164:
        pj.deriv.dx = '+1d4'
        pj.deriv.corp = 1
    elif pj.deriv.comb <= 204:
        pj.deriv.dx = '+1d6'
        pj.deriv.corp = 2
    else:
        pj.deriv.corp = 2
        j = 1
        com = pj.deriv.comb
        for i in range(com):
            if com > 204:
                com = com - 80
                j = j + 1
                pj.deriv.corp = pj.deriv.corp + 1
        pj.deriv.dx = '+' + str(j) + 'd6'
    
    print(pj.deriv.dx)
    print(pj.deriv.corp)
    return pj 