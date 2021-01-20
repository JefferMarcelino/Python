def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            break
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um numero inteiro valido.\033[m")
            continue
    return n


def linha(tam=42):
    return "-" * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print("\033[33m{}\033[m - \033[34m{}\033[m".format(c, item))
        c += 1
    print(linha())
    opc = leiaInt("\033[32mSua Opcao > \033[m")
    return opc
