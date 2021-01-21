from time import sleep
import os
from datetime import datetime
import sys
from tkinter import *

arq = "dados.txt"


def bt_click():
    while True:
        try:
            t = int(ed.get())
        except:
            lb1["text"] = "ERRO. Por favor, digite um numero valido!"
            sleep(1.5)
            sys.exit()
        else:
            break
    if int(ed.get()) <= 0 or int(ed.get()) >= 61:
        lb1["text"] = "ERRO! Tente um número entre 0 a 60"
    else:
        if int(ed.get()) <= 1:
           lb1["text"] = "O seu Computador será desligado em {} segundo".format(int(ed.get())) 
        else:
            lb1["text"] = "O seu Computador será desligado em {} segundos".format(int(ed.get()))
        global temp
        temp = int(ed.get())
        os.system("shutdown -s -f -t {}".format(int(ed.get())))


janelaP = Tk()
#LxA+E+T

janelaP.geometry("500x200")
janelaP.title("DEFINIR PROGRAMA DESLIGAR")
janelaP["bg"] = "sky blue"

lb = Label(janelaP, text="Quantos Segundos voçe quer: ", font="12")
lb.place(x=0, y=0)
lb["bg"] = "sky blue"

lb1 = Label(janelaP, text="", font="14")
lb1.place(x=0, y=175)
lb1["bg"] = "sky blue"

ed = Entry(janelaP, width=30)
ed.place(x=220, y=2)

bt = Button(janelaP, width=15, text="ENVIAR", font="16", command=bt_click)
bt.place(x=310, y=140)

janelaP.mainloop()

try:
    dado = open(arq, "a")
except:
    dado = open(arq, "w")

dado.write("------> Dia = {}\n".format(datetime.today().date()))
dado.write("Horas = {}\n".format(datetime.today().time()))
dado.write("Tempo agendando: {} Segundos\n".format(temp))
dado.write("*\n")
dado.write("*\n")
dado.write("*\n")
dado.write("*\n")
