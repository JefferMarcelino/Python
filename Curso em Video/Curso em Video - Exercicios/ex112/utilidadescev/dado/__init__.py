def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).strip().replace(",", ".")
        if entrada.isalpha() or entrada == "":
            print("\033[31mERRO! \"{}\" é um preco invalido\033[m".format(entrada))
        else:
            valido = True
            return float(entrada)
