"""
Crie um programa que leia um arquivo-texto e gere um arquivo de
saida paginado. Cada linha nao deve conter mais de 76 caracteres.
Cada pagina tera no maximo 60 linhas. Adicione na ultima linha de
cada pagina o numero da pagina atual e nome do arquivo original.
"""

arq = str(input("Digite o nome do arquivo(inclua o extensao do formato): "))

book = open(arq)
book_formated = open("ex007 - book_formated.txt", "w")

limite_caracteres = 75
limite_caracteres_temp = 75
limite_linhas = 60

linhas = 0
paginas = 0
contador = 0

for linha in book.readlines():
    tam = len(linha) // 2
    if len(linha) >= limite_caracteres_temp:
        while True:
            book_formated.write(linha[contador:limite_caracteres])
            book_formated.write("\n")
            linhas += 1
            contador += 75
            limite_caracteres += 75
            if limite_caracteres > len(linha):
                book_formated.write(linha[contador:])
                book_formated.write("\n")
                linhas += 1
                contador = 0
                limite_caracteres = 75
                break

    else:
        book_formated.write(linha)
        book_formated.write("\n")
        linhas += 1

    if linhas >= limite_linhas:
        linhas = 0
        paginas += 1
        book_formated.write("{} -> {}".format(str(paginas), arq.replace(".txt", "")))
        book_formated.write("\n")
        book_formated.write("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        book_formated.write("\n")

book.close()
book_formated.close()
