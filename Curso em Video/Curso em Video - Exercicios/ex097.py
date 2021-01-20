"""ex097 - Um print especial
Faca um programa que tenha uma funcao chamada escreva(), que receba um texto
qualquer como parametro e mostre uma mensagem com tamanho adaptavel.
Ex:
escreva("Ola, Mundo!")
saida:
~~~~~~~~~~~~~~
  Ola, Mundo!
~~~~~~~~~~~~~~"""


def escreva(msg):
    tam = len(msg) + 4
    print("~" * tam)
    print(f"  {msg}")
    print("~" * tam)


# PROGRAMA PRINCIPAL
escreva("Jeffer Marcelino")
escreva("Curso de Python no Youtube")
escreva("CeV")
