from tkinter import *
import random
import tkinter.font as tkFont
import time
fenetre=Tk()
fenetre['bg']='white'
fenetre.title('choix')

cn=Frame(fenetre,padx=50,pady=50, borderwidth=2, relief=GROOVE)
cn.grid()

font3=tkFont.Font(family="Times", size="14", slant="italic", underline="1")
font4=tkFont.Font(family="Times", size="12")
font5=tkFont.Font(family="Times", size="12", slant="italic")
font6=tkFont.Font(family="Times", slant="italic", underline="1")
font7=tkFont.Font(family="Times", size="16")

nombre=StringVar()
choix1=Radiobutton(cn,text='1 Baton',variable=nombre,value=1 ,font=font4 )
choix1.grid(row=2,column=0)
choix2=Radiobutton(cn,text='2 Batons',variable=nombre,value=2 , font=font4)
choix2.grid(row=2,column=1)
choix3=Radiobutton(cn,text='3 Batons',variable=nombre,value=3 , font=font4)
choix3.grid(row=2,column=2)

j=Label(cn,text="voua avez prid batons." , font=font3)
j.grid(row=4,column=1,padx=5,pady=5)

ia=Label(cn,text="L'ordinateur a pris "" batons." , font=font3)
ia.grid(row=5,column=1,padx=5,pady=5)

l=Label(cn)
l.grid(row=6, column=1)

bat=Label(cn, text="Batons restants :" , font=font3)
bat.grid(row=6,column=1,padx=5,pady=5)

gagnant=Label(cn, text="" , font=font7)
gagnant.grid(row=6,column=1,padx=5,pady=5)
B=20
I=0
J=0
C=1

def Jeu2():
    global B
    global I
    global J
    print ('tour1')
    if B!=1:
        J=nombre.get()
        J=int(J)#int() : permet de modifier une variable en entier.
        print("Vous avez pris",J,"batons.")
        B=B-J
        print("Il reste",B,"batons.")
        print("Tour terminé,à l'IA de jouer.")
        time.sleep(2)
        if J==1:
            if B>1:
                I=2
                print("L'IA a pris",I,"batons.")
                B=B-I
                print("Il reste",B,"batons.")
        if J==2:
            if B>1:
                I=1
                print("L'IA a pris",I,"batons.")
                B=B-I
                print("Il reste",B,"batons.")
        if J==3:
                I=3
                print("L'IA a pris",I,"batons.")
                B=B-I
                print("Il reste",B,"batons.")
        vali2.config(command=Jeu3)
        
vali2=Button(cn,text='valider')
vali2.grid(row=3,column=2,padx=5,pady=5)


def Jeu3():
        print ('tour2')
        global B
        global I
        global J
        print ("votre tour")
        J=nombre.get()
        J=int(J)
        B=B-J
        print("Il reste",B,"batons.")
        print("Tour terminé,à l'ia de jouer.")
        if B>6: 
            I=4-J
            print("L'IA a pris",I,"baton(s).")
            B=B-I
            print("Il reste",B,"batons.")
        vali2.config(command=Jeu4)   
    
def Jeu4():
        print ('tour3')
        global B
        global I
        global J
        print ("votre tour")
        J=nombre.get()
        J=int(J)
        B=B-J
        print("Il reste",B,"batons.")
        print("Tour terminé,à l'ia de jouer.")
        if B>6: 
            I=4-J
            print("L'IA a pris",I,"baton(s).")
            B=B-I
            print("Il reste",B,"batons.")
        if B==8:#faille du programme le rendant battable--->corrigé
            I=3#
            print("L'IA a pris",I,"batons.")#
            B=B-I#
            print("Il reste",B,"batons.")#    
        vali2.config(command=Jeu5)

def Jeu5():
        print ('tour4')
        global B
        global I
        global J
        print ("votre tour")
        J=nombre.get()
        J=int(J)
        B=B-J
        print("Il reste",B,"batons.")
        print("Tour terminé,à l'ia de jouer.")
        if B<=4:
            if B==4:
                I=3
                print("L'IA a pris",I,"batons.")
                B=B-I
                print("Il reste",B,"baton.")
                print("Vous avez perdu.")
                                
            if B==3:
                I=2
                print("L'IA a pris",I,"batons.")
                B=B-I
                print("Il reste",B,"baton.")
                print("Vous avez perdu.")
            if B==2:
                I=1
                print("L'IA a pris",I,"baton.")
                B=B-I
                print("Il reste",B,"baton.")
                print("Vous avez perdu")
        if B==6:
            I=1
            print("L'IA a pris",I,"batons.")#
            B=B-I#
            print("Il reste",B,"batons.") 
        if B==8:#faille du programme le rendant battable--->corrigé
            I=3#
            print("L'IA a pris",I,"batons.")#
            B=B-I#
            print("Il reste",B,"batons.")#    
        if B>6: 
            I=4-J
            print("L'IA a pris",I,"baton(s).")
            B=B-I
            print("Il reste",B,"batons.")
        if B==1:
            vali2.destroy()
        elif B!=1:
            vali2.config(command=Jeu6)
     
def Jeu6():
        global B
        global I
        global J
        print ('tour5')
        print ("votre tour")
        J=nombre.get()
        J=int(J)
        B=B-J
        print("Il reste",B,"batons.")
        print("Tour terminé,à l'ia de jouer.")
        if B<=4:
            if B==4:
                I=3
                print("L'IA a pris",I,"batons.")
                B=B-I
                print("Il reste",B,"baton.")
                print("Vous avez perdu.")
                                
            if B==3:
                I=2
                print("L'IA a pris",I,"batons.")
                B=B-I
                print("Il reste",B,"baton.")
                print("Vous avez perdu.")
            if B==2:
                I=1
                print("L'IA a pris",I,"baton.")
                B=B-I
                print("Il reste",B,"baton.")
                print("Vous avez perdu")
        if B==6:
            I=1
            print("L'IA a pris",I,"batons.")#
            B=B-I#
            print("Il reste",B,"batons.") 
        if B==8:#faille du programme le rendant battable--->corrigé
            I=3#
            print("L'IA a pris",I,"batons.")#
            B=B-I#
            print("Il reste",B,"batons.")#    
        if B>6: 
            I=4-J
            print("L'IA a pris",I,"baton(s).")
            B=B-I
            print("Il reste",B,"batons.")     
        vali2.destroy()

if C==1:
    vali2.config(command=Jeu2)
        
fenetre.mainloop()
