from tkinter import *

janela = Tk()

janela.geometry("400x300")

lb1 = Label(janela, text="Label 1")
lb2 = Label(janela, text="Label 2")
lb3 = Label(janela, text="ANCHOR 1")
lb4 = Label(janela, text="ANCHOR 2")

lb1.grid(row=10, column=10)
lb2.grid(row=11, column=16)

janela.mainloop()
