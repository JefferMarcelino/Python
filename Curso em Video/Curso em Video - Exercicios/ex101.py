"""ex101 - Funcoes para votacao
Crie um programa que tenha uma funcao chamada voto() que vai receber como
parametro o ano de nascimento de uma pessoa, retornando um valor literal indicando
se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas elecoes."""


def vota(nascimento):
    from datetime import datetime
    ano = datetime.today().year
    idade = ano - nascimento
    if idade < 18:
        return f"Com {idade} anos: NAO VOTA"
    elif idade < 18 or idade < 65:
        return f"Com {idade} anos: VOTO OBRIGATORIO"
    else:
        return f"Com {idade} anos: VOTO OPCIONAL"


# PROGRAMA PRINCIPAL
nasc = int(input("Em que ano voce nasceu? "))
print(vota(nasc))
