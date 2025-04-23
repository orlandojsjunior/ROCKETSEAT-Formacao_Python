'''
Nesta aula, vamos falar sobre entrada de dados em programas. 
A entrada de dados permite que o programa interaja com o usuário, permitindo que ele digite valores no terminal. 

Para isso, podemos utilizar a função input(), onde podemos fazer uma pergunta ao usuário e armazenar a resposta em uma variável. 
Por exemplo, podemos perguntar a idade do usuário e usar essa informação para tomar decisões no programa. 

É importante lembrar que o valor digitado pelo usuário será armazenado como uma string. 
Se precisarmos comparar com números, devemos converter para inteiro usando a função int(). 

Dessa forma, podemos criar programas mais interativos e intuitivos.
'''

# Exemplo de entrada de dados

nome = input('Qual o seu nome? ')
print(f'Olá, {nome}!')

idade = int(input('Qual a sua idade? '))
print(f'Sua idade é: {idade} anos!')

temperatura = float(input('Qual a temperatura hoje?'))
print(f'A temperatura de hoje é: {temperatura} graus!')
