while True:
    
    tot = 0
    quantcopias = int(input("Digite a quantidade de copias normais: "))
    quantcopiasverso = int(input("Digite a quantidade de copias com versos: "))
    print("-=" * 30)
    if quantcopias > 0:
        print("{} copias normais são {} MT".format(quantcopias, quantcopias * 1.5))
        tot += quantcopias * 1.5
    if quantcopiasverso > 0:
        print("{} copias com verso são {} MT".format(quantcopiasverso, quantcopiasverso * 3))
        tot += quantcopiasverso * 3
    print("-=" * 30)
    print("Total é {} MT".format(tot))
    print("-=" * 30)
    while True:
        resp = str(input("Quer Continuar? [S/N] ")).upper()[0]
        if resp in "SN":
            break
        else:
            print("INVALIDO!", end="")
    if resp == "N":
        break
    
print("<<< VOLTE SEMPRE>>>")
