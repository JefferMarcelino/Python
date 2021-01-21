from datetime import datetime
import os
import sys

sys.path.append("C:\Data")

arq = "C:\Data\dados.txt"
password = "C:\Data\password.txt"

dado1 = open(password, "w")
dado1.write("The Computer was turned on, and someone has invaded! \n")
dado1.write("--> Time = {}\n".format(datetime.today().time()))
dado1.close()

senha = str(input("Digite a senha: "))
if senha == "jeffer2006":
    dado1 = open(password, "r")
    for data in dado1.readline():
        if data == "T":
            dado1.close()
            dado1 = open(password, "w")
            dado1.write("Clear! \n")
    invader = 0
else:
    invader = 1
try:
    dado = open(arq, "a")
except:
    dado = open(arq, "w")

dado.write("The Computer was turned on: \n")
dado.write("--> Time = {}\n".format(datetime.today().time()))
dado.write("--> Day = {}\n".format(datetime.today().date()))

if invader == 1:
    dado.write("Someone has invaded! \n")

dado.write("\n")
dado.write("\n")

dado.close()
dado1.close()

# Jeffer Marcelino