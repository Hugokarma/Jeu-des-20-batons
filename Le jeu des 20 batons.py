from tkinter import *#pour l'affichage
import random#pour les variables aléatoire
import tkinter.font as tkFont#pour les formes, taille et police de caractère....

prst=Tk()#crée fenêtre
prst['bg']='white'
prst.title('Twenty sticks to die')


font1=tkFont.Font(family="Times", size="22", weight="bold", slant="italic")
font2=tkFont.Font(family="Times", size="18", weight="bold", slant="italic")
font3=tkFont.Font(family="Times", size="14", underline="1")
font4=tkFont.Font(family="Times", size="12")
font5=tkFont.Font(family="Times", size="12", slant="italic")

regle=LabelFrame(prst,text="Les 20 batons", padx=200, pady=200, font=font1)
regle.pack(fill="both", expand="yes")#fill: elle détermine s'il faut utiliser plus d'espace ou garder les "propres" dimensions.
#expand: il traite de l'expansion du widget parent peut être enlevé


texte=Label(regle, text="BIENVENUE")#peut pas mettre pack ici
texte.pack()#sans ca prends pas en compte le configure
texte.configure(font=font2)
#lebels pour le sregles
texte1=Label(regle)
texte1.pack()
texte2=Label(regle, text="Présentation du jeu des 20 batons:")
texte2.pack()
texte2.configure(font=font3)
texte3=Label(regle, text="Jeu de réflexion, le jeu de 20 batons est issu de l'émission Ford Boyard.")
texte3.pack()
texte3.configure(font=font4)
texte4=Label(regle, text="But et règles du jeu:")
texte4.pack()
texte4.configure(font=font3)
texte5=Label(regle, text="Le but du jeu est simple, pour gagner il faut que l'adversaire saissise le dernier baton.")
texte5.pack()
texte5.configure(font=font4)
texte5=Label(regle, text="20 batons sont disposez devant vous. Chaucun votre tour vous devez prendre entre 1 et 3 batons.")
texte5.pack()
texte5.configure(font=font4)
texte6=Label(regle, text="Comme dit précédemment si vous par malheur c'est votre tour et qu'il ne reste qu'un baton, vous avez perdu.")
texte6.pack()
texte6.configure(font=font4)
texte7=Label(regle)
texte7.pack()

boutonlancer=Button(regle, text="Lancer une partie contre l'IA", command=prst.destroy, borderwidth=10, relief=GROOVE , font=font5)
boutonlancer.pack()


prst.mainloop()



fenetre=Tk()
fenetre['bg']='white'
fenetre.title('Twenty sticks to die')


font3=tkFont.Font(family="Times", size="14", slant="italic", underline="1")
font4=tkFont.Font(family="Times", size="12")
font5=tkFont.Font(family="Times", size="12", slant="italic")
font6=tkFont.Font(family="Times", size="18", slant="italic", underline="1")

pileface=Frame(fenetre,padx=50,pady=50, bd=2, relief=GROOVE)
pileface.grid()


titre=Label(pileface, text="Pile ou Face" , font=font6)
titre.grid(row=0, column=1)
titre2=Label(pileface, text="Ce pile ou face va déterminer si vous ou l'IA commence." , font=font4)
titre2.grid(row=1, column=1)

question=Label(pileface, text="Entrez votre nom :" , font=font3)
question.grid(row=2,column=1,padx=25,pady=15)

reponse=Entry(pileface)#widget pour entrer son nom
reponse.grid(row=2,column=2)

def ecrire_nom1(event):#fonction pour que le joueur entre son nom
    global nom1
    nom1=reponse.get()
    #print(nom1)
    joueur1.configure(text=reponse.get())

reponse.bind("<Return>",ecrire_nom1)

joueur1= Label(pileface, text="Joueur", font=font4)#label ou le nom du joueur apparait
joueur1.grid(row=3,column=1,padx=15,pady=15)

ia= Label(pileface, text="Ordinateur", font=font4)
ia.grid(row=3,column=2,padx=40,pady=15)

choix=Label(pileface, text="Choississez entre pile et face :", font=font3)
choix.grid(row=4,column=0,padx=15,pady=15)

L="L'IA"
P="Vous"
C=0#variable qui permet de faire commencer les bonnes fonction selon le résultat du pile/face
def commencer1():#fonction pour le pile ou face associé au bouton pile
    global A
    global C
    piece=random.randint(1,2)
    if piece == 1:
        #print("Pile")utile pour voir si ca fonctionne pas dans le jeu
        resultat.configure(text='Pile')
        label.configure(text='Vous commencez.')
        A=P,"commencez"#sert à titre indicatif dans la dernière fenêtre
        C=1#le joueur gagne, cela va permettre de lancer les fonctions correspondantes
    else:
        resultat.configure(text='Face')
        label.configure(text="L'IA commence.")
        A=L,"commence"
        C=2#joueur perd donc les fonctions correpondante seront lancés

