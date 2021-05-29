from configparser import ConfigParser

config = ConfigParser()

config['Caracteristicas'] = {
    'genero': 'mf',
    'dinheiro': 'atual',
    'ocupacoes_regem_atributos': 'False'
}

config['Gerador'] = {
    'numero_pj_por_execucao': '1',
    'gerar_pj_para': 'VTT'
}

config['Arquivos'] = {
    'modelo_VTT': 'Config/modelo.json',
    'modelo_txt': 'Config/modelotxt.txt',
    'pasta_pj': 'Personagens'
}

with open('./Config/config.txt', 'w') as f:
    config.write(f)
    f.close()
