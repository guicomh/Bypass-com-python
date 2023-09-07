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

def abrir_fivem():

    os.system("cd .. && cd .. &&cd ..  &&cd AppData\Local\FiveM && start FiveM.exe") 

    

janela = Tk()

janela.iconbitmap("icone.ico")

janela.title("Limpeza")
janela.geometry("300x200")

texto = Label(janela, text="Limpar") . pack()


botao = Button(janela, text="Apagar", command=apagar_tudo) . pack()


botao_limpeza = Button(janela, text='Cache', command=fivem_a) . pack()


botao_kendra = Button(janela, text='FiveM', command=abrir_fivem) . pack()



janela.mainloop()
