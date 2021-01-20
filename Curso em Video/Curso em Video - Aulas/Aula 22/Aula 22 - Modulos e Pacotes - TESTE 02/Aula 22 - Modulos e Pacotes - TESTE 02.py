from uteiss import numeros

num = int(input("Digite um numero: "))
fat = numeros.fatorial(num)
print("O factorial de {} e {}".format(num, fat))
print("O dobro de {} e {}".format(num, numeros.dobro(num)))