def commencer2():#fonction pour le pile/face associé au bouton face
    global A
    global C
    piece=random.randint(1,2)
    if piece == 1:
        #print("Face")pareil qu'avec print
        resultat.configure(text='Face')
        label.configure(text='Vous commencez.')
        A=P,"commencez"
        C=1#le joueur gagne, cela va permettre de lancer les fonctions correspondantes
    else :
        resultat.configure(text='Pile')
        label.configure(text="L'IA commence.")
        A=L,"commence"
        C=2#joueur perd donc les fonctions correpondante seront lancés

bpile=Button(pileface, text='Pile', command=commencer1, borderwidth=5, relief=RIDGE , font=font5)
bpile.grid(row=4,column=1) 

bface=Button(pileface, text='Face', command=commencer2, borderwidth=5, relief=RIDGE , font=font5)
bface.grid(row=4,column=2)

resultat=Label(pileface , font=font4)#label qui affiche qui a gagné ou perdu
resultat.grid(row=5,column=1,padx=5,pady=5)

label=Label(pileface , font=font4)#label qui affiche qui commence
label.grid(row=5, column=2, padx=15,pady=5)

boutonquitter=Button(pileface,text='Lancer la partie',command=fenetre.destroy, borderwidth=7, relief=GROOVE , font=font5)
boutonquitter.grid(row=6, column=1, padx=15,pady=1)


fenetre.mainloop()



fenetre1=Tk()
fenetre1['bg']='white'
fenetre1.title('Twenty sticks to die')


font3=tkFont.Font(family="Times", size="14", slant="italic", underline="1")
font4=tkFont.Font(family="Times", size="12")
font5=tkFont.Font(family="Times", size="12", slant="italic")
font6=tkFont.Font(family="Times", size="18", slant="italic", underline="1")
font7=tkFont.Font(family="Times", size="20")
font8=tkFont.Font(family="Times", size="8")#font représente plusieurs types d'écriture

res=Frame(fenetre1,padx=50,pady=50, borderwidth=2, relief=GROOVE)
res.grid()
batons=Frame(fenetre1,padx=110,pady=80, borderwidth=2, relief=GROOVE)
batons.grid()


lancer=Label(res,text=A, font=font4)
lancer.grid(row=0,column=1,padx=5,pady=5)

nombre=StringVar()
choix1=Radiobutton(res,text='1 Baton',variable=nombre,value=1 , font=font4)
choix1.grid(row=2,column=0)
choix2=Radiobutton(res,text='2 Batons',variable=nombre,value=2 , font=font4)
choix2.grid(row=2,column=1,ipadx=208)
choix3=Radiobutton(res,text='3 Batons',variable=nombre,value=3 , font=font4)
choix3.grid(row=2,column=2)

txt=Label(res, text="Vous commencez, combien de batons voulez-vous prendre ?", font=font3)
txt.grid(row=1,column=1,pady=25)

j=Label(res,font=font3)#label affiche ce que le joueur a pris
j.grid(row=3, column=0,pady=5)

j2=Label(res)#permet d'eviter que les wigets s'adaptent au texte creer une largeur
j2.grid(row=4,column=0, ipadx=100)#de colonne assez grande pour tt les widgets, ipads creer espace de chauque a partir d'un point car pas de texte ici

vali2=Button(res,text="Valider", borderwidth=5, relief=RIDGE , font=font5)
vali2.grid(row=3,column=1,pady=5)

ia=Label(res, font=font3)#label affiche ce que l'IA a pris
ia.grid(row=3,column=2,pady=5)

ia2=Label(res)#permet d'avoir des colonnes avec des largeurs fixe
ia2.grid(row=4,column=2,ipadx=100,pady=5)

bat=Label(res, text="Batons restants: 20", font=font3)
bat.grid(row=4,column=1,pady=5)

gagnant=Label(res, font=font7)#affiche le gagnant
gagnant.grid(row=5,column=1,pady=5)

tour=Label(res, font=font8)#affiche le nmbr de tour
tour.grid(row=5,column=2,padx=5,pady=5)

if C==2:#test de la variable lors du pile/face détermine quelle fonction lancé en premier
    txt.configure(text="L'intelligence artificielle commence à jouer.",font=font3)
    #adapte affichage au tirage pileface
B=20#nbre batons restants
I=0#nbre batons pris par l'IA
J=0#nbre batons pris par le joueur

