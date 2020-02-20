###
# Exercicios
###

# 1) Crie uma funcao que receba duas listas e verifique se elas são iguais. Cada elemento e sua ordem devem ser o mesmo. Retorne True ou False.
#
# 2) Crie uma funcao que verifica se duas strings são palindromes perfeitas. Faca as 'limpeza'/sanitizacao necessarias.  Retorne True ou False.
#
# OBS.: Utilize apenas o que foi estudado ate agora

def listasIguais(a, b):
  if a == b:
    return True;
  return False;

lista1 = [1,2,3,4]
lista2 = [1,2,3,4]

print(listasIguais(lista1,lista2))

def palindrome(str1):
  strLimpa = ''.join(str1.split())
  if strLimpa.lower() == strLimpa[::-1].lower():
    return "Esta frase é palindrome"
  return "Esta frase não é palindrome"

print(palindrome("Nata n"))
