tribos = ["Gade", "Levi", "Juda", "Naftali",
         "Benjamim", "Zebulom", "Simião"]

nome = str(input("Qual e o teu nome: ")).title()
while True:
    tribo = str(input("Tribo na qual pertence:")).title()
    if tribo in tribos:
        break
    else:
        print("INVÁLIDO! ", end="")
while True:        
    batismo = str(input("É batizado/a nas aguas: [S/N]")).upper()[0]
    if batismo in "SN":
        break
    else:
        print("INVÁLIDO! ", end="")
    
if batismo == "S":
    batismo = "Sim"
elif batismo == "N":
    batismo = "Não"

while True:
    batistonoE = str(input("É batizado/a no Espirito Santo? [S/N]: ")).upper()[0]
    if batistonoE in "NS":
        break
    else:
        print("INVÁLIDO! ", end="")
        
if batistonoE == "S":
    batistonoE = "Sim"
elif batistonoE == "N":
    batistonoE = "Não"

ID = str(input("Digite seu numero de BI: "))

print("{:<30}{:<10}{:<10}{:<14}{:<15}".format("NOME", "TRIBO", "BATISMO", "BATISTONOE", "ID"))
print("-" * 80)
print("{:<30}{:<10}{:<10}{:<14}{:<15}".format(nome, tribo, batismo, batistonoE, ID))
