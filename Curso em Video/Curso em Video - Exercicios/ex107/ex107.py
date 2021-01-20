"""ex107 - Exercitando modulos em Python
Crie um modulo chamado moeda.py que tenha as funcoes incorporados aumentar(),
diminuir(), dobro() e metade().
Faca tambem um programa que importe esse modulo e use algumas dessas funcoes."""

from ex107 import moeda

preco = float(input("Digite o preco: "))
print("A metade de {}MTs é {}MTs".format(preco, moeda.metade(preco)))
print("O dobro de {}MTs é {}MTs".format(preco, moeda.dobro(preco)))
print("Aumentado 10%, temos {}MTs".format(moeda.aumentar(preco, 10)))
