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
