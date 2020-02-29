#!/usr/bin/python3

professor1 = {'id': 42, 'name': 'Alexandre Abreu', 'age': 30, 'state_origin': 'Minas Gerais', 'courses': ['Inteligência Artificial', 'Mineração de Dados', 'Programação para Internet I', 'Programação para Internet II']}

professor2 = {'id': 37, 'name': 'Denilson Barbosa', 'age': 40, 'state_origin': 'Paraná', 'courses': ['Inteligência Artificial', 'Banco de Dados I', 'Banco de Dados II', 'Programação para Internet I']}

# Utilizando construtor
professor3 = dict(id=28, name='Jorge Armino', idade=37)

# adicionando chave e valor em um dict jah existente
professor3['state_origin'] = 'Rio Grande do Sul'
professor3['courses'] = ['Filosofia', 'Informática e Sociedade']

###
## Exercicios

# 1) Implemente o metodo define_default_city de acordo com a docstring definida no inicio da funcao.
#Utilize a clausula else no loop implementado.

#''' Define a capital do estado de origem como city_origin para um professor existente no arquivo.
#Retorna True se a capital do estado de origem existe no arquivo capitais-BR.csv e False, caso contrario.


def define_default_city(state):
	arquivo = open('capitais-BR.csv', 'r')
	for linha in arquivo:
		if state in linha:
			capital = linha.split(';')
			professor1['city_origin'] = capital[1]
			return True
	return False
	arquivo.close()

print(define_default_city(professor1['state_origin']))
print(professor1)

# 2) Remova do arquivo capitais-BR.csv todas capitais dos estados do sudeste e teste se sua funcao estah
#robusta o suficiente.

def ler_arq():
	arquivo = open('capitais-BR.csv', 'r')
	conteudo = arquivo.read()
	return conteudo

def remove_capital_sudeste():
	for linha in open('capitais-BR.csv', 'r'):
		quebra = linha.split(';')
		state = quebra[0]
		if(state == 'São Paulo' or state == 'Minas Gerais' or state == 'Espírito Santo' or state == 'Rio de Janeiro'):
			conteudo = ler_arq()
			arquivo = open('capitais-BR.csv', 'w')
			capital = linha.split(';')
			conteudo = conteudo.replace(capital[1], '\n')
			arquivo.write(conteudo)
			arquivo.close()

remove_capital_sudeste()

# 3) Faca uma funcao que le o arquivo lista-cpf.txt, retorne a quantidade de CPF unicos (sem repeticao)
#e os escreva em um arquivo lista-cpf-unicos.txt. Eh necessario descompactar o arquivo lista-cpf.txt.tar.gz
#primeiro.
