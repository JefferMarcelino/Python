"""
Modifique o programa da Aula 06 para imprimir 40 vezes o
simbolo de = se este for o primeiro caractere da linha.
Adicione tambem a opcao de parar de imprimir ate que se
pressione a tecla Enter cada vez que uma linha iniciar com 
. como primeiro caractere.
"""

Largura = 79
entrada = open("ex006 - entrada.txt")

for linha in entrada.readlines():
    if linha[0] == ";":
        continue
    elif linha[0] == ">":
        print(linha[1:].rjust(Largura))
    elif linha[0] == "*":
        print(linha[1:].center(Largura))
    elif linha[0] == "=":
        print("=" * 40)
        print(linha[1:])
    elif linha[0] == ".":
        cont = 0
        while True:
            print(linha[1:])
            cont += 1
            if cont >= 20:
                break
    else:
        print(linha)

entrada.close()
