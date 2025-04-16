'''
Principais características das tuplas:
Nesta aula, vamos aprender sobre o próximo tipo de variável em Python: a tupla.

- A tupla é uma coleção ordenada e imutável de elementos:
    - Uma vez criada, não podemos modificar seus elementos.
    - Podemos criar uma tupla usando parênteses e acessar seus elementos da mesma forma que uma lista.

- Métodos úteis das tuplas:
    1. `count`: Retorna a quantidade de vezes que um elemento aparece na tupla.
    2. `index`: Retorna o índice da primeira ocorrência de um elemento na tupla.
'''

# Criando uma tupla

minha_tupla = (1, 2, 2, 3, 4)

print(f"Minha Tupla: {minha_tupla}")
print(f"Tipo: {type(minha_tupla)}")
print(f"Acessando o elemento no índice 0: {minha_tupla[0]}")  # Acessando o primeiro elemento da tupla
print(f"Acessando o último elemento da tupla: {minha_tupla[-1]}")  # Acessando o último elemento usando índice negativo

# Metodo count().

Contagem = minha_tupla.count(2)  # Contando quantas vezes o número 2 aparece na tupla
print(f"Quantidade de vezes que o elemento 2 aparece na tupla: {Contagem}")
print(f"Quantidade de vezes que o elemento 2 aparece na tupla: {minha_tupla.count(2)}")

# Metodo index().

Indice = minha_tupla.index(3)  # Encontrando o índice da primeira ocorrência do número 3 na tupla
print(f"Índice do elemento 3 na tupla: {Indice}")
print(f"Índice do elemento 3 na tupla: {minha_tupla.index(3)}")
