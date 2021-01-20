# r - leitura
# w - escrita, apaga o conteudo se ja existir
# a - escrita, mas preserva o conteudo se ja existir
# b - modo binario
# + - atualizacao (leitura e escrita)

impares = open("Aula 04 - impares.txt", "w")
pares = open("Aula 04 - pares.txt", "w")

for n in range(0, 1000):
    if n % 2 == 0:
        pares.write("{}\n".format(n))
    else:
        impares.write("{}\n".format(n))

impares.close()
pares.close()
