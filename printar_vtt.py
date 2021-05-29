import json
import manipulartxt

def criar_nomearq_pj(pj, arq):
    # Criando o nome do arquivo
    nomearq = pj.nome
    nomearq = nomearq.replace(" ","_")
    nomearq = nomearq + '.json'
    nomearq = arq.pastapj + '/' + nomearq
    return nomearq

def modificar_arquivo(pj, arq):
    # Criando / verificando pasta de personagens
    manipulartxt.pasta(arq.pastapj)
    n = criar_nomearq_pj(pj, arq)
    nomearq = str(n)

    # Manipulando Json
    f1 = open(arq.m_vtt, 'r', encoding='utf-8-sig') #abrindo modelo
    data = json.load(f1)
    f1.close()

    f = open(nomearq , 'w', encoding='utf-8-sig') #criando arquivo
    data['name'] = pj.nome
    data['attribs'][8]['current'] = pj.ocupacao
    data['attribs'][9]['current'] = pj.idade
    data['attribs'][10]['current'] = pj.genero
    data['attribs'][13]['current'] = pj.atrib.str
    data['attribs'][14]['current'] = pj.atrib.con
    data['attribs'][15]['current'] = pj.atrib.siz
    data['attribs'][19]['current'] = pj.atrib.dex
    data['attribs'][23]['current'] = pj.atrib.app
    data['attribs'][24]['current'] = pj.atrib.edu
    data['attribs'][25]['current'] = pj.atrib.int
    data['attribs'][26]['current'] = pj.atrib.pow
    data['attribs'][28]['current'] = pj.luck
    data['attribs'][29]['current'] = pj.atrib.pow
    data['attribs'][29]['max'] = pj.atrib.pow
    data['attribs'][105]['current'] = pj.antec.desc
    data['attribs'][106]['current'] = pj.antec.cren
    data['attribs'][107]['current'] = pj.antec.psig
    data['attribs'][108]['current'] = pj.antec.lcal
    data['attribs'][109]['current'] = pj.antec.pert
    data['attribs'][110]['current'] = pj.antec.carc

    json.dump(data,f)
    f.close()