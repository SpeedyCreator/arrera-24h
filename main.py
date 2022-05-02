from tkinter import*
import os
import serial
import time
#varriable
VarBoucle = 0
port ="/dev/ttyUSB0"
color = "white"
TextColor = "black"
Tmax = 8.00
vide =""
#fonction de noitoiment des donnes
def nettoieTemp(L):
    temp=L[4:]
    NewL = temp[:-11]
    NewL = int(NewL)
    return NewL
def nettoieTension(L):
    temp=L[7:]
    NewL = temp[:-7]
    NewL = float(NewL)
    NewL = NewL / 100
    return NewL 

#fenetre principale
screen = Tk()
screen.title("BMW M1 #1 telemetrie")
screen.minsize(1100,500)
screen.config(bg = color)
screen.iconphoto(False,PhotoImage(file='image/bmw.png'))

#fonction
def VerificationConnextion():
    print("Votre arduino et connecter sur : ")
    print(port)

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
CadreLeft= Frame(screen,width=300,height=800,bg = color)
Cadreright= Frame(screen,width=300,height=800,bg = color)


LabelTitre2 = Label(CadreLeft, text="Temperature",width=10,font=("arial",30),bg = color ,fg = TextColor)
LabelTitre1 = Label(Cadreright,text="Batterie   ",width=10,font=("arial",30),bg = color,fg = TextColor)
LabelEcartG1 = Label(CadreLeft,height="17",width="10",bg = color)
LabelAffichageG = Label(CadreLeft,width="10",height="2")
LabelEcartG2 = Label(CadreLeft,height="8",width="10",bg = color)
LabelImageG = Label(CadreLeft,image=IMGNORMAL1,bg = color)
LabelEcartG3 = Label(CadreLeft,height="4",width="10",bg = color)

LabelEcartD1 = Label(Cadreright,height="6",width="10",bg = color)
LabelTextD1 = Label(Cadreright,text="Tension de la batterie",bg = color,fg = TextColor)
LabelAffichageD1 = Label(Cadreright,width="10",height="2")
LabelEcartD2 = Label(Cadreright,height="8",width="10",bg = color)
LabelTextD2 = Label(Cadreright,text="Pourcentage",bg = color,fg = TextColor)
LabelAffichageD2 = Label(Cadreright,width="10",height="2")
LabelEcartD3 = Label(Cadreright,height="8",width="10",bg = color)
LabelImageD = Label(Cadreright,image=IMG100,bg = "white")
LabelEcartD4 = Label(Cadreright,height="4",width="10",bg = color)

#affichage
def affichagePrincipal():
    CadreLeft.pack(side="left")
    Cadreright.pack(side="right")
    labelImage.pack()
    LabelTitre2.pack()
    LabelTitre1.pack()
def Affichagetension():
    LabelEcartD1.pack()
    LabelTextD1.pack()
    LabelAffichageD1.pack()
    LabelEcartD2.pack()
    LabelTextD2.pack()
    LabelAffichageD2.pack()
    LabelEcartD3.pack()
    LabelImageD.pack()
    LabelEcartD4.pack()
def AffichageTemp():
    LabelEcartG1.pack()
    LabelAffichageG.pack()
    LabelEcartG2.pack()
    LabelImageG.pack()
    LabelEcartG3.pack()

#Menu

def affichageValeur():
    Telementrie = serial.Serial(port,9600,timeout=1)
    serialdata = Telementrie.readline()
    rawdata1 = str(serialdata)
    print(rawdata1)
    temperature = nettoieTemp(rawdata1)
    tension = nettoieTension(rawdata1) 
    pourcentage = tension * 100 / Tmax
    pourcentageSTR = str(pourcentage)
    temperatureSTR1 =  str(temperature)
    TensionSTR1 = str(tension)
    LabelAffichageG['text'] = temperatureSTR1
    LabelAffichageD1['text'] = TensionSTR1
    LabelAffichageD2['text'] = pourcentageSTR
    if temperature >= 17 :
        LabelImageG['image'] = IMGFROID
    if temperature <= 17  and temperature >= 30 :
        LabelImageG['image'] = IMGNORMAL1
    if temperature <= 30 and temperature >= 45 :
        LabelImageG['image'] = IMGNORMAL2
    if temperature <= 45 : 
        LabelImageG['image'] = IMGCHAUD  
    
    if pourcentage >= 1:
        LabelImageD['image'] = IMG0
    if pourcentage <= 1 and pourcentage >= 19:
        LabelImageD['image'] = IMG20
    if pourcentage <= 20 and pourcentage >= 39:
        LabelImageD['image'] = IMG40   
    if pourcentage <= 40 and pourcentage >= 59:
        LabelImageD['image'] = IMG60
    if pourcentage <= 60 and pourcentage >= 79:
        LabelImageD['image'] = IMG80
    if pourcentage <= 80 and pourcentage >= 100:
        LabelImageD['image'] = IMG100
def CommandStart():
    VarBoucle =+1 
    while VarBoucle == 1 :
        affichageValeur()
        LabelAffichageD1.update()
        LabelAffichageD2.update()
        LabelAffichageG.update()
        LabelImageD.update()
        LabelImageG.update()
        time.sleep(1.5)
        affichageValeur()
        LabelAffichageD1.update()
        LabelAffichageD2.update()
        LabelAffichageG.update()
        LabelImageD.update()
        LabelImageG.update()
        time.sleep(1.5)
        affichageValeur()
        LabelAffichageD1.update()
        LabelAffichageD2.update()
        LabelAffichageG.update()
        LabelImageD.update()
        LabelImageG.update()
        time.sleep(1.5)
        affichageValeur()

def reste():
    LabelImageG['image']= IMGNORMAL1
    LabelImageD['image'] = IMG100
    LabelAffichageG['text'] = vide
    LabelAffichageD1['text'] = vide
    LabelAffichageD2['text'] = vide
    LabelAffichageD1.update()
    LabelAffichageD2.update()
    LabelAffichageG.update()
    LabelImageD.update()
    LabelImageG.update()

        
configMenu = Menu(screen,bg=color,fg = TextColor)
Option = Menu(configMenu,tearoff=0)
StartStop = Menu(configMenu,tearoff=0)
Option.add_command(label="Verification de la connextion",command=VerificationConnextion)
Option.add_command(label="Configuration baterie")
Option.add_command(label="Configuration temperature")
StartStop.add_command(label="Start",command=CommandStart)
StartStop.add_command(label="Restet" ,command=reste)
configMenu.add_cascade(label="Configuration",menu=Option)
configMenu.add_cascade(label="On off",menu=StartStop)
screen.config(menu=configMenu) 

#affichage
affichagePrincipal()
Affichagetension()
AffichageTemp()

screen.mainloop()