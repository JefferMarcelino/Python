# r - leitura
# w - escrita, apaga o conteudo se ja existir
# a - escrita, mas preserva o conteudo se ja existir
# b - modo binario
# + - atualizacao (leitura e escrita)

import sys

print("Numero de parametros: {}".format(len(sys.argv)))

for n, p in enumerate(sys.argv):
    print("Parametro {} = {}".format(n, p))
