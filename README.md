# Gerador-CoC7-para-VTT-Roll20
Gerador de personagens de RPG para a extensão  VTT Enhancement Suite para Roll20 ou em Bloco de Notas

##########################################################
########### INFORMAÇÕES ##################################
##########################################################

Programa: Gerador de Personagens de CoC 7e
Versão: 1.0.01
Sistema de RPG: Chamado de Cthulhu 7e
Importação: Extensão VTT Enhancement Suite para Roll20
Desenvolvido por: Taberna da Maçã Envenenada

##########################################################

Esse programa gera personagens aleatórios para serem
importados para o Roll20 com plugin VTT Enhancement
Suite no formato .json ou em arquivo de bloco de notas
comum .txt.

##########################################################
########### DIREITOS AUTORAIS ############################
##########################################################

Este programa é licenciado pela licença Creative Commons
portanto é livre para modificações, cópias, distribuição
e até mesmo a venda.
******** IMPORTANTE **************************************
Entretando algumas informações dos arquivos da pasta 'Data'
são retiradas da tradução do livro 'Chamado de Cthulhu 7e'
traduzido pela New Order do livro 'Call of Cthulhu 7th' da
editora Chaosium e estas sim possuem direitos reservados
pela Chaosium.

##########################################################
########### COMO UTILIZAR ################################
##########################################################

#### GERANDO PERSONAGEM ##################################

Basta executar o programa que ele irá gerar um personagem
aleatório de acordo com as configurações do config.txt que
está na pasta 'Config'. A pasta padrão para na qual os
personagens são salvos é a 'Personagens'.

#### Data ################################################

Qualquer arquivo da pasta 'Data' pode ser alterado para
corresponder melhor à sua criação de personagens.
Por exemplo, para acrescentar um sobrenome na lista que
poderá ser gerado, abra 'sobrenomes.txt' e coloque em uma
nova linha.
A probabilidade de ser escolhido um item dessas listas
depende de quantas vezes esse item está aparecendo, por
exemplo, o nome João é muito mais comum que Adalberto,
logo João aparece mais vezes no arquivo dos nomes
masculinos.
As linhas em branco que alguns arquivos contém também são
contabilizadas, elas são consideradas como 'não terá essa
característica' para alguns tipos de arquivos como o dos
cabelos.

#### CONFIGURAÇAO ########################################

Dentro da pasta 'Config' você encontra um arquivo chamado
'config.txt', nele você pode alterar as opções que achar
necessário.

[Caracteristicas]
genero
	Determina de qual gênero será o personagem:
	mf = sorteia aleatoriamente entre masculino ou feminino
	m = masculino
	f = feminino

dinheiro [ainda inativo]
	Determina em qual escala será o dinheiro do personagem:
	anos20 = dinheiro clássico do CoC para anos 20
	moderna = dinheiro do CoC para período moderno
	atual = correção para se assemelhar à realidade de 2021, corresponde a 3x moderna

ocupacoes_regem_atributos [ainda inativo]
	Os atributos são gerados para fazerem sentido com a ocupação:
	True = sim
	False = não, são gerados aleatoriamente

[Gerador]
numero_pj_por_execucao
	Número de personagens que o programa irá gerar a cada vez que for executado, por exemplo:
	1 = Irá gerar apenas 1 personagem
	2 = Irá gerar 2 personagens
	30 = Irá gerar 30 personagens

gerar_pj_para
	O personagem será gerado para qual plataforma?
	vtt = Extensão para navegador VTT Enhancement Suite para ser importado no Roll20 com arquivo .json
	txt = Criado em bloco de notas .txt

[Arquivos]
modelo_vtt
	Define qual é e onde está o modelo para personagens para VTT, o padrão é:
	Config/modelo.json

modelo_txt
	Define qual é e onde está o modelo para personagens em bloco de notas, o padrão é:
	Config/modelotxt.txt
pasta_pj
	Pasta onde serão armazenados os personagens gerados pelo algoritmo, a pasta padrão é:
	Personagens
© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
Loading complete