def Jeu2():#fonction qd joeuur commence
    global B#on globalise les variables au début de la fonction pour pouvoir les réutiliser
    global I
    global J
    tour.configure(text='1')
    J=nombre.get()#récupère la valeur du radio boutons
    J=int(J)#int() : permet de modifier une variable en entier pour le calcul
    B=B-J
    J=str(J)#permet d'afficher une variable avec tkinter
    B=str(B)#permet d'afficher une variable avec tkinter
    j.configure(text="Vous avez pris "+J+" baton(s).")#change le texte d'un label
    bat.configure(text="Il reste "+B+" batons.")
    txt.configure(text="L'IA joue.")
    J=int(J)
    B=int(B)
    def Jeu21():#1er tour de l'IA
        global B
        global I
        j.configure(text="")
        if J==1:#condition par rapport au 1er tour du joueur
            I=2
            B=B-I
            I=str(I)
            B=str(B)           
            ia.configure(text="L'IA a pris "+I+" batons.")
            bat.configure(text="Il reste "+B+" batons.")
        if J==2:#condition par rapport au 1er tour du joueur
            I=1
            B=B-I
            I=str(I)
            B=str(B)
            ia.configure(text="L'IA a pris "+I+" baton.")
            bat.configure(text="Il reste "+B+" batons.")
        if J==3:#condition par rapport au 1er tour du joueur, ces condition rende l'IA imbattable
            I=3
            B=B-I
            I=str(I)
            B=str(B)
            ia.configure(text="L'IA a pris "+I+" batons.")
            bat.configure(text="Il reste "+B+" batons.")
        B=int(B)
        vali2.config(command=Jeu3)#configure la commande du bouton sur la fonction Jeu3
        txt.configure(text="A vous de jouer combien de batons voulez vous prendre ?")
    res.after(2500,Jeu21)#retarde le lancement de Jeu21, pour laisser le temps ai joueur de lire l'interface

def Jeu3():#nouvelle manche tour joueur
    global B
    global I
    global J
    tour.configure(text='2')
    J=nombre.get()
    J=int(J)
    B=B-J
    J=str(J)
    B=str(B)
    j.configure(text="Vous avez pris "+J+" baton(s).")
    bat.configure(text="Il reste "+B+" batons.")
    txt.configure(text="L'IA joue.")
    ia.configure(text="")
    J=int(J)
    B=int(B)
    def Jeu31():#tour IA
        global B
        global I
        j.configure(text="")
        if B>6: 
            I=4-J#astuce pour que l'IA gagne
            B=B-I
            I=str(I)
            B=str(B)
            ia.configure(text="L'IA a pris "+I+" baton(s).")
            bat.configure(text="Il reste "+B+" batons.")
        B=int(B)
        txt.configure(text="A vous de jouer combien de batons voulez vous prendre ?")
        vali2.config(command=Jeu4)   
    res.after(2500,Jeu31)
        
def Jeu4():
    global B
    global I
    global J
    tour.configure(text='3')
    J=nombre.get()
    J=int(J)
    B=B-J
    J=str(J)
    B=str(B)
    j.configure(text="Vous avez pris "+J+" baton(s).")
    bat.configure(text="Il reste "+B+" batons.")
    txt.configure(text="L'IA joue.")
    ia.configure(text="")
    J=int(J)
    B=int(B)
    def Jeu41():
        global B
        global I
        j.configure(text="")
        if B>6:#Condition de jeu normal pour toute la partie
            I=4-J
            B=B-I
            I=str(I)
            B=str(B)
            ia.configure(text="L'IA a pris "+I+" baton(s).")
            bat.configure(text="Il reste "+B+" batons.")
        if B==8:#faille du programme le rendant battable--->corrigé
            I=3#
            B=B-I#
            I=str(I)
            B=str(B)
            ia.configure(text="L'IA a pris "+I+" batons.")
            bat.configure(text="Il reste "+B+" batons.")    
        B=int(B)
        txt.configure(text="A vous de jouer combien de batons voulez vous prendre ?")
        vali2.config(command=Jeu5)
    res.after(2500,Jeu41)
    
def Jeu5():
    global B
    global I
    global J
    tour.configure(text='4')
    txt.configure(text="A vous de jouer combien de batons voulez vous prendre ?")
    J=nombre.get()
    J=int(J)
    B=B-J
    J=str(J)
    B=str(B)
    j.configure(text="Vous avez pris "+J+" baton(s).")
    bat.configure(text="Il reste "+B+" batons.")
    txt.configure(text="L'IA joue.")
    ia.configure(text="")
    J=int(J)
    B=int(B)
    def Jeu51():
        global B
        global I
        j.configure(text="")
        if B<=4:#nouvelle condition pour que l'IA gagne
            if B==4:#condition selon le nbre de batons restants
                I=3
                B=B-I
                I=str(I)
                B=str(B)
                ia.configure(text="L'IA a pris "+I+" batons.")
                bat.configure(text="Il reste "+B+" baton.")
                gagnant.configure(text="Vous avez perdu.")                      
            if B==3:#condition selon le nbre de batons restants
                I=2
                B=B-I
                I=str(I)
                B=str(B)
                ia.configure(text="L'IA a pris "+I+" batons.")
                bat.configure(text="Il reste "+B+" baton.")
                gagnant.configure(text="Vous avez perdu.")
            if B==2:#condition selon le nbre de batons restants
                I=1
                B=B-I
                I=str(I)
                B=str(B)
                ia.configure(text="L'IA a pris "+I+" baton.")
                bat.configure(text="Il rest e"+B+" baton.")
                gagnant.configure(text="Vous avez perdu.")#####--->
        if B==6:#faille du programme coup exceptionnel
            I=1
            B=B-I#
            I=str(I)
            B=str(B)
            ia.configure(text="L'IA a pris "+I+" baton.")
            bat.configure(text="Il reste "+B+" batons.")
        if B==8:#faille du programme le rendant battable--->corrigé
            I=3#
            B=B-I#
            I=str(I)
            B=str(B)
            ia.configure(text="L'IA a pris "+I+" batons.")
            bat.configure(text="Il reste "+B+" batons.")
        B=int(B)#erreur line 333 avec ca resout le pb
        if B>6: 
            I=4-J
            B=B-I
            I=str(I)
            B=str(B)
            ia.configure(text="L'IA a pris "+I+" baton(s).")
            bat.configure(text="Il reste "+B+" batons.")
        B=int(B)
        if B==1:
            vali2.destroy()
        elif B!=1:
            vali2.config(command=Jeu6)
            txt.configure(text="A vous de jouer combien de batons voulez vous prendre ?")
    res.after(2500,Jeu51)
    
