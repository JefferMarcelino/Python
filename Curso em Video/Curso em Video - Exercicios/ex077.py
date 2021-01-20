"""ex077 - Contado vogais em Tupla
Crie um programa que tenha uma tupla com varias palavras
(nao usar acentos). Depois disso, voce deve mostrar, para
cada palavra, quais sao as suas vogais."""

palavras = ("aprender", "programar", "linguagem", "python",
            "curso", "gratis", "estudar", "praticar", "trabalhar",
            "mercado", "programador", "futuro")
for palavra in palavras:
    print("\nNa palavra {} temos ".format(palavra.upper()), end="")
    for letra in palavra:
        if letra.lower() in "aeiou":
            print(letra, end=" ")
