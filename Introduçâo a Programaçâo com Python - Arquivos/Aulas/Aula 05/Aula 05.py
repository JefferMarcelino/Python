# r - leitura
# w - escrita, apaga o conteudo se ja existir
# a - escrita, mas preserva o conteudo se ja existir
# b - modo binario
# + - atualizacao (leitura e escrita)

multiplos4 = open("Aula 05 - multiplos de 4.txt", "w")
pares = open("../Aula 04/Aula 04 - pares.txt")

for l in pares.readlines():
    if int(l) % 4 == 0:
        multiplos4.write(l)

pares.close()
multiplos4.close()
