###
# Exercicio
###

# 1) Imprima os metodos disponiveis para uma lista e para uma tupla.
# 2) Faca um metodo para retornar apenas as diferencas entre as duas de metodos

# lista
list = [2, 3, 5, 7, 11, 13, 17, 19]
# tupla
tuple = (2, 3, 5, 7, 11, 13, 17, 19)

print('\nLista atual: ', list)
list.append(22)
print('Numero inserido no final: ', list)

list.insert(1,15)
print('Inserindo na posição 1: ', list)

list.reverse()
print('Invertendo a lista', list)

list.sort()
print('Ordenando a lista', list)

list.pop(0)
print('Removendo posição 0 com pop: ', list)

list.remove(15)
print('Removendo por item com remove: ', list)

print('Obtendo o indice do número 19 com index: ', list.index(19))

print('Contando quantas vezes aparece o número 11: ', list.count(11))

print('\nTupla não permite mudar seus valores, nem adicionar ou remover elemento algum!')
print('Tupla: ', tuple)
print('Número acessado na segunda posição da tupla: ', tuple[2])

print('Obtendo o indice do número 19 com index: ', tuple.index(19))

print('Contando quantas vezes aparece o número 3: ', tuple.count(3))

print('Acessando o item de indice 2 de uma tupla: ', tuple[2])


# 3) Adicione as coordenadas (latitude, longitude) para os dicts professor1, professor2 e professor3.
##Copie os dicts do arquivo 106.py

professor1 = {'id': 42, 'name': 'Alexandre Abreu', 'age': 30, 'state_origin': 'Minas Gerais', 'courses': ['Inteligência Artificial', 'Mineração de Dados', 'Programação para Internet I', 'Programação para Internet II']}
professor2 = {'id': 37, 'name': 'Denilson Barbosa', 'age': 40, 'state_origin': 'Paraná', 'courses': ['Inteligência Artificial', 'Banco de Dados I', 'Banco de Dados II', 'Programação para Internet I']}
professor3 = dict(id=28, name='Jorge Armino', idade=37)
professor3['state_origin'] = 'Rio Grande do Sul'
professor3['courses'] = ['Filosofia', 'Informática e Sociedade']


professor1['Latitude'] = '-26.1874457'
professor1['Longitude'] = '-50.3998166'
professor2['Latitude'] = '-26.1831987'
professor2['Longitude'] = '-50.3691398'
professor3['Latitude'] = '-26.1771891'
professor3['Longitude'] = '-50.3995146'

print('\nProfessor 1: ', professor1)
print('\nProfessor 2: ', professor2)
print('\nProfessor 3: ', professor3)
