import os 

os.system("Title Bypassgui")

temp = input("Apagar arquivos do seu computador? (y/n) >")

if temp == 'y':

# apagando arquivos temporarios
    os.system("rd/s/q %temp%")
    os.system("RD/s/q Recent")

# apagando pasta mods fivem
    os.system("cd AppData\Local\FiveM\FiveM.app")
    os.system("RD/s/q mods")

if temp == 'n':

    print("ok")
    os.system("pause")   


os.system("pause")


  
