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
    'nome': 'Orlando',
    'idade': 45,
    'curso': 'Formação Python',
}

print(f"Dicionario {aluno}")  # Exibindo o dicionário completo

print(f"Nome: {aluno['nome']}")  # Exibindo o valor associado à chave 'nome'

print(f"Idade: {aluno['idade']}")  # Exibindo o valor associado à chave 'idade'

print(f"Curso: {aluno['curso']}")  # Exibindo o valor associado à chave 'curso'

print(f"Tipo: {type(aluno)}")  # Exibindo o tipo do objeto 'aluno'

print(f"Chaves: {aluno.keys()}")  # Exibindo todas as chaves do dicionário

# Adicionando novos pares chave-valor ao dicionário
aluno['Telefone'] = '11 99999-9999'
aluno['Endereco'] = 'Rua das Flores, 123'
aluno['Sobrenome'] = 'Junior'

print(f"Dicionario Atualizado {aluno}") 
print(f"Sobrenome: {aluno['Sobrenome']}") # Exibindo o sobrenome