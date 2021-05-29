import manipulartxt
import random
import time
random.seed(time.time())

def nomes(genero):
    if genero == 'm':
        arquivodonome = 'nomes-masculinos.txt'
    else:
        arquivodonome = 'nomes-femininos.txt'
    #x = len(arquivodonome)
    i = random.randrange(2,5)
    if i == 2:
        nome1 = manipulartxt.gerar(arquivodonome)
        sobrenome = manipulartxt.gerar('sobrenomes.txt')
        sobrenome = manipulartxt.conferir(nome1,sobrenome,'sobrenomes.txt')
        nome1 = nome1.replace("\n", "")
        sobrenome = sobrenome.replace("\n", "")
        nome = nome1 + ' ' + sobrenome
    elif i == 3:
        nome1 = manipulartxt.gerar(arquivodonome)
        nome2 = manipulartxt.gerar('sobrenomes.txt')
        sobrenome = manipulartxt.gerar('sobrenomes.txt')
        nome2 = manipulartxt.conferir(nome1,nome2,'sobrenomes.txt')
        sobrenome = manipulartxt.conferir(nome1,sobrenome,'sobrenomes.txt')
        sobrenome = manipulartxt.conferir(nome2,sobrenome,'sobrenomes.txt')
        nome1 = nome1.replace("\n", "")
        nome2 = nome2.replace("\n", "")
        sobrenome = sobrenome.replace("\n", "")
        nome = nome1 + ' ' + nome2 + ' ' + sobrenome
    elif i == 4:
        nome1 = manipulartxt.gerar(arquivodonome)
        nome2 = manipulartxt.gerar(arquivodonome)
        sobrenome = manipulartxt.gerar('sobrenomes.txt')
        nome2 = manipulartxt.conferir(nome1,nome2,arquivodonome)
        sobrenome = manipulartxt.conferir(nome1,sobrenome,'sobrenomes.txt')
        sobrenome = manipulartxt.conferir(nome2,sobrenome,'sobrenomes.txt')
        nome1 = nome1.replace("\n", "")
        nome2 = nome2.replace("\n", "")
        sobrenome = sobrenome.replace("\n", "")
        nome = nome1 + ' ' + nome2 + ' ' + sobrenome
    else:
        nome1 = manipulartxt.gerar(arquivodonome)
        nome2 = manipulartxt.gerar(arquivodonome)
        nome3 = manipulartxt.gerar('sobrenomes.txt')
        sobrenome = manipulartxt.gerar('sobrenomes.txt')
        nome2 = manipulartxt.conferir(nome1,nome2,arquivodonome)
        nome3 = manipulartxt.conferir(nome1,nome3,arquivodonome)
        nome3 = manipulartxt.conferir(nome2,nome3,arquivodonome)
        sobrenome = manipulartxt.conferir(nome1,sobrenome,'sobrenomes.txt')
        sobrenome = manipulartxt.conferir(nome2,sobrenome,'sobrenomes.txt')
        sobrenome = manipulartxt.conferir(nome3,sobrenome,'sobrenomes.txt')
        nome1 = nome1.replace("\n", "")
        nome2 = nome2.replace("\n", "")
        nome3 = nome3.replace("\n", "")
        sobrenome = sobrenome.replace("\n", "")
        nome = nome1 + ' ' + nome2 + ' ' + nome3 + ' ' + sobrenome
    nome = nome.replace("\n", "")
    nome = func_junior(genero,nome)
    return nome

def func_junior(genero,nome):
    if genero == 'm':
        j = random.randrange(30)
        if j == 5:
            x = ['Junior','Junior','Junior','Junior','Junior','Filho','Neto']
            k = len(x)
            k = random.randrange(k)
            nome = nome + ' ' + x[k]
    else:
        j = random.randrange(150)
        if j == 5:
            x = ['Filha','Filha','Filha','Filha','Neta']
            k = len(x)
            k = random.randrange(k)
            nome = nome + ' ' + x[k]
    return nome
