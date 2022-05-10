from tkinter import*
import time
import os

#varriable
screen = Tk()
color = "white"
TextColor = "black"
OptionList = ["Choix pilote","Antonin","Axel","Baptiste D","Baptiste P","Gabriel","Martin","Pierrick"]
CompteurPilote = IntVar(value=0)
VarriableRetour = StringVar(screen)
VarriableRetour.set(OptionList[0])
VarriablePilote = ""
#config fenetre
screen.title("Stat BMW M1 E30 #1")
screen.iconphoto(False,PhotoImage(file="image/bmw.png"))
screen.minsize(1100,500)
screen.config(bg = color)

#cadre
CadreLeft = Frame(screen,width=300,height=800,bg=color)
CadreCenter = Frame(screen,width=300,height=800,bg=color)
CadreRight = Frame(screen,width=300,height=800,bg=color)
#widget
LabelText1 = Label(CadreCenter,text="Pilote",bg=color,fg=TextColor,font=("arial",30))
LabelEcart1 = Label(CadreCenter,bg=color,height=5)
LabelEcart2 = Label(CadreCenter,bg=color,height=5)
LabelEcart3 = Label(CadreCenter,bg=color,height=5)
LabelEcart4 = Label(CadreCenter,bg=color,height=5)
Menulist = OptionMenu(CadreCenter,VarriableRetour, *OptionList)
LabelAffichage1 = Label(CadreCenter,width=10,height=2)
#commande
def callback(*args):
    LabelAffichage1.configure(text="{}".format(VarriableRetour.get()))
def setPilote():
    VarriablePilote = VarriableRetour.get()
def NewFile():
    print()
#menu
configMenu = Menu(screen,bg=color,fg = TextColor)
configMenu.add_command(label="Creer un nouveau fichier",command=NewFile)


#Bouton
BoutonSetPilote = Button(CadreCenter,text="Set pilote",command=setPilote)
#affichage
CadreCenter.pack()
CadreLeft.pack()
CadreRight.pack()

LabelText1.pack()
LabelEcart1.pack()
Menulist.pack()
LabelEcart2.pack()
LabelAffichage1.pack()
LabelEcart3.pack()
BoutonSetPilote.pack()
LabelEcart4.pack()
VarriableRetour.trace("w",callback)
screen.config(menu=configMenu)
screen.mainloop()