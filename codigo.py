import os
from tkinter import *
from tkinter import ttk

def apagar_tudo():

    os.system("rd/s/q %temp%")
    os.system("RD/s/q Recent")
    os.system("cd .. && cd .. && cd ..  &&cd AppData\Local\FiveM\FiveM.app && rd/s/q mods")
    os.system("cd .. && cd .. && cd ..  &&cd AppData\Local\FiveM\FiveM.app && rd/s/q logs ")  

def fivem_a():

    os.system("cd .. && cd .. &&cd ..  &&cd AppData\Local\FiveM\FiveM.app\data  && rd/s/q cache && rd/s/q nui-storage && rd/s/q server-cache &&  rd/s/q server-cache-priv ")
    

janela = Tk()

janela.iconbitmap("icone.ico")

janela.title("Bypass do Gui")
janela.geometry("300x200")

texto = Label(janela, text="Limpar Fivem")
texto.grid(column=0, row=0, padx=130, pady=1)

botao = Button(janela, text="Apagar", command=apagar_tudo)
botao.grid(column=0, row=1, padx=10, pady=10)

botao_limpeza = Button(janela, text='Apagar Cache', command=fivem_a)
botao_limpeza.grid(column=0 , row=2, padx=15, pady=15)

botao_kendra = Button(janela, text='Fechar', command=janela.destroy)
botao_kendra.grid(column=0, row=3, padx=20, pady=20)


janela.mainloop()
