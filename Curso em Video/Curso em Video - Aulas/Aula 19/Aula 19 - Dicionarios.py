estado = {}
brasil = []
for c in range(0, 3):
    estado["uf"] = str(input("Unidade Federativa: "))
    estado["sigla"] = str(input("Sigla do Estdo: "))
    brasil.append(estado.copy())
print(brasil)
