'''
Nesta aula, vamos aprender sobre o tipo booleano em programação. Os booleanos são variáveis que podem ter apenas dois valores: true (verdadeiro) ou false (falso). 
Eles são amplamente utilizados em todas as linguagens de programação, principalmente em comparações e condicionais. Nas condicionais, 
temos blocos de código que são executados se uma determinada condição for verdadeira. Podemos utilizar os operadores lógicos "and" e "or" para comparar duas entradas e obter uma saída. 
O operador "and" só retorna verdadeiro se as duas condições forem verdade.

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