# r - leitura
# w - escrita, apaga o conteudo se ja existir
# a - escrita, mas preserva o conteudo se ja existir
# b - modo binario
# + - atualizacao (leitura e escrita)

arquivo = open("Aula 01 - numeros.txt", "w")  # utilizamos a funcao open para abrir Aula 01 - numeros.txt, o modo
# escolhido foi w

for linha in range(1, 101):  # criamos um laco para gerar numeros das linhas
    arquivo.write("{}\n".format(linha))  # escrevemos o numero da linha no arquivo, usando o metodo write

arquivo.close()  # fecha o arquivo
