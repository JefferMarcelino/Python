import os
from tkinter import *


def bt_click_sim():
    os.system("shutdown -a")
    lb1.place(x=140, y=75)


janelaP = Tk()
#LxA+E+T

janelaP.geometry("500x200")
janelaP.title("DEFINIR PROGRAMA DESLIGAR")
janelaP["bg"] = "sky blue"

lb = Label(janelaP, text="TEM CERTEZA QUE QUER ANULAR O AGENDAMENTO?")
lb.place(x=0, y=0)
lb["bg"] = "sky blue"

lb1 = Label(janelaP, text="AGENDAMENTO CANCELADO!", font="25")
lb1["bg"] = "sky blue"

bt = Button(janelaP, width=10, text="SIM", font="30", command=bt_click_sim)
bt.place(x=200, y=140)


janelaP.mainloop()
