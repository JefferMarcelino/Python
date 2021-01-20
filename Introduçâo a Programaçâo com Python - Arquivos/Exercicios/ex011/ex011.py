"""
Altere o programa para exibir o tamanho da agenda no menu principal.
"""

agenda = []


def pede_nome():
    return input("Nome: ")


def pede_telefone():
    return input("Telefone: ")


def mostra_dados(nome, telefone):
    print("Nome: {} Telefone: {}".format(nome, telefone))


def pede_nome_arquivo():
    return input("Nome do Arquivo: ")


def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None


def novo():
    global agenda
    nome = pede_nome()
    telefone = pede_telefone()
    agenda.append([nome, telefone])


def apaga():
    global agenda
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:
        del agenda[p]
    else:
        print("Nome nao encontrado!")


def altera():
    p = pesquisa(pede_nome())
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print("Encontrado:")
        mostra_dados(nome, telefone)
        nome = pede_nome()
        telefone = pede_telefone()
        agenda[p] = [nome, telefone]
    else:
        print("Nome nao encontrado!")


def lista():
    print("\nAgenda\n\n-------------------------------------------")
    for e in agenda:
        mostra_dados(e[0], e[1])
    print("-------------------------------------------\n")


def leia():
    global agenda
    nome_arquivo = pede_nome_arquivo()
    arquivo = open(nome_arquivo, "r", encoding="utf-8")
    agenda = []
    for l in arquivo.readlines():
        nome, telefone = l.strip().split("#")
        agenda.append([nome, telefone])
    arquivo.close()


def grava():
    nome_arquivo = pede_nome_arquivo()
    arquivo = open(nome_arquivo, "w", encoding="utf-8")
    for e in agenda:
        arquivo.write("{}#{}\n".format(e[0], e[1]))
    arquivo.close()


def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print("Valor Invalido, favor digitar entre {} e {}".format(inicio, fim))


def menu():
    print("""
    A lista contem dados de {} pessoa(s)
    
    1 - Novo
    2 - Altera
    3 - Apaga
    4 - Lista
    5 - Grava
    6 - Le
    
    0 - Sai
    """.format(len(agenda)))
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 6)


while True:
    opção = menu()
    if opção == 0:
        break
    elif opção == 1:
        novo()
    elif opção == 2:
        altera()
    elif opção == 3:
        apaga()
    elif opção == 4:
        lista()
    elif opção == 5:
        grava()
    elif opção == 6:
        leia()
