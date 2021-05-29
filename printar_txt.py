import manipulartxt
from configparser import ConfigParser
parser = ConfigParser()

def criar_nomearq_pj(pj, arq):
    # Criando o nome do arquivo
    nomearq = pj.nome
    nomearq = nomearq.replace(" ","_")
    nomearq = nomearq + '.txt'
    nomearq = arq.pastapj + '/' + nomearq
    return nomearq

def modificar_arquivo(pj, arq):
    # Criando / verificando pasta de personagens
    manipulartxt.pasta(arq.pastapj)
    n = criar_nomearq_pj(pj, arq)
    nomearq = str(n)

    # Manipulando Paser
    parser.read(arq.m_txt) #lendo o modelo
    data = {s:dict(parser.items(s)) for s in parser.sections()}

    data['Informacoes']['nome'] = pj.nome
    data['Informacoes']['ocupacao'] = pj.ocupacao
    data['Informacoes']['idade'] = pj.idade
    data['Informacoes']['genero'] = pj.genero
    data['Atributos']['str'] = pj.atrib.str
    data['Atributos']['con'] = pj.atrib.con
    data['Atributos']['siz'] = pj.atrib.siz
    data['Atributos']['dex'] = pj.atrib.dex
    data['Atributos']['app'] = pj.atrib.app
    data['Atributos']['edu'] = pj.atrib.edu
    data['Atributos']['int'] = pj.atrib.int
    data['Atributos']['pow'] = pj.atrib.pow
    data['Atributos']['luck'] = pj.luck
    data['Antecedentes']['descricao'] = pj.antec.desc
    data['Antecedentes']['ideologia_ou_crenca'] = pj.antec.cren
    data['Antecedentes']['pessoa_significativa'] = pj.antec.psig
    data['Antecedentes']['local_importante'] = pj.antec.lcal
    data['Antecedentes']['pertence_querido'] = pj.antec.pert
    data['Antecedentes']['caracteristica'] = pj.antec.carc

    sanidade = str(pj.deriv.san) + ' / ' + str(pj.deriv.san)
    vida = str(pj.deriv.vda) + ' / ' + str(pj.deriv.vda)
    magia = str(pj.deriv.mag) + ' / ' + str(pj.deriv.mag)
    data['Derivados']['sanidade'] = sanidade
    data['Derivados']['vida'] = vida
    data['Derivados']['magia'] = magia
    data['Derivados']['movimento'] = pj.deriv.mov
    data['Derivados']['valor_de_combate'] = pj.deriv.comb
    data['Derivados']['corpo'] = pj.deriv.corp
    data['Derivados']['dx'] = pj.deriv.dx

    parser.read_dict(data)
    with open(nomearq, 'w') as f:
        parser.write(f)
        f.close()


