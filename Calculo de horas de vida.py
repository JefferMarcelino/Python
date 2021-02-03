from datetime import datetime

print("Calculo de Horas de vida")
print("-=" * 15)

ano_nasc = int(input("Digite o seu ano de nascimento: "))
ano_actual = int(input("Digite o ano actual (999 para pegar o ano do Computador): "))

if ano_actual == 999:
    ano_actual = datetime.today().year

idade = ano_actual - ano_nasc
dias = idade * 365
horas = dias * 24
minutos = horas * 60

print("-=" * 15)
print("De acordo com os dados inseridos voce tem aproximadamente: ")
print("     -> {} ano(s) de vida.".format(idade))
print("     -> {} dia(s) de vida.".format(dias))
print("     -> {} hora(s) de vida.".format(horas))
print("     -> {} minuto(s) de vida.".format(minutos))