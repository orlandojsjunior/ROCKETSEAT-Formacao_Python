'''
Loop while em Python.

- O `while` é usado para repetir um bloco de código enquanto uma condição for verdadeira.

Podemos:
1. Criar um contador que começa em 0 e é incrementado a cada iteração do loop:
    - O loop continua enquanto o contador for menor que 5.
    - Podemos usar o `break` para sair do loop em uma condição específica.
'''
# Exemplo de loop while com contador

print("Exemplo de while")
contador = 0
while True:
    print("Contagem:", contador)
    contador += 1
    if contador == 5:
        break

print("Programa finalizado")



