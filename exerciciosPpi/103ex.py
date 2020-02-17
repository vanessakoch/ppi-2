###
# Exercicios
###

# 1) Extraia o titulo do livro da string
# 2) Salve o titulo de cada livro em uma variável
# 3) Quantos caracteres cada título tem?
# 4) Imprima com a formatacao: {Titulo} - {Autor}, {Ano}


book1 = 'Homo Deus by Yuval Noah Harari, 2015'
book2 = 'Antifragile by Nassim Nicholas Taleb, 2012'
book3 = 'Fooled by Randomness by Nassim Nicholas Taleb, 2001'

# 5) Verifique se uma palavra é uma palindrome perfeita.
# Palindrome perfeito sao palavras que ao serem escritas em ordem reversa,
# resultam na mesma palavra.
# Ignore espacos e caixa alta

palindrome_one = 'ovo'
palindrome_two = 'Natan'
palindrome_three = 'luz azul'
palindrome_four = 'caneta azul'

# 1
#print(book1[0:9])

print(book1.split('by'))

# 2
variavelTitulo = book2[0:11]
print(variavelTitulo)

# 3
tamanhoBook1 = len(book1[0:8])
print(tamanhoBook1)
tamanhoBook2 = len(variavelTitulo)
print(tamanhoBook2)

# 4
print("{", book1[0:9], "} - {", book1[13:30], "}, {", book1[32:37], "}")

# 5
isPalindrome = False
inverso = palindrome_one[::-1]

if(palindrome_one == inverso):
	isPalindrome = True

print(isPalindrome)