def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print("Somando os valores {} temos {}".format(valores, s))


# PROGRAMA PRINCIPAL
soma(5, 2)
soma(2, 9, 4)
