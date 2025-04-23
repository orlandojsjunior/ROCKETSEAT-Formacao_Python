'''
Nesta aula, vamos aprender sobre condicionais em Python. 
As condicionais permitem tomar decisões com base em condições e executar um bloco de código específico. 
Vamos utilizar os comandos if, elif e else para fazer comparações. 

Por exemplo, podemos comparar a idade de uma pessoa e executar diferentes blocos de código com base nessa comparação. 
Também vamos aprender sobre os operadores de comparação, como maior que, menor que, igual a, diferente de, entre outros. 

Além disso, vou mostrar como podemos simplificar o uso de condicionais em uma única linha de código. 
As condicionais são muito utilizadas na programação para criar diferentes fluxos de execução e fazer comparações.
'''

# Condicionais if, elif e else.
# Condicionais são estruturas que permitem tomar decisões com base em condições.

# if, elif e else


idade = 18  # Define a idade como 18
print("Exemplo de comando if")

# Verifica se a idade é maior ou igual a 18
if idade >= 18:
    print("Você é maior de idade.")  # Exibe mensagem se a condição for verdadeira
# Verifica se a idade é maior ou igual a 12 (mas menor que 18, devido à ordem das condições)
elif idade >= 12:
    print("Você é um adolescente")  # Exibe mensagem se a condição for verdadeira
# Caso nenhuma das condições anteriores seja verdadeira
else:
    print("Você é menor de idade.")  # Exibe mensagem para todas as outras idades

# Operador ternário para definir uma mensagem com base na idade
mensagem = "Pode tirar a carteira de habilitação" if idade >= 18 else "Você não pode tirar a carteira de habilitação"
print(mensagem)  # Exibe a mensagem correspondente

# if idade == 19:
#   print("Você tem 19 anos")

# if idade < 18:
#   print("Você é menor de idade")

# if idade != 10:
#   print("Você não tem 10 anos")