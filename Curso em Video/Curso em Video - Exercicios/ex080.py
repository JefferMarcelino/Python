"""ex080 - Lista ordenada sem repeticoes
Crie um programa onde o usario possa digitar 5 valores numericos e cadastre-os em
uma lista, ja na posicao correcta de insercao(sem usar o sort()). No final, mostre
a lista ordenada na tela."""

lista = []
for c in range(0, 5):
    n = int(input("Digite um valor: "))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print("Adicionado ao final da lista...")
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print("Adicionado na posicao {} da lista".format(pos))
                break
            pos += 1
print("-=" * 30)
print("Os valores digitados em ordem foram {}".format(lista))
