#coding:utf-8

from tkinter import *


fenetre=Tk()
fenetre.title("Calculatrice")
longueur=200
largeur=200
fenetre.minsize(largeur,longueur)
fenetre.resizable(width=False, height=False)
pad_x=10
pad_y=10
#cadrant1
texte_cadrant1=""
l_teste_nbr=Label(fenetre, text=1)
def f_zero():
    if l_teste_nbr["text"]==1:
        cadrant1["text"]+="0"
    if l_teste_nbr["text"]==0:
        cadrant1["text"]=""
        cadrant1["text"]+="0"
        l_teste_nbr["text"]=1
def f_un():
    if l_teste_nbr["text"]==1:
        cadrant1["text"]+="1"
    if l_teste_nbr["text"]==0:
        cadrant1["text"]=""
        cadrant1["text"]+="1"
        l_teste_nbr["text"]=1

def f_deux():
    if l_teste_nbr["text"]==1:
        cadrant1["text"]+="2"
    if l_teste_nbr["text"]==0:
        cadrant1["text"]=""
        cadrant1["text"]+="2"
        l_teste_nbr["text"]=1

def f_trois():
    if l_teste_nbr["text"]==1:
        cadrant1["text"]+="3"
    if l_teste_nbr["text"]==0:
        cadrant1["text"]=""
        cadrant1["text"]+="3"
        l_teste_nbr["text"]=1

def f_quatre():
    if l_teste_nbr["text"]==1:
        cadrant1["text"]+="4"
    if l_teste_nbr["text"]==0:
        cadrant1["text"]=""
        cadrant1["text"]+="4"
        l_teste_nbr["text"]=1

def f_cinq():
    if l_teste_nbr["text"]==1:
        cadrant1["text"]+="5"
    if l_teste_nbr["text"]==0:
        cadrant1["text"]=""
        cadrant1["text"]+="5"
        l_teste_nbr["text"]=1

def f_six():
    if l_teste_nbr["text"]==1:
        cadrant1["text"]+="6"
    if l_teste_nbr["text"]==0:
        cadrant1["text"]=""
        cadrant1["text"]+="6"
        l_teste_nbr["text"]=1

def f_sept():
    if l_teste_nbr["text"]==1:
        cadrant1["text"]+="7"
    if l_teste_nbr["text"]==0:
        cadrant1["text"]=""
        cadrant1["text"]+="7"
        l_teste_nbr["text"]=1

def f_huit():
    if l_teste_nbr["text"]==1:
        cadrant1["text"]+="8"
    if l_teste_nbr["text"]==0:
        cadrant1["text"]=""
        cadrant1["text"]+="8"
        l_teste_nbr["text"]=1

def f_neuf():
    if l_teste_nbr["text"]==1:
        cadrant1["text"]+="9"
    if l_teste_nbr["text"]==0:
        cadrant1["text"]=""
        cadrant1["text"]+="9"
        l_teste_nbr["text"]=1


cadrant1=Label(fenetre, text=texte_cadrant1, width=20, bg="lightblue", font=" 20")
cadrant1.grid(row=0,column=0, sticky=W+E, columnspan=4, padx=10, pady=5)
operateur=""
nbr_operateur=0
#cadrant2
texte_cadrant2=""
cadrant2=Label(fenetre, text=texte_cadrant2, bg="lightblue", font=" 20")
cadrant2.grid(row=2,column=0, sticky=W+E, columnspan=4, padx=10, pady=5)

#ligne 1
#bouton 1
un=Button(fenetre, text="1",width="4",command=f_un)
un.grid(row=3,column=0, padx=pad_x, pady=pad_y)

#bouton 2
deux=Button(fenetre, text="2", width="4", command=f_deux)
deux.grid(row=3,column=1,padx=pad_x, pady=pad_y)
#bouton 3
trois=Button(fenetre, text="3", width="4", command=f_trois)
trois.grid(row=3,column=2,padx=pad_x, pady=pad_y)

#operateur /

def f_division():
    if l_nbr_operateur["text"]<=0:
        cadrant1["text"]+="/"
        l_nbr_operateur["text"]+=1
        l_operateur["text"]="/"

