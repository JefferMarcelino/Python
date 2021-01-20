try:
    a = int(input("Primeiro numero: "))
    b = int(input("Segundo numero: "))
    r = a / b
except (ValueError, TypeError):
    print("Problema encontrado foi com os tipos de dados que voce digitou.")
except ZeroDivisionError:
    print("Nao é possivel dividir um numero por 0!")
except KeyboardInterrupt:
    print("O usario preferiu nao informar os dados")
else:
    print("O resultado e {:.1f}".format(r))
finally:
    print("Volte Sempre! Muito Obrigado :)")