def Jeu6():
    global B
    global I
    global J
    tour.configure(text='5')
    txt.configure(text="A vous de jouer combien de batons voulez vous prendre ?")
    J=nombre.get()
    J=int(J)
    B=B-J
    J=str(J)
    B=str(B)
    j.configure(text="Vous avez pris "+J+" baton(s).")
    bat.configure(text="Il reste "+B+" batons.")
    txt.configure(text="L'IA joue.")
    ia.configure(text="")
    J=int(J)
    B=int(B)
    def Jeu61():
        global B
        global I
        j.configure(text="")
        if B<=4:
            if B==4:
                I=3
                B=B-I
                I=str(I)
                B=str(B)
                ia.configure(text="L'IA a pris "+I+" batons.")
                bat.configure(text="Il reste "+B+" baton.")
                gagnant.configure(text="Vous avez perdu.")
            if B==3:
                I=2
                B=B-I
                I=str(I)
                B=str(B)
                ia.configure(text="L'IA a pris "+I+" batons.")
                bat.configure(text="Il reste "+B+" baton.")
                gagnant.configure(text="Vous avez perdu.")
            if B==2:
                I=1
                B=B-I
                I=str(I)
                B=str(B)
                ia.configure(text="L'IA a pris "+I+" baton.")
                bat.configure(text="Il reste "+B+" baton.")
                gagnant.configure(text="Vous avez perdu.")#######-->
        if B==6:
            I=1
            B=B-I#
            I=str(I)
            B=str(B)
            ia.configure(text="L'IA a pris "+I+" baton.")
            bat.configure(text="Il reste "+B+" batons.") 
        if B==8:#faille du programme le rendant battable--->corrigé
            I=3#
            B=B-I#
            I=str(I)
            B=str(B)
            ia.configure(text="L'IA a pris "+I+" batons.")
            bat.configure(text="Il reste "+B+" batons.")
        B=int(B)
        if B>6: 
            I=4-J
            B=B-I
            I=str(I)
            B=str(B)
            ia.configure(text="L'IA a pris "+I+" baton(s).")
            bat.configure(text="Il reste "+B+" batons.")     
        B=int(B)
        #pas besoin de condition car dernier tour en principe (tour max)
            #choix1.destroy() le radio bouton est détruit ????alors que le prochain destroy.
        vali2.destroy()#ne detruit pas lebouton mais le rend inutilsable
    res.after(2000,Jeu61)

if C==2:#test de la variable du pile/face, si l'IA gagne il commence alors les fontions suivante sont lancé
    def Jeu7():#premier tour de l'IA
        global B#pareil on globalise les variable pour les réutiliser
        global I
        tour.configure(text='tour: 1')
        I=random.randint(1,3)#fonction pour tirer un nombre aléatoire
        B=B-I
        I=str(I)
        B=str(B)
        ia.configure(text="L'IA a pris "+I+" batons.")
        bat.configure(text="Il reste "+B+" batons.")
        B=int(B)
        txt.configure(text="A vous de jouer combien de batons voulez vous prendre ?")
    res.after(2000,Jeu7)#retarde lancement de fonction Jeu7 de 2 secondes
#la 1 ere et derniere fonction ne représente que 1 tour car on veut que le joueur n'utilise le bouton que quand il joue
    #et pas quand l'IA joue, donc la 1ere est fonction du tour de l'IA se lancant seul et la dernière focntion
    #pourrait etre 1 manche(tour joueue +tour IA) mais cela est inutile, donc dernière fonction est une fonction joueur
