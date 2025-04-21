'''
Os loops são estruturas que nos permitem repetir um bloco de código enquanto uma condição for verdadeira. 

Existem dois tipos de loops: o "for" e o "while". 
Nesta aula, vamos focar no loop "for". 

O loop "for" é utilizado para iterar sobre uma sequência de elementos, como listas, tuplas e dicionários. 
Vamos começar vendo como o loop "for" funciona com listas. 
Em seguida, veremos como utilizá-lo com tuplas e dicionários. 

Com dicionários, podemos imprimir as chaves, os valores ou ambos juntos.
'''


print("for utilizando lista")

lista = [1, 2, 3, 4, 5]
for elemento in lista:
  print(elemento)


print("For utilizando tupla") #TODO: teste 01
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
  print(elemento)


pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
print("For utilizando dicionatio - chaves")
for chave in pessoa.keys():
  print(chave)


print("\nFor utilizando dicionatio - valores")
for valor in pessoa.values():
  print(valor)


print("\nFor utilizando dicionatio - items")
for chave, valor in pessoa.items():
  print(f"{chave}: {valor}")
