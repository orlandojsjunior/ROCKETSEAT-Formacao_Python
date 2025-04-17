'''
Principais conceitos sobre dicionários:
Nesta aula, continuamos nossos estudos sobre dicionários em Python.

- Atualizando valores:
    - Para atualizar um valor existente em um dicionário, utilizamos a mesma sintaxe de criação.
   
- Removendo pares chave-valor:
    - Utilizamos o comando `del` para remover um par chave-valor.
    - Importante: O `del` exclui todo o par chave-valor, não apenas a chave ou o valor separadamente.
   
- Métodos principais:
    1. `keys()`: Retorna todas as chaves do dicionário.
    2. `values()`: Retorna todos os valores do dicionário.
    3. `items()`: Retorna uma lista de tuplas contendo todos os pares chave-valor.
    - Observação: Para acessar os elementos individualmente, é necessário transformar o resultado em uma lista utilizando a função `list()`.
'''

# Dicionario da aula anterior
aluno = {
    'nome': 'Orlando',
    'idade': 44,
    'curso': 'Formação Python',
}

print(f"Dicionário: {aluno}")


# Adicionando novos pares chave-valor ao dicionário
aluno['Telefone'] = '11 99999-9999'
aluno['Endereco'] = 'Rua das Flores, 123'
aluno['Sobrenome'] = 'Junior'

# Exibindo o dicionário atualizado
print(f"Dicionário Atualizado: {aluno}")
print(f"Sobrenome: {aluno['Sobrenome']}")




# Atualizando valores no dicionário
aluno["idade"] = 45
print("Idade atualizada:", aluno["idade"])

# Removendo um par chave-valor
del aluno["Sobrenome"]
print("Dicionário após remoção:", aluno)

# Métodos: keys(), values(), items()
chaves = list(aluno.keys())
print("Chaves do dicionário:", chaves)
print("Primeira chave:", chaves[0])

valores = list(aluno.values())
print("Valores do dicionário:", valores)
print("Primeiro valor do dicionário:", valores[0])

itens = list(aluno.items())
print("Pares chave-valor do dicionário:", itens)
print("Primeira chave-valor: %s = %s" % (itens[0][0], itens[0][1]))