def Jeu8():#manche donc d'abord tour de joueur et apres IA
    global B
    global J
    global I
    J=nombre.get()#obtiens la valeur du radio boutons
    J=int(J)#int() : permet de modifier une variable en entier.
    print=(B)
    B=B-J
    J=str(J)
    B=str(B)
    j.configure(text="Vous avez pris "+J+" batons.")
    bat.configure(text="Il reste "+B+" batons.")
    ia.configure(text="")
    txt.config(text="L'intelligence artificielle joue.")
    B=int(B)
    def Jeu81():#tour IA
        global B
        global I
        tour.configure(text='tour: 1')
        I=random.randint(1,3)
        B=B-I
        I=str(I)
        B=str(B)
        ia.configure(text="L'IA a pris "+I+" batons.")
        j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
        bat.configure(text="Il reste "+B+" batons.")
        B=int(B)
        txt.configure(text="A vous de jouer combien de batons voulez vous prendre ?")
    res.after(2500,Jeu81)
    vali2.config(command=Jeu9)

def Jeu9():
    global B
    global J
    global I
    J=nombre.get()
    J=int(J)#int() : permet de modifier une variable en entier.
    print=(B)
    B=B-J
    J=str(J)
    B=str(B)
    j.configure(text="Vous avez pris "+J+" batons.")
    bat.configure(text="Il reste "+B+" batons.")
    txt.config(text="L'intelligence artificielle joue.")
    ia.configure(text="")
    B=int(B)
    def Jeu91():
        global B
        global I
        tour.configure(text='tour: 1')
        I=random.randint(1,3)
        B=B-I
        I=str(I)
        B=str(B)
        ia.configure(text="L'IA a pris "+I+" batons.")
        j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
        bat.configure(text="Il reste "+B+" batons.")
        B=int(B)
        txt.configure(text="A vous de jouer combien de batons voulez vous prendre ?")
    res.after(2500,Jeu91)
    vali2.config(command=Jeu10)

def Jeu10():#tour joueur
    global B
    global J
    global I
    J=nombre.get()
    J=int(J)#int() : permet de modifier une variable en entier.
    print=(B)
    B=B-J
    J=str(J)
    B=str(B)
    j.configure(text="Vous avez pris "+J+" batons.")
    bat.configure(text="Il reste "+B+" batons.")
    txt.config(text="L'intelligence artificielle joue.")
    ia.configure(text="")
    B=int(B)
    def Jeu101():#tour IA
        global B
        global I
        if B>4:#condition de jeu 
            tour.configure(text='tour: 1')
            I=random.randint(1,3)
            B=B-I
            I=str(I)
            B=str(B)
            ia.configure(text="L'IA a pris "+I+" batons.")
            j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
            bat.configure(text="Il reste "+B+" batons.")
            #B=int(B)
            txt.configure(text="A vous de jouer combien de batons voulez vous prendre ?")
        elif B<=4:#condition pour que l'IA gagne
            if B==4:#agit intelligement en fonction de la situation
                I=3
                B=B-I
                I=str(I)#str pour etre afficher
                B=str(B)
                ia.configure(text="L'IA a pris "+I+" batons.")
                j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
                bat.configure(text="Il reste "+B+" batons.")
                gagnant.configure(text="Vous avez perdu.")
            if B==3:#agit intelligement en fonction de la situation
                I=2
                B=B-I
                I=str(I)#str pour etre afficher
                B=str(B)
                ia.configure(text="L'IA a pris "+I+" batons.")
                j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
                bat.configure(text="Il reste "+B+" batons.")
                gagnant.configure(text="Vous avez perdu.")
            if B==2:#agit intelligement en fonction de la situation
                I=1
                B=B-I
                I=str(I)#str pour etre afficher
                B=str(B)
                ia.configure(text="L'IA a pris "+I+" batons.")
                j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
                bat.configure(text="Il reste "+B+" batons.")
                gagnant.configure(text="Vous avez perdu.")
        B=int(B)#remet en int car doit reutiliser ensuite
        if B!=1:  
            vali2.config(command=Jeu11) #continue le jeu si B est différent de 1   
        elif B==1:
            vali2.destroy()#détruit le bouton donc arrete le jeu si B est égale à 1
    res.after(2500,Jeu101)#retarde lancement de fonction Jeu11 de 2.5sec
    
def Jeu11():
    global B
    global J
    global I
    J=nombre.get()
    J=int(J)#int() : permet de modifier une variable en entier.
    print=(B)
    B=B-J
    J=str(J)
    B=str(B)
    j.configure(text="Vous avez pris "+J+" batons.")
    bat.configure(text="Il reste "+B+" batons.")
    ia.configure(text="")
    B=int(B)
    if B==1:
        gagnant.configure(text="Vous avez gagné")
        vali2.destroy()
    elif B>1:
        txt.config(text="L'intelligence artificielle joue.")
        def Jeu111():
            global B
            global I
            if B>4:
                tour.configure(text='tour: 1')
                I=random.randint(1,3)
                B=B-I
                I=str(I)
                B=str(B)
                ia.configure(text="L'IA a pris "+I+" batons.")
                j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
                bat.configure(text="Il reste "+B+" batons.")
                #B=int(B)
                txt.configure(text="A vous de jouer combien de batons voulez vous prendre ?")
            elif B<=4:
                if B==4:
                    I=3
                    B=B-I
                    I=str(I)#str pour etre afficher
                    B=str(B)
                    ia.configure(text="L'IA a pris "+I+" batons.")
                    j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
                    bat.configure(text="Il reste "+B+" batons.")
                    gagnant.configure(text="Vous avez perdu.")
                if B==3:
                    I=2
                    B=B-I
                    I=str(I)#str pour etre afficher
                    B=str(B)
                    ia.configure(text="L'IA a pris "+I+" batons.")
                    j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
                    bat.configure(text="Il reste "+B+" batons.")
                    gagnant.configure(text="Vous avez perdu.")
                if B==2:
                    I=1
                    B=B-I
                    I=str(I)#str pour etre afficher
                    B=str(B)
                    ia.configure(text="L'IA a pris "+I+" batons.")
                    j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
                    bat.configure(text="Il reste "+B+" batons.")
                    gagnant.configure(text="Vous avez perdu.")
            B=int(B)       
            if B!=1:  
                vali2.config(command=Jeu12)    
            elif B==1:
                vali2.destroy()
        res.after(2500,Jeu111)

