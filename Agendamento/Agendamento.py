from tkinter import *
import os
from time import sleep
from datetime import datetime
import sys

janela_principal = Tk()

arq = "dados.txt"
valor = 1


def bt_click1():
    global valor
    valor = 1


def bt_click2():
    global valor
    valor = 60


def bt_click3():
    while True:
        try:
            t = int(ed1.get())
        except:
            lb2["text"] = "ERRO. Por favor, digite um numero valido!"
            sleep(1.5)
            sys.exit()
        else:
            break
    tempo = valor * 60 * int(ed1.get())
    lb2["text"] = "Seu computador sera desligado em {} segundos".format(tempo)
    os.system("shutdown -s -f -t {}".format(tempo))
    global temp
    temp = tempo


def bt_click4():
    os.system("shutdown -a")
    lb2["text"] = "Agedando o Cancelamento, com Sucesso"
    sleep(1.5)
    sys.exit()


def bt_click5():
    os.system("shutdown -s -f")


janela_principal.geometry("450x200")
janela_principal["bg"] = "sky blue"
janela_principal.title("Agendamento")

lb1 = Label(janela_principal, text="ESCOLHA UMA OPCAO: ", font="14")
lb1.place(x=0, y=0)
lb1["bg"] = "sky blue"

lb2 = Label(janela_principal, text="", font="18")
lb2.place(x=0, y=115)
lb2["bg"] = "sky blue"

bt1 = Button(janela_principal, text="MINUTOS", width=10, font=20, command=bt_click1)
bt1.place(x=0, y=30)
bt1["bg"] = "powder blue"

bt2 = Button(janela_principal, text="HORAS", width=10, font=20, command=bt_click2)
bt2.place(x=0, y=65)
bt2["bg"] = "powder blue"

ed1 = Entry(janela_principal, width=40)
ed1.place(x=150, y=75)

bt3 = Button(janela_principal, text="ENVIAR", width=10, font=20, command=bt_click3)
bt3.place(x=210, y=150)
bt3["bg"] = "powder blue"

bt4 = Button(janela_principal, text="CANCELAR", width=15, font=30, command=bt_click4)
bt4.place(x=50, y=150)
bt4["bg"] = "powder blue"

bt5 = Button(janela_principal, text="DESLIGAR", width=10, font=30, command=bt_click5)
bt5.place(x=325, y=150)
bt5["bg"] = "powder blue"

janela_principal.mainloop()

try:
    dado = open(arq, "a")
except:
    dado = open(arq, "w")


dado.write("---------> Dia = {} <---------\n".format(datetime.today().date()))
dado.write("--> Horas = {}\n".format(datetime.today().time()))
if valor == 1:
    dado.write("--> Tempo agendando: {} Minutos\n".format(temp / 60 / valor))
elif valor == 60:
    dado.write("--> Tempo agendando: {} Horas\n".format(temp / 60 / valor))
dado.write("-=" * 30)
dado.write("\n")
