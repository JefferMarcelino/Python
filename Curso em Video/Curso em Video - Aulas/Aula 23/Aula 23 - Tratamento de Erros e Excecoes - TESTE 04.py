try:
    a = int(input("Primeiro numero: "))
    b = int(input("Segundo numero: "))
    r = a / b
except Exception as erro:
    print("Problema encontrado foi {}".format(erro.__class__))
else:
    print("O resultado e {:.1f}".format(r))
finally:
    print("Volte Sempre! Muito Obrigado :)")
