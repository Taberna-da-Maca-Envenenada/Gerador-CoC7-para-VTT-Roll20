import random
import time
import os
random.seed(time.time())

### Sortear uma linha de um documento
def gerar(arquivo):
    nomes = open( 'Data/' +arquivo, encoding="utf8")
    listanomes = nomes.readlines()
    nomes.close()
    i = len(listanomes)
    x = listanomes[random.randrange(i)]
    x = x.replace("\n", "")
    return x

def gerar2(arquivo):
    palavra = gerar(arquivo)
    if palavra != "":
        palavra = palavra + ', '
    return palavra

def gerar3(genero, arquivoM, arquivoF):
    if genero == 'm':
        palavra = gerar2(arquivoM)
    else:
        palavra = gerar2(arquivoF)
    return palavra

### Conferir se dois elementos são iguais, se não sortear novamente
def conferir(nome1,nome2, arquivo):
    if nome1 == nome2:
        nome2 = gerar_nome(arquivo)
        nome2 = nome.replace2("\n", "")
        nome2 = conferir_nomes(nome1, nome2, arquivo)
    else:
        return nome2
    return nome2

### Criando uma pasta se ela nao existe
def pasta(nome_da_pasta):
    listaarquivos = os.listdir('.')
    j = len(listaarquivos)
    flag = 0
    for i in range(j):
        if listaarquivos[i] == nome_da_pasta:
            flag = 1
    if flag == 0:
        os.mkdir('./' + nome_da_pasta)

### Modificar genero da palavra do masculino para o feminino
def modgenero(genero,palavra):
    if genero == 'f':
        if palavra == 'pé-frio':
            return palavra
        b = len(palavra)
        j = 0
        new = ''
        flag = 0
        for i in palavra:
            if j == b - 2 and i == 'ã':
                    flag = 1
                    new = new + 'o'
                    j = j + 1
            if j == b - 1 and flag == 0:
                if i == 'o':
                    new = new + 'a'
                    j = j + 1
                else:
                    new = new + i
                    j = j + 1
            elif j == b - 1:
                new = new + 'n'
                j = j + 1
                flag = 2
            elif flag == 2:
                new = new + 'a'
                j = j + 1
            else:
                j = j + 1
                new = new + i
        flag = 0
        j = 0
        new2 = ''
        for i in palavra:
            if j == b - 2:
                if i == 'o':
                    flag = 1
                    print(flag)
                new2 = new2 + i
            elif j == b - 1 and flag == 1:
                if i == 'r':
                    flag = 2
                    print(flag)
                new2 = new2 + i
            else:
                new2 = new2 + i
            j = j + 1
        if flag == 2:
            new2 = new2 + 'a'
            palavra = new2
        else:
            palavra = new
    return palavra
