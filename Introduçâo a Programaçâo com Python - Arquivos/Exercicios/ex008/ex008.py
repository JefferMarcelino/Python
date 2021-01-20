"""
Modifique o programa anterior para tambem receber o numero de
caracteres por linha e o numero de paginas por folha pela linha
de comando.
"""

arq = str(input("Digite o nome do arquivo(inclua o extensao do formato): "))

book = open(arq)
book_formated = open("ex008 - book_formated.txt", "w")

limite_caracteres = int(input("Digite o limete de caracteres por linha: "))
limite_caracteres_temp = limite_caracteres - 1
limite_linhas = int(input("Digite o limite de linhas por pagina: "))
limite_caracteres -= 1
limite_linhas -= 1

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
            contador += limite_caracteres_temp
            limite_caracteres += limite_caracteres_temp
            if limite_caracteres > len(linha):
                book_formated.write(linha[contador:])
                book_formated.write("\n")
                linhas += 1
                contador = 0
                limite_caracteres = limite_caracteres_temp
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
