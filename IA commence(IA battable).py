import random

def Jeu1():
    B=20
    I=0
    J=0
    while B!=1:
        if B>4:
            I=random.randint(1,3)
            print("L'IA prends",I,"batons.")
            B=B-I
            print("Il reste",B,"batons.")
            #if B<=1:
                #print("Vous a perdu.")
                #break
            #else:

            print("Tour terminé,à vous de jouer.")
            J=input("Prenez entre 1 à 3 batons:")
            J=int(J)
            print("Vous avez pris",J,"batons.")
            B=B-J
            print("Il reste",B,"batons.")
            if B<=1:
                print("Vous avez gagné")
                break
            else:
                print("Tour terminé,à l'IA de jouer.")
        if B<=4:
            if B==4:
                I=3
                print("L'IA a pris",I,"batons.")
                B=B-I
                print("Il reste",B,"baton.")
                print("Vous avez perdu.")
                break
            if B==3:
                I=2
                print("L'IA a pris",I,"batons.")
                B=B-I
                print("Il reste",B,"baton.")
                print("Vous avez perdu")
                break
            if B==2:
                I=1
                print("L'IA a pris",I,"baton.")
                B=B-I
                print("Il reste",B,"baton.")
                print("Vous avez perdu")
                break
            #else:
                #print("Tour terminé,à vous de jouer.")
                #J=input("Prenez entre 1 à 3 batons:")
                #J=int(J)
                #print("Vous avez pris",J,"batons.")
                #B=B-J
                #print("Il reste",B,"batons.")
                #if B==1:
                  #  print("Vous avez gagné")
                   # break
                #else:
                 #   print("Tour terminé,à l'IA de jouer.")
         
           
        
            
Jeu1()








