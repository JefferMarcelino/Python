# r - leitura
# w - escrita, apaga o conteudo se ja existir
# a - escrita, mas preserva o conteudo se ja existir
# b - modo binario
# + - atualizacao (leitura e escrita)

Largura = 79
entrada = open("Aula 06 - entrada.txt")

for linha in entrada.readlines():
    if linha[0] == ";":
        continue
    elif linha[0] == ">":
        print(linha[1:].rjust(Largura))
    elif linha[0] == "*":
        print(linha[1:].center(Largura))
    else:
        print(linha)

entrada.close()
