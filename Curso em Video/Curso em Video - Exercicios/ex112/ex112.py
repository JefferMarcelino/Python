"""""ex110 - Transformando mosulos em pacotes"""


from utilidadescev import moeda
from utilidadescev import dado

preco = dado.leiaDinheiro("Digite o preco: ")
moeda.resumo(preco, 35, 22)
