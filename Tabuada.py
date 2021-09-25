from random import randint

print("\033[35mTABUADA\033[m")
print("\033[34m-=\033[m" * 30)

while True:
    n = str(input("\033[36mDigite um número(Digite 0 para escolher um número aleatório): \033[m"))
    if n == "0":
        n = randint(1, 999)
        break
    try:
        if int(n): 
            n = int(n)
            break
    except:
        print("Por favor, digite um número válido!")

print("-=" * 13)
print(f"\033[35m    -> TABUADA DE {n}\033[m")
print("-=" * 13)
for c in range(1, 11):
    print("\033[33m{} x {:2} = {}\033[m".format(n, c, n*c))
