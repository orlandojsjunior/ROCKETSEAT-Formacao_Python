'''
Nesta aula, vamos aprender sobre o tipo booleano em programação. 

- Os booleanos são variáveis que podem ter apenas dois valores: `True` (verdadeiro) ou `False` (falso).
- Eles são amplamente utilizados em todas as linguagens de programação, principalmente em comparações e condicionais.

Podemos:
1. Utilizar os operadores lógicos "and" e "or" para comparar duas entradas e obter uma saída:
    - O operador "and" só retorna verdadeiro se as duas condições forem verdadeiras.
    - O operador "or" retorna verdadeiro se pelo menos uma das condições for verdadeira.
2. Criar blocos de código que são executados se uma determinada condição for verdadeira usando condicionais:
    - `if` para verificar a condição.
    - `else` para tratar o caso contrário.

Na próxima aula, veremos mais sobre operadores e estruturas condicionais.
'''

# Condição Verdadeira
True

# Condição Falsa
False 

# Condicionais
# if = se 
# else = senão 


if True:
    print("Bloco IF será executado")
else:
    print("Bloco ELSE não será executado")


# Operadores Lógicos: and e or

# and = e
if True and True:
    print("Bloco será executado")

if True and False:
    print("Bloco não será executado")

if False and False:
    print("Bloco não será executado")


# or = ou
if True or False:
    print("Bloco OR será executado")

if False or False:
    print("Bloco OR não será executado")

if True or True:
    print("Bloco OR será executado")    