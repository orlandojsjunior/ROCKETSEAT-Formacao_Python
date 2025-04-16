'''
Principais métodos da listas:
Nesta aula, continuamos a explorar as listas em Python. 

- Aprendemos sobre a parte mutável das listas e como podemos fazer alterações nos elementos:
    - Demonstramos como trocar o primeiro elemento da lista por um texto usando atribuição.

- Discutimos sobre métodos de lista:
    1. `append`: Adiciona um elemento ao final da lista.
    2. `index`: Retorna o índice do primeiro elemento igual ao valor especificado.
    3. `insert`: Insere um elemento em um índice específico.
    4. `pop` e `remove`: Removem elementos da lista.
    5. `sort`: Organiza uma lista. 
        - Importante: O método `sort` só funciona corretamente se todos os elementos da lista forem do mesmo tipo.
'''

# Declarando uma lista com diferentes tipos de dados
minha_lista = [1, 2, 3, 4, 5, "Orlando", True, False]

print(minha_lista)  # Exibe a lista completa

minha_lista[0] = "Python"  # Troca o primeiro elemento da lista por um texto


# Exibindo os selementos da lista
print("Exibindo elementos em uma lista:", minha_lista[0])  # Exibe o primeiro elemento da lista

print("Exibindo elementos em uma lista:", minha_lista[5])  # Exibe o quinto elemento da lista

print("Exibindo fatiamento da lista:", minha_lista[1:7])  # Exibe os elementos a partir do segundo até o final da lista - Fatiamento de lista

print("Exibindo fatiamento da lista:", minha_lista[:6])  # Exibe os elementos do início até o sexto elemento

print("Exibindo fatiamento da lista:", minha_lista[3:])  # Exibe os elementos a partir do terceiro elemento até o final da lista


# Principais Metodos de listas

# 1. Metodo append(): Adicionando um elemento ao final da lista

minha_lista.append(6) 

print("Adicionando um elemento ao final da lista:", minha_lista)  # Exibe a lista após a adição do elemento


# 2. Metodo index(): Retorna o índice do primeiro elemento igual ao valor especificado

indice = minha_lista.index(6)  # Obtém o índice do elemento 6
print("Retorna o índice do primeiro elemento igual ao valor especificado:", indice)  # Exibe o índice do elemento 6


# 3. Metodo insert(): Insere um elemento em um índice específico

minha_lista.insert(2, 10)  # Insere o elemento 10 no índice 2

print("Insere um elemento em um índice específico:", minha_lista)  # Exibe a lista após a inserção do elemento


# 4. Metodo pop(): Remove o último elemento da lista e o retorna

elemento_removido = minha_lista.pop(3)  # Remove o último elemento da lista

print("Remove o último elemento da lista e o retorna:", elemento_removido)  # Exibe o elemento removido

print("Exibindo lista após o pop:", minha_lista)  # Exibe a lista após a remoção do elemento


# 5. Metodo remove(): Remove o primeiro elemento com o valor especificado

minha_lista.remove(True)  # Remove o elemento True da lista

print("Remove o primeiro elemento com o valor especificado:", minha_lista)  # Exibe a lista após a remoção do elemento


# 6. Metodo sort(): Organiza uma lista

'''
ATENÇÃO: O método sort só funciona corretamente se todos os elementos da lista forem do mesmo tipo.
minha_lista.sort()  # Organiza a lista em ordem crescente
print("Organiza uma lista:", minha_lista)  # Exibe a lista organizada - Nesse caso vai exibir mensagem de erro pois a lista não atende os requisitos para o sort

'''

# Criei uma lista com números inteiros para demonstrar o método sort

lista_desorganizada = [5, 2, 9, 1, 7, 3]

print("Lista desorganizada:", lista_desorganizada)  # Exibe a lista desorganizada

# Organizando a lista em ordem crescente

lista_desorganizada.sort()

print("Lista organizada em ordem crescente:", lista_desorganizada)

# Organizando a lista em ordem decrescente

lista_desorganizada.sort(reverse=True)

print("Lista organizada em ordem decrescente:", lista_desorganizada)