def Jeu12():
    global B
    global J
    global I
    J=nombre.get()
    J=int(J)#int() : permet de modifier une variable en entier.
    print=(B)
    B=B-J
    J=str(J)
    B=str(B)
    j.configure(text="Vous avez pris "+J+" batons.")
    bat.configure(text="Il reste "+B+" batons.")
    ia.configure(text="")
    B=int(B)
    if B==1:
        gagnant.configure(text="Vous avez gagné")
        vali2.destroy()
    elif B>1:
        txt.config(text="L'intelligence artificielle joue.")
        def Jeu121():
            global B
            global I
            if B>4:
                tour.configure(text='tour: 1')
                I=random.randint(1,3)
                B=B-I
                I=str(I)
                B=str(B)
                ia.configure(text="L'IA a pris "+I+" batons.")
                j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
                bat.configure(text="Il reste "+B+" batons.")
                #B=int(B)
                txt.configure(text="A vous de jouer combien de batons voulez vous prendre ?")
            elif B<=4:
                if B==4:
                    I=3
                    B=B-I
                    I=str(I)#str pour etre afficher
                    B=str(B)
                    ia.configure(text="L'IA a pris "+I+" batons.")
                    j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
                    bat.configure(text="Il reste "+B+" batons.")
                    gagnant.configure(text="Vous avez perdu.")
                if B==3:
                    I=2
                    B=B-I
                    I=str(I)#str pour etre afficher
                    B=str(B)
                    ia.configure(text="L'IA a pris "+I+" batons.")
                    j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
                    bat.configure(text="Il reste "+B+" batons.")
                    gagnant.configure(text="Vous avez perdu.")
                if B==2:
                    I=1
                    B=B-I
                    I=str(I)#str pour etre afficher
                    B=str(B)
                    ia.configure(text="L'IA a pris "+I+" batons.")
                    j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
                    bat.configure(text="Il reste "+B+" batons.")
                    gagnant.configure(text="Vous avez perdu.")
            B=int(B)     
            if B!=1:  
                vali2.config(command=Jeu13)    
            elif B==1:
                vali2.destroy()
    res.after(2500,Jeu121)
    
def Jeu13():
    global B
    global J
    global I
    J=nombre.get()
    J=int(J)#int() : permet de modifier une variable en entier.
    print=(B)
    B=B-J
    J=str(J)
    B=str(B)
    j.configure(text="Vous avez pris "+J+" batons.")
    bat.configure(text="Il reste "+B+" batons.")
    ia.configure(text="")
    B=int(B)
    if B==1:
        gagnant.configure(text="Vous avez gagné")
        vali2.destroy()
    elif B>1:
        txt.config(text="L'intelligence artificielle joue.")
        def Jeu131():
            global B
            global I
            if B>4:
                tour.configure(text='tour: 1')
                I=random.randint(1,3)
                B=B-I
                I=str(I)
                B=str(B)
                ia.configure(text="L'IA a pris "+I+" batons.")
                j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
                bat.configure(text="Il reste "+B+" batons.")
                #B=int(B)
                txt.configure(text="A vous de jouer combien de batons voulez vous prendre ?")
            elif B<=4:
                if B==4:
                    I=3
                    B=B-I
                    I=str(I)#str pour etre afficher
                    B=str(B)
                    ia.configure(text="L'IA a pris "+I+" batons.")
                    j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
                    bat.configure(text="Il reste "+B+" batons.")
                    gagnant.configure(text="Vous avez perdu.")
                if B==3:
                    I=2
                    B=B-I
                    I=str(I)#str pour etre afficher
                    B=str(B)
                    ia.configure(text="L'IA a pris "+I+" batons.")
                    j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
                    bat.configure(text="Il reste "+B+" batons.")
                    gagnant.configure(text="Vous avez perdu.")
                if B==2:
                    I=1
                    B=B-I
                    I=str(I)#str pour etre afficher
                    B=str(B)
                    ia.configure(text="L'IA a pris "+I+" batons.")
                    j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
                    bat.configure(text="Il reste "+B+" batons.")
                    gagnant.configure(text="Vous avez perdu.")
            B=int(B)     
        if B!=1:  
            vali2.config(command=Jeu14)    
        elif B==1:
            vali2.destroy()
    res.after(2500,Jeu131)

