from ex155.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("Houve um ERRO na Criacao do Arquivo!")
    else:
        print("Arquivo {} criado com sucesso!".format(nome))


def lerArquivo(nome):
    try:
        a = open(nome, "rt")
    except:
        print("Erro ao ler o arquivo!")
    else:
        cabecalho("PESSOAS CADASTRADAS")
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print("{:<30} {:>3} anos".format(dado[0], dado[1]))
    finally:
        a.close()


def cadastrar(arq, nome="desconhecido", idade=0):
    try:
        a = open(arq, "at")
    except:
        print("Houve um ERRO na abertura do arquivo!")
    else:
        try:
            a.write("{};{}\n".format(nome, idade))
        except:
            print("Houve um ERRO na hora de escrever os dados!")
        else:
            print("Novo registo de {} adicionado!".format(nome))
            a.close()

