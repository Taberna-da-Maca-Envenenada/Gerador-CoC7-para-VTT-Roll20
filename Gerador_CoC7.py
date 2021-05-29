#!/usr/bin/env python
# -*- coding: utf-8 -*-

#BIBLIOTECAS
import rolardados
import manipulartxt
import gerarnomes
import gerarantec
import printar_vtt
import printar_txt
import extras
from configparser import ConfigParser
parser = ConfigParser()

# Lendo 'config.txt'
parser.read('Config/config.txt')
genero = parser.get('Caracteristicas','genero')

# Criando objeto personagem
class objeto:
    pass
pj = objeto()
pj.atrib = objeto()
pj.deriv = objeto()
pj.antec = objeto()


#GERANDO OldID
#texto = '-M'
#oldid = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(18))
#oldid = texto + oldid
#print(oldid)

n_pj = parser.get('Gerador','numero_pj_por_execucao')
nz = int(n_pj)
for nx in range(nz):
    #GERANDO NOME
    pj.genero = extras.sortear_genero(genero)
    print('#### INFORMAÇÕES ####')
    print(pj.genero)
    pj.nome = gerarnomes.nomes(pj.genero)
    print(pj.nome)

    #GERAR OCUPAÇÃO
    pj.ocupacao = manipulartxt.gerar('ocupacoes.txt')
    print('Ocupação: ', pj.ocupacao)

    # GERANDO ATRBUTOS ALEATORIOS
    ### AGE 10 + 3d10 + incremento aleatório
    x = rolardados.soma(3,10) + 10
    x = extras.incremento_idade(x)
    pj.idade = x
    ### STR 3d6x5
    x = 5 * rolardados.soma(3,6)
    pj.atrib.str = x
    ### CON 3d6x5
    x = 5 * rolardados.soma(3,6)
    pj.atrib.con = x
    ### SIZ 2d6+6 x5
    x = 5 * (rolardados.soma(2,6) + 6)
    pj.atrib.siz = x
    ### DEX 3d6x5
    x = 5 * rolardados.soma(3,6)
    pj.atrib.dex = x
    ### APP 3d6x5
    x = 5 * rolardados.soma(3,6)
    pj.atrib.app = x
    ### EDU 2d6+6 x5
    x = 5 * (rolardados.soma(2,6) + 6)
    pj.atrib.edu = x
    ### INT 2d6+6 x5
    x = 5 * (rolardados.soma(2,6) + 6)
    pj.atrib.int = x
    ### POW 3d6x5
    x = 5 * rolardados.soma(3,6)
    pj.atrib.pow = x
    ### LUCK 3d6x5
    x = 5 * rolardados.soma(3,6)
    pj.luck = x

    pj = extras.atrib_secundarios(pj)

    print('#### ATRIBUTOS ####')
    print('str = ', pj.atrib.str)
    print('con = ', pj.atrib.con)
    print('siz = ', pj.atrib.siz)
    print('dex = ', pj.atrib.dex)
    print('app = ', pj.atrib.app)
    print('edu = ', pj.atrib.edu)
    print('int = ', pj.atrib.int)
    print('pow = ', pj.atrib.pow)
    print('luck = ', pj.luck)
    print('age = ', pj.idade)

    #GERAR ANTECEDENTES
    ### Descrição
    print('#### ANTECEDENTES ####')
    pj.antec.desc = gerarantec.descricao(pj.genero)
    print('Descrição: ', pj.antec.desc)

    pj.antec.psig = gerarantec.pessoasignificante()
    print('Pessoa Significante: ', pj.antec.psig)

    pj.antec.cren = manipulartxt.gerar('crencas01.txt')
    print('Crença: ', pj.antec.cren)

    pj.antec.lcal = manipulartxt.gerar('localimportante01.txt')
    print('Local Importante: ', pj.antec.lcal)

    pj.antec.pert = manipulartxt.gerar('pertencesqueridos01.txt')
    print('Pertence Querido: ', pj.antec.pert)

    pj.antec.carc = manipulartxt.gerar('caracteristica01.txt')
    print('Característica: ', pj.antec.carc)


    ### Importando o modelo da ficha
    arq = objeto()
    arq.pastapj = parser.get('Arquivos','pasta_pj')
    arq.m_vtt = parser.get('Arquivos','modelo_VTT')
    arq.m_txt = parser.get('Arquivos','modelo_txt')

    ### MODIFICANDO ARQUIVO
    s = parser.get('Gerador','gerar_pj_para')
    if s == 'vtt':
        printar_vtt.modificar_arquivo(pj, arq)
    elif s == 'txt':
        printar_txt.modificar_arquivo(pj, arq)
    else:
        printar_vtt.modificar_arquivo(pj, arq)