def Jeu14():
    global B
    global J
    global I
    J=nombre.get()
    J=int(J)#int() : permet de modifier une variable en entier.
    print=(B)
    B=B-J
    J=str(J)
    B=str(B)
    j.configure(text="Vous avez pris "+J+" batons.")
    bat.configure(text="Il reste "+B+" batons.")
    ia.configure(text="")
    B=int(B)
    if B==1:
        gagnant.configure(text="Vous avez gagné")
        vali2.destroy()
    elif B>1:
        txt.config(text="L'intelligence artificielle joue.")
        def Jeu141():
            global B
            global I
            if B>4:
                tour.configure(text='tour: 1')
                I=random.randint(1,3)
                B=B-I
                I=str(I)
                B=str(B)
                ia.configure(text="L'IA a pris "+I+" batons.")
                j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
                bat.configure(text="Il reste "+B+" batons.")
                #B=int(B)
                txt.configure(text="A vous de jouer combien de batons voulez vous prendre ?")
            elif B<=4:
                if B==4:
                    I=3
                    B=B-I
                    I=str(I)#str pour etre afficher
                    B=str(B)
                    ia.configure(text="L'IA a pris "+I+" batons.")
                    j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
                    bat.configure(text="Il reste "+B+" batons.")
                    gagnant.configure(text="Vous avez perdu.")
                if B==3:
                    I=2
                    B=B-I
                    I=str(I)#str pour etre afficher
                    B=str(B)
                    ia.configure(text="L'IA a pris "+I+" batons.")
                    j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
                    bat.configure(text="Il reste "+B+" batons.")
                    gagnant.configure(text="Vous avez perdu.")
                if B==2:
                    I=1
                    B=B-I
                    I=str(I)#str pour etre afficher
                    B=str(B)
                    ia.configure(text="L'IA a pris "+I+" batons.")
                    j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
                    bat.configure(text="Il reste "+B+" batons.")
                    gagnant.configure(text="Vous avez perdu.")
            B=int(B)     
        if B!=1:  
            vali2.config(command=Jeu15)    
        elif B==1:
            vali2.destroy()
    res.after(2500,Jeu141)

def Jeu15():
    global B
    global J
    global I
    J=nombre.get()
    J=int(J)#int() : permet de modifier une variable en entier.
    print=(B)
    B=B-J
    J=str(J)
    B=str(B)
    j.configure(text="Vous avez pris "+J+" batons.")
    bat.configure(text="Il reste "+B+" batons.")
    ia.configure(text="")
    B=int(B)
    if B==1:
        gagnant.configure(text="Vous avez gagné")
        vali2.destroy()
    elif B>1:
        txt.config(text="L'intelligence artificielle joue.")
        def Jeu151():
            global B
            global I
            if B>4:
                tour.configure(text='tour: 1')
                I=random.randint(1,3)
                B=B-I
                I=str(I)
                B=str(B)
                ia.configure(text="L'IA a pris "+I+" batons.")
                j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
                bat.configure(text="Il reste "+B+" batons.")
                #B=int(B)
                txt.configure(text="A vous de jouer combien de batons voulez vous prendre ?")
            elif B<=4:
                if B==4:
                    I=3
                    B=B-I
                    I=str(I)#str pour etre afficher
                    B=str(B)
                    ia.configure(text="L'IA a pris "+I+" batons.")
                    j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
                    bat.configure(text="Il reste "+B+" batons.")
                    gagnant.configure(text="Vous avez perdu.")
                if B==3:
                    I=2
                    B=B-I
                    I=str(I)#str pour etre afficher
                    B=str(B)
                    ia.configure(text="L'IA a pris "+I+" batons.")
                    j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
                    bat.configure(text="Il reste "+B+" batons.")
                    gagnant.configure(text="Vous avez perdu.")
                if B==2:
                    I=1
                    B=B-I
                    I=str(I)#str pour etre afficher
                    B=str(B)
                    ia.configure(text="L'IA a pris "+I+" batons.")
                    j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
                    bat.configure(text="Il reste "+B+" batons.")
                    gagnant.configure(text="Vous avez perdu.")
            B=int(B)     
        if B!=1:  
            vali2.config(command=Jeu16)    
        elif B==1:
            vali2.destroy()
    res.after(2500,Jeu151)

