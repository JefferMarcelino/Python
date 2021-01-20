"""ex087 - Mais sobre Matriz em Python
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input("Digite um valor para a posicao [{}, {}]: ".format(linha, coluna)))

print("-=" * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print("[{:^5}]".format(matriz[linha][coluna]), end="")
        if matriz[linha][coluna] % 2 == 0:
            spar += matriz[linha][coluna]
    print()
print("-=" * 30)

print("A soma dos valores pares e {}.".format(spar))
for l in range(0, 3):
    scol += matriz[l][2]
print("A soma dos valores da terceira coluna e {}.".format(scol))
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz [1][c] > mai:
        mai = matriz[1][c]
print("O maior valor da segunda linha e {}".format(mai))
