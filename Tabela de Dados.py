dados = []
pessoas = []

while True:

    nome = str(input("\033[35mDigite o nome: \033[m")).title()

    while True:
        sexo = str(input("\033[35mDigite o sexo: \033[m")).upper()[0]
        if sexo in "FM":
            break
        else:
            print("\033[31mINVALIDO!\033[m")
    peso = float(input("\033[35mDigite o peso: \033[m"))
    altura = float(input("\033[35mDigite a altura: \033[m"))

    print("-" * 60)

    pessoas.append(nome)
    pessoas.append(sexo)
    pessoas.append(peso)
    pessoas.append(altura)
    dados.append(pessoas[:])
    pessoas.clear()

    while True:
        resp = str(input("Quer continuar? [S/N] ")).upper()[0]
        if resp in "NS":
            break
    if resp == "N":
        break

print("\033[34m+", "-" * 27, "+", "-" * 5, "+", "-" * 5, "+", "-" * 5, "+\033[m")
print("\033[34m|\033[m\033[34m{:<29}| {:<6}| {:<6}| {:<6}|\033[m".format("NOME", "SEXO", "PESO", "ALTURA"))
print("\033[34m+", "-" * 27, "+", "-" * 5, "+", "-" * 5, "+", "-" * 5, "+\033[m")

for dado in dados:
    print("\033[34m|\033[m\033[32m{:>29}\033[m\033[34m|\033[m \033[32m{:>6}\033[m\033[34m|\033[m \033[32m{:>6}\033["
          "m\033[34m|\033[ "
          "m\033[32m{:>7}\033[34m|\033[m".format(dado[0], dado[1], dado[2], dado[3]))
print("\033[34m+", "-" * 27, "+", "-" * 5, "+", "-" * 5, "+", "-" * 5, "+\033[m")
