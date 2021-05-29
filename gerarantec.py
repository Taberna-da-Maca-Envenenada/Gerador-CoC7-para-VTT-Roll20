import manipulartxt
import random
import time
random.seed(time.time())

def descricao(genero):
    desc1 = manipulartxt.gerar('descricao01.txt')
    desc1 = manipulartxt.modgenero(genero,desc1)
    desc2 = manipulartxt.gerar('descricao02.txt')
    desc2 = manipulartxt.modgenero(genero,desc2)
    desc3 = manipulartxt.gerar('descricao03.txt')
    desc3 = manipulartxt.modgenero(genero,desc3)
    desc4 = manipulartxt.gerar('descricao04.txt')
    desc4 = manipulartxt.modgenero(genero,desc4)

    desc5 = manipulartxt.gerar2('descricao05-oculos.txt')
    desc6 = manipulartxt.gerar2('descricao06-chapeu.txt')
    desc7 = manipulartxt.gerar3(genero,'descricao07-cabelom.txt','descricao07-cabelof.txt')
    desc8 = manipulartxt.gerar3(genero,'descricao8-barba.txt','none.txt')

    desc = desc1 + ', ' + desc2 + ', ' + desc5 + desc6 + desc7 + desc8 + desc3 + ', ' + desc4
    return desc

def pessoasignificante():
    ps1 = manipulartxt.gerar('pessoassignificantes01.txt')
    ps2 = manipulartxt.gerar('pessoassignificantes02.txt')
    ps = ps1 + '. ' + ps2
    return ps