def Jeu16():
    global B
    global J
    global I
    J=nombre.get()
    J=int(J)#int() : permet de modifier une variable en entier.
    print=(B)
    B=B-J
    J=str(J)
    B=str(B)
    j.configure(text="Vous avez pris "+J+" batons.")
    bat.configure(text="Il reste "+B+" batons.")
    ia.configure(text="")
    B=int(B)
    if B==1:
        gagnant.configure(text="Vous avez gagné")
        vali2.destroy()
    elif B>1:
        txt.config(text="L'intelligence artificielle joue.")
        def Jeu161():
            global B
            global I
            if B>4:
                tour.configure(text='tour: 1')
                I=random.randint(1,3)
                B=B-I
                I=str(I)
                B=str(B)
                ia.configure(text="L'IA a pris "+I+" batons.")
                j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
                bat.configure(text="Il reste "+B+" batons.")
                #B=int(B)
                txt.configure(text="A vous de jouer combien de batons voulez vous prendre ?")
            elif B<=4:
                if B==4:
                    I=3
                    B=B-I
                    I=str(I)#str pour etre afficher
                    B=str(B)
                    ia.configure(text="L'IA a pris "+I+" batons.")
                    j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
                    bat.configure(text="Il reste "+B+" batons.")
                    gagnant.configure(text="Vous avez perdu.")
                if B==3:
                    I=2
                    B=B-I
                    I=str(I)#str pour etre afficher
                    B=str(B)
                    ia.configure(text="L'IA a pris "+I+" batons.")
                    j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
                    bat.configure(text="Il reste "+B+" batons.")
                    gagnant.configure(text="Vous avez perdu.")
                if B==2:
                    I=1
                    B=B-I
                    I=str(I)#str pour etre afficher
                    B=str(B)
                    ia.configure(text="L'IA a pris "+I+" batons.")
                    j.configure(text="")#permet d'enlever indication du nombre de bat pris avant
                    bat.configure(text="Il reste "+B+" batons.")
                    gagnant.configure(text="Vous avez perdu.")
            B=int(B)     
        if B!=1:  
            vali2.config(command=Jeu17)
            choix2.destroy()#si calcul exact il reste 2 batons donc le jouruer a pas besoin
            choix3.destroy()#de choix2 et choix3
        elif B==1:
            vali2.destroy()
    res.after(2500,Jeu161)

def Jeu17():#ultime tour possible
    global B
    global J
    global I
    J=nombre.get()
    J=int(J)#int() : permet de modifier une variable en entier.
    print=(B)
    B=B-J
    J=str(J)
    B=str(B)
    j.configure(text="Vous avez pris "+J+" batons.")
    bat.configure(text="Il reste "+B+" batons.")
    ia.configure(text="")
    B=int(B)
    gagnant.configure(text="Vous avez gagné")
    vali2.destroy()

   
if C==1:#permet selon le résultat de pile/face de lancer la bonne condition
    vali2.config(command=Jeu2)#le joueur commence 
elif C==2:
    vali2.config(command=Jeu8)#l'IA commence

plateau=Label(batons, text="Plateau de jeu." , font=font6)
plateau.pack()

plateau2=Label(batons)#aspect visuel du jeu
plateau2.pack()

canvas=Canvas(batons,width=1140,height=250,background='brown')#canvas représentent les batons
ligne1=canvas.create_line(76,75,76,175,width=8,capstyle='round',fill='beige')
ligne2=canvas.create_line(128,75,128,175,width=8,capstyle='round',fill='beige')
ligne3=canvas.create_line(180,75,180,175,width=8,capstyle='round',fill='yellow')
ligne4=canvas.create_line(232,75,232,175,width=8,capstyle='round',fill='beige')
ligne5=canvas.create_line(284,75,284,175,width=8,capstyle='round',fill='green')
ligne6=canvas.create_line(336,75,336,175,width=8,capstyle='round',fill='beige')
ligne7=canvas.create_line(388,75,388,175,width=8,capstyle='round',fill='beige')
ligne8=canvas.create_line(440,75,440,175,width=8,capstyle='round',fill='red')
ligne9=canvas.create_line(492,75,492,175,width=8,capstyle='round',fill='beige')
ligne10=canvas.create_line(544,75,544,175,width=8,capstyle='round',fill='orange')
ligne11=canvas.create_line(596,75,596,175,width=8,capstyle='round',fill='beige')
ligne12=canvas.create_line(648,75,648,175,width=8,capstyle='round',fill='purple')
ligne13=canvas.create_line(700,75,700,175,width=8,capstyle='round',fill='beige')
ligne14=canvas.create_line(752,75,752,175,width=8,capstyle='round',fill='pink')
ligne15=canvas.create_line(804,75,804,175,width=8,capstyle='round',fill='beige')
ligne16=canvas.create_line(856,75,856,175,width=8,capstyle='round',fill='beige')
ligne17=canvas.create_line(908,75,908,175,width=8,capstyle='round',fill='grey')
ligne18=canvas.create_line(960,75,960,175,width=8,capstyle='round',fill='beige')
ligne19=canvas.create_line(1012,75,1012,175,width=8,capstyle='round',fill='silver')
ligne20=canvas.create_line(1064,75,1064,175,width=8,capstyle='round',fill='beige')
canvas.pack()



fenetre1.mainloop()
