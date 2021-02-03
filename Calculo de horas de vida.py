from datetime import datetime

print("Calculo de Horas de vida")
print("-=" * 15)

ano_nasc = int(input("Digite o seu ano de nascimento: "))
ano_actual = int(input("Digite o ano actual (999 para pegar o ano do Computador): "))
if ano_actual == 999:
    ano_actual = datetime.today().year
print(ano_nasc)
print(ano_actual)