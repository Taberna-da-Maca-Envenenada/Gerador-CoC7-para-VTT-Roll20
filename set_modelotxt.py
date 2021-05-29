from configparser import ConfigParser

config = ConfigParser()

config['Informacoes'] = {
    'nome': 'nome',
    'genero': 'm',
    'ocupacao': 'profissao',
    'idade': '20'
}

config['Atributos'] = {
    'Str': '60',
    'Con': '60',
    'Siz': '60',
    'Dex': '60',
    'Int': '60',
    'Edu': '60',
    'Pow': '60',
    'Luck': '60'
}

config['Derivados'] = {
    'Vida': '60 / 60',
    'Magia': '60 / 60',
    'Sanidade': '60 / 60',
    'Movimento': '7',
    'Valor_de_Combate': '120',
    'Corpo': '2',
    'DX': '+1d4'
}

config['Antecedentes'] = {
    'Descricao': 'bonito',
    'Ideologia_ou_Crenca': 'crenca',
    'Pessoa_Significativa': 'pessoa',
    'Local_Importante': 'local',
    'Pertence_Querido': 'pertence',
    'Caracteristica': 'caracteristica'
}

config['Anotacoes'] = {

}

with open('./Config/modelotxt.txt', 'w') as f:
    config.write(f)
    f.close()
