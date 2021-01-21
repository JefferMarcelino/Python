import Contador_V2

while True:
    dias = int(input("Quantos dias são? "))
    temp = dias
    print("{} dias são: ".format(dias))
    quant = 0
    if dias >= 30:
        while True:
            dias -= 30
            quant += 1
            if dias < 29:
                break
    Contador_V2.contador(3)
    print("> {} dias sao:".format(temp))
    print(">>> {} Mese(s)".format(quant))
    if dias // 7 >= 0:
        print(">>> {} Semana(s)".format(dias // 7))
    print(">>> E Restam {} Dia(s)".format(dias % 7))
    while True:
        resp = str(input("Quer continuar? [S/N] ")).upper()[0]
        if resp in "NS":
            break
        else:
            print("INVALIDO")
    if resp == "N":
        break
    print("-=" * 30)
print("\n>>> VOLTE SEMPRE <<<")
