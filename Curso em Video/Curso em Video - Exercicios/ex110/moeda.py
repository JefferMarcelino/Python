def aumentar(preco=0, taxa=0, formatado=False):
    res = preco + (preco * taxa / 100)
    return res if formatado is False else moeda(res)


def diminuir(preco=0, taxa=0, formatado=False):
    res = preco - (preco * taxa / 100)
    return res if formatado is False else moeda(res)


def dobro(preco=0, formatado=False):
    res = preco * 2
    return res if formatado is False else moeda(res)


def metade(preco=0, formatado=False):
    res = preco / 2
    return res if formatado is False else moeda(res)


def moeda(preco=0, moeda="MTs"):
    return f"{preco:.2f}{moeda}".replace(".", ",")


def resumo(p=0, taxaa=10, taxar=5):
    print("-" * 30)
    print("RESUMO DO VALOR".center(30))
    print("-" * 30)
    print("Preco analisado: \t\t{}".format(moeda(p)))
    print("Dobro do preco: \t\t{}".format(dobro(p, True)))
    print("Metade do preco: \t\t{}".format(metade(p, True)))
    print("Com {}% de aumento: \t{}".format(taxaa, aumentar(p, taxaa, True)))
    print("Com {}% de reducao: \t{}".format(taxar, diminuir(p, taxar, True)))
    print("-" * 30)
