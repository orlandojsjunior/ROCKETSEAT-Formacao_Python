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



# Continuação Loop for

'''
Explorando algumas técnicas úteis para aprimorar o uso do loop "for". 

1. **Função range()**: 
  A função `range()` é usada para gerar uma sequência de números, o que facilita a criação de listas numéricas sem a necessidade de declarar manualmente cada elemento.

2. **Função len() com range()**: 
  Podemos combinar `len()` com `range()` para iterar sobre os índices de uma lista, permitindo acessar e manipular elementos diretamente.

3. **Função enumerate()**: 
  A função `enumerate()` é extremamente útil para iterar sobre uma lista, fornecendo tanto o índice quanto o valor de cada elemento. Isso elimina a necessidade de gerenciar índices manualmente.

Essas ferramentas são amplamente utilizadas em programação e ajudam a tornar o código mais eficiente e legível. Saber quando e como utilizá-las é essencial para escrever scripts Python mais robustos e elegantes.
'''

# [0,1,2,3,4]
print("\n Utilizando a função range()")
for numero in range(5):
  print("Numero:", numero)


print("\n Utilizando a função range() com len()")
lista = [1, 2, 3, 4, 5]
for indice in range(0, len(lista)):
  print("Indice:", indice)
  print("Elemento:", lista[indice])
  if indice == 3:
    lista[indice] = 5
  else:
    lista[indice] = 0
print(lista)


# enumerate()
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
  print(f"{indice}: {valor}")
  if indice == 1:
    print("Idice 1")