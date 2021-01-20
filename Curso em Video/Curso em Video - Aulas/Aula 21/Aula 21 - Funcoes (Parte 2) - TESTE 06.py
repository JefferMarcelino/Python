def parOuImpar(n=0):
    if n % 2 ==0:
        return True
    else:
        return False


num = int(input("Digite um numero: "))
if parOuImpar(num):
    print("E par!")
else:
    print("Nao e par!")
