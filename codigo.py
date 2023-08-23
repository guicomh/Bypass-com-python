import os 

os.system("Title Bypass.gui")

temp = input("Apagar arquivos do seu computador? (y/n) >")

if temp == 'y':

# apagando arquivos temporarios e recents 
    os.system("rd /q %temp%")
    os.system("RD/s/q Recent")

# apagando a pasta mods fivem
    os.system("cd C:\Users\elise\AppData\Local\FiveM\FiveM.app")
    os.system("RD/s/q mods")

    


if temp == 'n':

    print("ok")
    os.system("pause")   


os.system("pause");


  