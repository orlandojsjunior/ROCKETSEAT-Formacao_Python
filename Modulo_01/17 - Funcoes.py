# Funções em Python

def saudacao(nome):
    print(f"Olá, {nome}!")

print("\nChamando a função saudacao:")
saudacao("Alice")
saudacao("Bob")

# Função com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("\nChamando função quadrado:")
resultado_quadrado = quadrado(6)
print("Resultado da função quadrado:", resultado_quadrado)

# Função com múltiplos parâmetros
def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print("\nChamando a função soma:")
numero1 = 25
numero2 = 30
resultado_soma = soma(numero1, numero2)
print(f"A soma do número {numero1} e número {numero2} = {resultado_soma}.")