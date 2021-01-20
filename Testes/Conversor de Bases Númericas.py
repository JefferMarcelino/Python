"""Conversor de Bases Númericas"""

conv = []
num = int(input("Digite um número para converter: "))
vdd = []
n = 1

while True:
    div = num % 2
    num = num // 2

    conv.append(div)
    if num == 0:
        break

for c in range(0, len(conv)):
    vdd.append(conv[-n])
    n = n + 1

print("Convertendo para binario e: ", end="")
for c in vdd:
    print(c, end="")
