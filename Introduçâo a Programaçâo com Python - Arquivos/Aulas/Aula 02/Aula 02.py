# r - leitura
# w - escrita, apaga o conteudo se ja existir
# a - escrita, mas preserva o conteudo se ja existir
# b - modo binario
# + - atualizacao (leitura e escrita)

arquivo = open("../Aula 01/Aula 01 - numeros.txt", "r")  # utilizamos a funcao open para abrir o arquivo, o modo escolhido foi r

for linha in arquivo.readlines():  # utilizamos o metodo readlines, que gera uma lista em que cada elemento é uma
    # linha do arquivo
    print(linha)  # simplesmente imprimimos a linha na tela

arquivo.close()  # fechamos o arquivo
