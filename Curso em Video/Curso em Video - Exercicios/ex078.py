"""ex078 - Maior e Menor Valores na Lista
Faca um programa que leia 5 valores numericas e guarde-os em uma lista. No
final, mostre qual foi o maior e o menor valor digitado e as suas respectivas
posicoes na lista."""

valores = []
maior = 0
menor = 0
for c in range(0, 5):
    valores.append(int(input("Digite um valor para a Posicao {}: ".format(c))))
    if c == 0:
        maior = valores[c]
        menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        elif valores[c] < menor:
            menor = valores[c]

print("-=" * 30)
print("Voce digitou os valores {}".format(valores))
print("O Maior valor digitado foi {} nas posicoes ".format(maior), end="")
for i, v in enumerate(valores):
    if v == maior:
        print(f"{i}...", end="")
print("\nO menor valor digitado foi {} nas posicoes ".format(menor), end="")
for i, v in enumerate(valores):
    if v == menor:
        print(f"{i}...", end="")