division=Button(fenetre, text="/", width="4", command=f_division)
division.grid(row=3, column=3, padx=pad_x, pady=pad_y)
#ligne 2
#bouton 4
quatre=Button(fenetre, text="4", width="4", command=f_quatre)
quatre.grid(row=4,column=0, padx=pad_x, pady=pad_y)

#bouton 5
cinq=Button(fenetre, text="5", width="4", command=f_cinq)
cinq.grid(row=4,column=1, padx=pad_x, pady=pad_y)
#bouton 6
six=Button(fenetre, text="6", width="4", command=f_six)
six.grid(row=4,column=2, padx=pad_x, pady=pad_y)

#operateur x
def f_multiplication():
    if l_nbr_operateur["text"]<=0:
        cadrant1["text"]+="x"
        l_nbr_operateur["text"]+=1
        l_operateur["text"]="x"


multiplication=Button(fenetre, text="X", width="4", command=f_multiplication)
multiplication.grid(row=4, column=3, padx=pad_x, pady=pad_y)

#ligne 3
#bouton 7
sept=Button(fenetre, text="7", width="4", command=f_sept)
sept.grid(row=5,column=0, padx=pad_x, pady=pad_y)

#bouton 8
huit=Button(fenetre, text="8", width="4", command=f_huit)
huit.grid(row=5,column=1, padx=pad_x, pady=pad_y)
#bouton 9
neuf=Button(fenetre, text="9", width="4", command=f_neuf)
neuf.grid(row=5,column=2, padx=pad_x, pady=pad_y)

#operateur -
def f_soustraction():
    if l_nbr_operateur["text"]<=0:
        cadrant1["text"]+="-"
        l_nbr_operateur["text"]+=1
        l_operateur["text"]="-"

soustraction=Button(fenetre, text="-", width="4", command=f_soustraction)
soustraction.grid(row=5, column=3, padx=pad_x, pady=pad_y)

#ligne 4
point=Button(fenetre, text=".",width=4)
#point.grid(row=6, column=0, padx=pad_x, pady=pad_y)
def f_clear():
    cadrant1["text"]=""
    cadrant2["text"]=""
    l_nbr_operateur=1
    l_operateur=""
    l_teste_nbr=1
clear=Button(fenetre, text="CLR", width=4, command=f_clear)
clear.grid(row=6, column=0, padx=pad_x, pady=pad_y)
zero=Button(fenetre, text="0" ,width="4", command=f_zero)
zero.grid(row=6, column=1, padx=pad_x, pady=pad_y)
#operateur +
l_nbr_operateur=Label(fenetre, text=0)
l_operateur=Label(fenetre, text="")
def f_addition():
    if l_nbr_operateur["text"]<=0:
        cadrant1["text"]+="+"
        l_nbr_operateur["text"]+=1
        l_operateur["text"]="+"



addition=Button(fenetre, text="+" ,width="4",command=f_addition)
addition.grid(row=6, column=3, padx=pad_x, pady=pad_y)

#ligne 5
def f_egal():

    if l_operateur["text"]=="+":

        tmp=cadrant1["text"]
        tmp=tmp.split("+")
        tmp[0]=int(tmp[0])
        tmp[1]=int(tmp[1])
        cadrant2["text"]=tmp[0]+tmp[1]
    if l_operateur["text"]=="-":

        tmp=cadrant1["text"]
        tmp=tmp.split("-")
        tmp[0]=int(tmp[0])
        tmp[1]=int(tmp[1])
        cadrant2["text"]=tmp[0]-tmp[1]
    if l_operateur["text"]=="x":

        tmp=cadrant1["text"]
        tmp=tmp.split("x")
        tmp[0]=int(tmp[0])
        tmp[1]=int(tmp[1])
        cadrant2["text"]=tmp[0]*tmp[1]
    if l_operateur["text"]=="/":

        tmp=cadrant1["text"]
        tmp=tmp.split("/")
        tmp[0]=int(tmp[0])
        tmp[1]=int(tmp[1])
        cadrant2["text"]=tmp[0]/tmp[1]
    l_teste_nbr["text"]=0
    l_nbr_operateur["text"]=0
egal=Button(fenetre, text="=", width=4, command=f_egal)
egal.grid(row=6, column=2, padx=pad_x, pady=pad_y)
fenetre.mainloop()
