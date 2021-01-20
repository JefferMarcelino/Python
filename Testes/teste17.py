import math
from random import randint

print("-=" * 30)
print("""Escolha uma disciplina:
[ 1 ] Matematica
[ 2 ] Portugues 
[ 3 ] Geografia
[ 4 ] Fisica
[ 5 ] Todas disciplinas""")

while True:
    opc = str(input(">>> "))
    try:
        opc = int(opc)
    except ValueError:
        print("Erro! Por favor, digite um numero valido!")
        break
    if 6 > int(opc) > 0:
        break
    print("Invalido!")
