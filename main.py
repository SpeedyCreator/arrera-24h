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
IMGGOOD = PhotoImage(file="image/good.png")
IMGBAD = PhotoImage(file="image/bad.png")
IMG100 = PhotoImage(file="image/100%.png")
IMG80 = PhotoImage(file="image/80%.png")
IMG60 = PhotoImage(file="image/60%.png")
IMG40 = PhotoImage(file="image/40%.png")
IMG20 = PhotoImage(file="image/20%.png")
IMG0 = PhotoImage(file="image/0.png")
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
LabelEcartG1 = Label(CadreLeft,height="17",width="10",bg="blue")
LabelAffichageG = Label(CadreLeft,width="10",height="2")
LabelEcartG2 = Label(CadreLeft,height="8",width="10",bg="blue")
LabelImageG = Label(CadreLeft,image=IMGGOOD,bg="blue")
LabelEcartG3 = Label(CadreLeft,height="4",width="10",bg="blue")

LabelEcartD1 = Label(Cadreright,height="6",width="10",bg="blue")
LabelTextD1 = Label(Cadreright,text="Tension de la batterie",fg="white",bg="blue")
LabelAffichageD1 = Label(Cadreright,width="10",height="2")
LabelEcartD2 = Label(Cadreright,height="8",width="10",bg="blue")
LabelTextD2 = Label(Cadreright,text="Pourcentage",fg="white",bg="blue")
LabelAffichageD2 = Label(Cadreright,width="10",height="2")
LabelEcartD3 = Label(Cadreright,bg="blue",height="8",width="10")
LabelImageD = Label(Cadreright,image=IMG100,bg="blue")
LabelEcartD4 = Label(Cadreright,bg="blue",height="4",width="10")
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
#Zone tension
LabelEcartD1.pack()
LabelTextD1.pack()
LabelAffichageD1.pack()
LabelEcartD2.pack()
LabelTextD2.pack()
LabelAffichageD2.pack()
LabelEcartD3.pack()
LabelImageD.pack()
LabelEcartD4.pack()
#Zone temperature
LabelEcartG1.pack()
LabelAffichageG.pack()
LabelEcartG2.pack()
LabelImageG.pack()
LabelEcartG3.pack()

screen.mainloop()