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

print(book1[:9])
print(book2[:11])
print(book3[:6])

# 2
titulo1 = book1[:9]
titulo2 = book2[:11]
titulo3 = book3[:6]

# 3
tamanhoBook1 = len(titulo1)
print(tamanhoBook1)
tamanhoBook2 = len(titulo2)
print(tamanhoBook2)
tamanhoBook3 = len(titulo3)
print(tamanhoBook3)

# 4
msg = 'Hi, {1} {0}!'.format(titulo1, titulo2)
print(msg)

# 5

# one

strLimpa = ''.join(palindrome_one.split())
isPalindrome = False

if strLimpa.lower() == strLimpa[::-1].lower():
	isPalindrome = True;

print(isPalindrome)

# two

strLimpa = ''.join(palindrome_two.split())
isPalindrome = False

if strLimpa.lower() == strLimpa[::-1].lower():
	isPalindrome = True;

print(isPalindrome)

# three

strLimpa = ''.join(palindrome_three.split())
isPalindrome = False

if strLimpa.lower() == strLimpa[::-1].lower():
	isPalindrome = True;

print(isPalindrome)

# four

strLimpa = ''.join(palindrome_four.split())
isPalindrome = False

if strLimpa.lower() == strLimpa[::-1].lower():
	isPalindrome = True;

print(isPalindrome)