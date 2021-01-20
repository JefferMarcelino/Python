"""""ex108 - Formatando Moedas em Python
Adapte o codigo do desafio 107, criando uma funcao adicional chamada moeda()
que consiga mostrar os valores como um valor monetario formatado"""

from ex108 import moeda

preco = float(input("Digite o preco: "))
print("A metade de {} é {}".format(moeda.moeda(preco), moeda.moeda(moeda.metade(preco))))
print("O dobro de {} é {}".format(moeda.moeda(preco), moeda.moeda(moeda.dobro(preco))))
print("Aumentado 10%, temos {}".format(moeda.moeda(moeda.aumentar(preco, 10))))
