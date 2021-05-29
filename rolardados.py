### BIBLIOTECAS
import random
import time
random.seed(time.time())

### LEGENDA
#n = numero de dados
#dado = numero de faces que tem no dado
#s = soma dos resultados

### FUNÇÕES
def soma(n, dado):
    s = 0
    for i in range(n):
        s = s + random.randrange(1, dado)
    return(s)
