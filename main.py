from sqlite3 import connect
from tkinter import*
import os
import serial
port ="/dev/ttyUSB0"
#fenetre principale
screen = Tk()
screen.title("BMW M1 #1 telemetrie")
screen.minsize(1100,500)
screen.bg = "white"
screen.iconphoto(False,PhotoImage(file='image/bmw.png'))
#Connextion serie
ConnectSerial = Toplevel()
ConnectSerial.iconphoto(False,PhotoImage(file='image/bmw.png'))
ConnectSerial.title("Connextion a l'arduino")
ConnectSerial.minsize(500,500)
ConnectSerial.minsize(500,500)
Titre = Label(ConnectSerial,text="Connextion",font=("arial",30)).pack()
entry = Entry(ConnectSerial,width=20).pack()
def Valider(port):
    port = entry.get()
    return port
BoutonValider = Button(ConnectSerial,text="Valider",bg="green").pack()
#varriable
VarBoucle = 0
Telementrie = serial.Serial(port,9600,timeout=1)
#fonction
def VerificationConnextion():
    print("Votre arduino et connecter sur : ")
    print(Telementrie.name())

#mise en place de l'image central
IMGNORMAL1 = PhotoImage(file="image/normal1.png")
IMGNORMAL2 = PhotoImage(file="image/normal2.png")
IMGCHAUD = PhotoImage(file="image/chaud.png")
IMGFROID = PhotoImage(file="image/froid.png")
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
LabelTitre1 = Label(Cadreright,text="Batterie   ",bg="blue",fg="white",font=("arial",30))
LabelTemp = Label(CadreLeft)
LabelBat = Label(Cadreright)
LabelEcartG1 = Label(CadreLeft,height="17",width="10",bg="blue")
LabelAffichageG = Label(CadreLeft,width="10",height="2")
LabelEcartG2 = Label(CadreLeft,height="8",width="10",bg="blue")
LabelImageG = Label(CadreLeft,image=IMGNORMAL1,bg="blue")
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
    Telementrie.open()
    while VarBoucle == 1:
        serialdata = Telementrie.readline()
        print(serialdata)

 #Menu
configMenu = Menu(screen,bg="grey",fg="white")
Option = Menu(configMenu,tearoff=0)
StartStop = Menu(configMenu,tearoff=0)
Option.add_command(label="Verification de la connextion",command=VerificationConnextion)
Option.add_command(label="Configuration baterie")
Option.add_command(label="Configuration temperature")
StartStop.add_command(label="Start",command=CommandStart)
StartStop.add_command(label="Stop")
configMenu.add_cascade(label="Configuration",menu=Option)
configMenu.add_cascade(label="On off",menu=StartStop)
screen.config(menu=configMenu) 

#affichage
CadreLeft.pack(side="left")
Cadreright.pack(side="right")
labelImage.pack()
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