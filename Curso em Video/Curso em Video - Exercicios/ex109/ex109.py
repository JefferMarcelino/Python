"""""ex109 - Formatando Moedas em Python
Modifique as funcoes que foram criadas no desafio 107 para que elas
aceitem um parametro ou mais, informando se o valor retornado por
elas vai ser ou nao formatado pela funcao moeda(), desenvolvido no
desafio 108."""


import moeda

preco = float(input("Digite o preco: "))
print("A metade de {} é {}".format(moeda.moeda(preco), moeda.metade(preco, True)))
print("O dobro de {} é {}".format(moeda.moeda(preco), moeda.dobro(preco, True)))
print("Aumentado 10%, temos {}".format(moeda.aumentar(preco, 10, True)))
print("Reduzindo 13%, temos {}".format(moeda.diminuir(preco, 13, True)))
