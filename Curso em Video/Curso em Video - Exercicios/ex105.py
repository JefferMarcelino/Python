"""ex105 - Analisando e gerando Dicionarios
Faca um programa que tenha uma funcao funcao notas() que pode receber varias
notas de alunos e vai retornar um dicionario com as seguintes informacoes:
- Quantidade de notas
- A maior nota
- A menor nota
- A media do aluno
- A situcao(opcional)
Adicione tambem as Docstrings"""


def notas(*nota, sit=False):
    """
    -> Funcao para analisar notas e situacoes de varios alunos.
    :param nota: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou nao adicionar a situcao
    :return: dicionario com varias informacoes sobre a situacao da turma
    """
    dic = {}
    testes = total = maior = menor = 0
    for n in nota:
        testes += n
        total += 1
        if total == 1:
            menor = n
            maior = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
    media = testes / total
    dic["total"] = total
    dic["maior"] = maior
    dic["menor"] = menor
    dic["media"] = media
    if sit:
        if media < 4:
            dic["situacao"] = "RUIM"
        if 7 > media > 4:
            dic["situacao"] = "RAZOAVEL"
        if media > 7:
            dic["situacao"] = "BOA"
    return dic


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)
