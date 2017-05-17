from tkinter import *
import random
import tkinter.font as tkFont


pf=Tk()#pf=pileface
pf['bg']='white'
pf.title('Twenty sticks')

font3=tkFont.Font(family="Times", size="14", slant="italic", underline="1")
font4=tkFont.Font(family="Times", size="12")
font5=tkFont.Font(family="Times", size="12", slant="italic")
font6=tkFont.Font(family="Times", size="18", slant="italic", underline="1")

pileface2=Frame(pf,padx=250, pady=250, borderwidth=2, relief=GROOVE)
pileface2.grid(row=0, column=0, padx=15, pady=15)

question1=Label(pileface2, text="Joueur 1, entrez votre nom :")
question1.grid(row=2,column=1,padx=25,pady=15)
question1.configure(font=font3)


reponse1= Entry(pileface2)
reponse1.grid(row=2,column=2)

question2=Label(pileface2, text="Joueur 2, entrez votre nom :")
question2.grid(row=2,column=3,padx=25,pady=15)
question2.configure(font=font3)
reponse2= Entry(pileface2)
reponse2.grid(row=2,column=4)
#""" docstrings""" indqiue fonction d'une fontion


def nom1(evenement):#focntion pour que le joueur 1 entre son nom
    global nom12
    nom12=reponse1.get()
    print(nom12)
    player1.configure(text=reponse1.get())
    #nom1=str(nom1)
    choi.configure(text=nom12+' Choississez entre pile et face :')
    return nom12# problème pour ressortir le nom que le joueur a entré, soit le nom de la fonction s'affiche
#même quand il n'y  a pas de global ou alors la méthode de la global ne marche, je n'ai pas reussi a corriger ce problème
#si cela est corrige il ne rest plus qu'a mettre la derniere fonction dans l'interface graphique et le programme marche
#Puis il faudra réussir à ouvrir ces fenetre et leurs fonctions avec un bouton dans l'interface du programme final 
reponse1.bind("<Return>",nom1)

player1=Label(pileface2, text="Joueur 1")
player1.grid(row=3, column=2, padx=15,pady=15)
player1.configure(font=font4)



def nom2(event):#focntion pour que le joueur 2 entre son nom
    global nom2#même problème pour la variable 
    nom2=reponse2.get()
    print(nom2)
    player2.configure(text=reponse2.get())  
reponse2.bind("<Return>",nom2)

player2= Label(pileface2, text="Joueur 2")
player2.grid(row=3, column=3, padx=15,pady=15)
player2.configure(font=font4)

choi=Label(pileface2, text='JOUER 1Choississez entre pile et face :')#mettrre nom1 en var
choi.grid(row=4, column=1,padx=15,pady=15)
choi.configure(font=font3)


piec=0
def pile1():#le joueur 1 choisi pile ou face cette fonction est qd le J1 choisis pile
    global piec#face sera donc associé au J2
    piec=1
    print (piec)
    butonpile.destroy()#enleve bouton 
    butonface.destroy()
    ls.configure(text='JOueur 1 choisi pile.')#indique qui prends pile
    ls2.configure(text='joeuru 2 choisi face.')#indique quu prends l'autre joueur

def face2():#le joueur 1 choisi pile ou face cette fonction est qd le J1 choisis face
    global piec#pile sera donc associé au J2
    piec=2
    print (piec)
    butonpile.destroy()#enleve bouton
    butonface.destroy()
    ls.configure(text='JOueur 1 choisi face.')#indique qui prends pile
    ls2.configure(text='joeuru 2 choisi pile.')#indique que prends l'autre joueur

def commencer2():#fonction fait tirage activer par le bouton lancer, elle détermine qui remporte le pile ou face
    ls.destroy()# et donc qui joue en premier
    ls2.destroy()
    piec=random.randint(1,2)
    resu=Label(pileface2, text=piec, font=font4)#met label a la place
    resu.grid(row=4, column=2, padx=15,pady=5)
    if piec==1:
        gagnant=Label(pileface2, text='JOUER 1 commence à jouer', font=font4)
        gagnant.grid(row=4,column=3,padx=5,pady=5)
    elif piec==2:
        gagnant=Label(pileface2, text='JOUER 2 commence à jouer', font=font4)
        gagnant.grid(row=4,column=3,padx=5,pady=5)
        

ls=Label(pileface2, font=font4)
ls.grid(row=4, column=2,padx=15,pady=15)
ls2=Label(pileface2, font=font4)
ls2.grid(row=4, column=3,padx=15,pady=15)

butonpile=Button(pileface2, text='Pile', command=pile1, borderwidth=5, relief=RIDGE)
butonpile.grid(row=4,column=2) 
butonpile.configure(font=font5)


butonface=Button(pileface2, text='Face', command=face2, borderwidth=5, relief=RIDGE)
butonface.grid(row=4,column=3)
butonface.configure(font=font5)

butonlancer=Button(pileface2, text='Tirage', command=commencer2, font=font5, borderwidth=5, relief=RIDGE)
butonlancer.grid(row=5,column=2)


butonpartie=Button(pileface2, text='Lancer la partie', command=pf.destroy, font=font5, borderwidth=7, relief=GROOVE)
butonpartie.grid(row=5, column=3)

pf.mainloop()

game=Tk()
game['bg']='white'
game.title('Twenty sticks to die')




res2=Frame(game,padx=50,pady=50, borderwidth=2, relief=GROOVE)
res2.grid()
batons2=Frame(game,padx=110,pady=80, borderwidth=2, relief=GROOVE)
batons2.grid()

player1=Label(res2, text="salut")
player1.grid()

B=20
J1=0
J2=0

def Jeu3():# focntion de jeu principal fonctionnel mais pas relié à une interface graphique
    global B
    global J1
    global J2
    while B!=1:
        print("A"" de jouer !")
        J1=input("Prenez entre 1 et 3 batons.")
        J1=int(J1)
        B=B-J1
        print(nom1," a pris",J1,"batons,il reste",B,"batons.")#problème de variable nom1
        if B==1:
            print(nom1,"a gangné !!!")#problème de variable nom1
            break
        elif B!=1:
            print("Votre tour est terminé")
        else: 
            print("A",nom2," DE joue")#problème de variable nom2
            J2=input("Prenez entre 1 et 3batons")
            J2=int(J2)
            B=B-J2
            print(nom2," a pris",J1,"batonsil reste",B,"batons")
            if B==1:
                print(nom2," a gagne")#problème de variable nom2
                break
            elif B!=1:
                print("Votre tour est termine")
Jeu3()
canvas=Canvas(batons2,width=1140,height=250,background='brown')#aspect visuelle des batons
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

re.mainloop()
