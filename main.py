from tkinter import*
import os
import serial
#fenetre principale
screen = Tk()
screen.title("BMW M1 #1 telemetrie")
screen.minsize(1100,500)
screen.bg = "white"
screen.iconphoto(False,PhotoImage(file='image/bmw.png'))
#varriable
VarBoucle = 0
Telemetrie = serial.Serial()
#fonction
def ConfigSerial():
    print("Ou es connecter votre arduino ?")
    Connexion = input("Emplacement de connextion: ")
    Connexion = str(Connexion)
    Telementrie = serial.Serial(Connexion,9600)
#Menu
configMenu = Menu(screen,bg="grey",fg="white")
Option = Menu(configMenu,tearoff=0)
Option.add_command(label="Connexion serie",command=ConfigSerial)
Option.add_command(label="Config baterie")
configMenu.add_cascade(label="Configuration",menu=Option)
screen.config(menu=configMenu)
#mise en place de l'image central
IMGcentral = PhotoImage(file="image/image.png")
labelImage = Label(image=IMGcentral)
#creation des deux cadre
CadreLeft= Frame(screen,width=300,height=800,bg="blue")
Cadreright= Frame(screen,width=300,height=800,bg="blue")

#mise en forme des cadre:
LabelTitre2 = Label(CadreLeft, text="Temperature",bg="blue",fg="white",font=("arial",30))
LabelTitre1 = Label(Cadreright,text="  Batterie ",bg="blue",fg="white",font=("arial",30))
LabelTemp = Label(CadreLeft)
LabelBat = Label(Cadreright)
LabelEcartG = Label(CadreLeft,height="35",width="10",bg="blue")
LabelEcartD = Label(Cadreright,height="35",width="10",bg="blue")
#Bouton
def CommandStart():
    BoutonStart.destroy()
    def Stop(Value):
        global VarBoucle
        VarBoucle = Value
    
    BoutonStop =  Button(screen,text="  Arret ",bg="red",command=lambda *arg :Stop(0)).pack()
    
    while VarBoucle == 1:
        serialdata = Telemetrie.readline()
        print(serialdata)
    print("fin")
    BoutonStart.pack()

BoutonStart = Button(screen,text="Demarage",command=CommandStart,bg="green")

#affichage
CadreLeft.pack(side="left")
Cadreright.pack(side="right")
labelImage.pack()
BoutonStart.pack()
LabelTitre2.pack()
LabelTitre1.pack()
#Zone temperature
LabelEcartG.pack()
LabelEcartD.pack()
#boucle

screen.mainloop()