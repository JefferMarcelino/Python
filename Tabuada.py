from random import randint

print("\033[35mTABUADA\033[m")
print("-=" * 30)

while True:
    n = str(input("Digite um número(Digite 0 para escolher um número aleatório): "))
    if n == "0":
        n = randint(1, 999)
        break
    try:
        if int(n): 
            n = int(n)
            break
    except:
        print("Por favor, digite um número válido!")


print(f"TABUADA DE {n}")

for c in range(1, 1000):
    print("{} x {:3} = {}".format(n, c, n*c))
