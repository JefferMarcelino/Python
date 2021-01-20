import uteis


# PROGRAMA PRINCIPAL
num = int(input("Digite um valor: "))
fat = uteis.fatorial(num)
print("O fatorial de {} e {}".format(num, fat))
print("O dobro de {} e {}".format(num, uteis.dobro(num)))
