"""ex086 - Matriz em Python
Crie um programa que crie uma matriz de dimensao 3x3 e preencha com valores lidos
pelo teclado.
No final, mostre a matriz na tela, com a formatacao correcta."""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input("Digite um valor para a posicao [{}, {}]: ".format(linha, coluna)))

print("-=" * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print("[{:^5}]".format(matriz[linha][coluna]), end="")
    print()
