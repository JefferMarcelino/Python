from ex155.lib.interface import *
from ex155.lib.arquivos import *
from time import sleep

arq = "cursoemvideo.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do Sistema"])
    if resp == 1:
        lerArquivo(arq)
    elif resp == 2:
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabecalho("Saindo do Sistema... Ate logo!")
        break
    else:
        print("\033[31mERRO! Digite uma opcao valida!\033[m")
    sleep(1)
