'''
Principais conceitos sobre dicionários:
Nesta aula, aprendemos sobre dicionários em Python.

- Introdução aos dicionários:
    - Um dicionário é uma coleção não ordenada de pares chave-valor.
    - Podemos criar um dicionário usando chaves `{}` e armazenar informações dentro dele.

- Acessando e manipulando dicionários:
    1. Acessar valores: Utilizamos as chaves para acessar os valores correspondentes.
        - Importante: Se tentarmos acessar uma chave que não existe, receberemos uma exceção `KeyError`.
    2. Adicionar novas chaves e valores: É possível adicionar novos pares chave-valor mesmo após a criação do dicionário.
    3. Dicionários aninhados: Podemos armazenar outros dicionários como valores.

- Exibindo dicionários:
    - Utilizamos a função `print` para exibir o conteúdo de um dicionário.
'''

# Criando um dicionário

aluno = {
    'nome': 'João',
    'idade': 20,
    'curso': 'Engenharia de Software'
}