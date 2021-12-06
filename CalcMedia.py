print("-=" * 30)
print("Calculo de media")
print("-=" * 30)

n_provas = int(input("Quantas provas foram realizadas? "))
notas = 0

for vezes in range(0, n_provas):
    while True:
        nota = float(input(f"Digite a nota da {vezes + 1}ª prova: "))
        if nota > 20 or nota < 0:
            print("ERRO! ", end="")
        else:
            notas += nota
            break

media = notas / n_provas
print(f"Foram realizadas {n_provas}.")
print(f"A média é {media:.2f}.")