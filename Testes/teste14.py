class Aluno:
    def __init__(self, nome=None, classe=None, idade=None, *notas):
        self.nome = nome
        self.classe = classe
        self.idade = idade
        self.notas = notas

    def __str__(self):
        return "None"

    def calcula_media(self):
        if self.notas is not None:
            n = 0
            n_provas = 0
            for nota in self.notas:
                n += nota
                n_provas += 1
            media = n / n_provas
            return media
    

jeffer = Aluno("Jeffer", 9, 14)
print(jeffer.notas)
print(jeffer.calcula_media())

