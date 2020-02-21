
###
# Exercicios
###

## Usando a lista: ['a','b','c']
# 1) Faca um loop para retornar: ['A','B','C']

list = ['a','b','c']

for i in list:
        print(i)


## Usando os numeros: [0, 1, 3, 4, 5]
# 2) Faca um loop para retornar a soma de todos os elementos da listas

list1 = [0, 1, 3, 4, 5]


soma = 0
for i in list1:
        soma += i
print(soma)

# 3) Faca um loop para retornar apenas os numeros impares

for i in list1:
        if(i % 2 != 0):
                print(i)

## usando a string: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
# 4) Conte quantas palavras de tamanho >= 5 existe nessa string

frase = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

total = 0
quebra = frase.split(' ')

for i in quebra:
    if(len(i) >= 5):
        total += 1
print(total)

# 5) Usando list comprehension, crie uma lista com os multiplos de 3 de 0 ate 100

lista = [numero for numero in range(1, 100+1) if numero % 3 == 0]
print(lista)

# Faca uma funcao para encontrar os numeros primos no intervalo [2, 10), mas nao utilize a clausula else do for


for n in range(2, 10):
        j = 2
        counter = 0
        while j < n:
                if n % j == 0:
                        counter = 1
                        j += 1
                else:
                        j += 1
        if counter == 0:
                print(n , ' - é um número primo')
        else:
                counter = 0;
