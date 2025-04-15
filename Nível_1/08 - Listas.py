'''
Listas:
Nesta aula, vamos aprender sobre listas em Python. 

- Uma lista é uma coleção de elementos ordenáveis e mutáveis. 
- Podemos declarar uma lista usando colchetes e separando os elementos por vírgula. 
- Os elementos podem ser de diferentes tipos. 

Podemos:
1. Acessar os elementos da lista usando índices, que começam em 0.
2. Exibir a lista completa ou apenas um elemento específico usando a função `print`.
3. Fatiar a lista, ou seja, obter um intervalo de elementos:
    - Fatiar do começo até um elemento específico.
    - Fatiar a partir de um elemento específico.

Na próxima aula, veremos sobre atribuição e os principais métodos das listas.
'''

minha_lista = [1, 2, 3, 4, 5, "Orlando", True, False]
print(minha_lista)  # Exibe a lista completa
print("Exibindo elementos em uma lista:", minha_lista[0])  # Exibe o primeiro elemento da lista
print("Exibindo elementos em uma lista:", minha_lista[5])  # Exibe o quinto elemento da lista
print("Exibindo fatiamento da lista:", minha_lista[1:7])  # Exibe os elementos a partir do segundo até o final da lista - Fatiamento de lista
print("Exibindo fatiamento da lista:", minha_lista[:6])  # Exibe os elementos do início até o sexto elemento
print("Exibindo fatiamento da lista:", minha_lista[3:])  # Exibe os elementos a partir do terceiro elemento até o final da lista