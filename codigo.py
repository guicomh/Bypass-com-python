import os
from tkinter import *
from tkinter import ttk

def apagar_tudo():

    os.system("rd/s/q %temp%")
    os.system("RD/s/q Recent")
    os.system("cd AppData\Local\FiveM\FiveM.app")
    os.system("rd/s/q mods")     
    

janela = Tk()

janela.title("Bypass do Gui")
janela.geometry("300x200")

texto = Label(janela, text="Bypass")
texto.grid(column=0, row=0, padx=130, pady=1)

botao = Button(janela, text="Apagar", command=apagar_tudo)
botao.grid(column=0, row=1, padx=10, pady=10)

botao_kendra = Button(janela, text='Fechar', command=janela.destroy)
botao_kendra.grid(column=0, row=2, padx=20, pady=20)


janela.mainloop()
