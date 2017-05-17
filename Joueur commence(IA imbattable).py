import random


def Jeu2():
    B=20
    I=0
    J=0
    if B!=1:
        J=input("Prenez entre 1 à 3 batons:")
        J=int(J)
        print("Vous avez pris",J,"batons.")
        B=B-J
        print("Il reste",B,"batons.")
        #if B<=1:#inutile
            #print("Vous avez gagné.")#inutile          
        #else: intutile
        print("Tour terminé,à l'IA de jouer.")
        if J==1:
                if B>1:#explication au procahin
                    I=2
                    print("L'IA a pris",I,"batons.")
                    B=B-I
                    print("Il reste",B,"batons.")
                    while B!=1:
                        J=input("Prenez entre 1 et 3 batons:")
                        J=int(J)
                        print("Vous avez pris",J,"batons.")
                        B=B-J
                        print("Il reste",B,"batons.")
                        if B<=1:
                            print("Vous avez gagné.")
                            break
                        else:
                            print("Tour terminé,à vous de jouer.")
                            if B==8:#faille du programme le rendant battable--->corrigé
                                I=3#
                                print("L'IA a pris",I,"batons.")#
                                B=B-I#
                                print("Il reste",B,"batons.")#
                            if B>6:#6 a la place de 4 car sinon lance la condition d au dessus et celle ci
                                I=4-J
                                print("L'IA a pris",I,"baton(s).")
                                B=B-I
                                print("Il reste",B,"batons.")
                            elif B<=4:                        
                                    if B==4:#mettre en fonction
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
                             
        if J==2:
                if B>1:#explciation au prochain
                    I=1
                    print("L'IA a pris",I,"batons.")
                    B=B-I
                    print("Il reste",B,"batons.")
                    while B!=1:
                        J=input("Prenez entre 1 et 3 batons:")
                        J=int(J)
                        print("Vous avez pris",J,"batons.")
                        B=B-J
                        print("Il reste",B,"batons.")
                        if B<=1:
                            print("Vous avez gagné.")
                            break
                        else:
                            print("Tour terminé,à vous de jouer.")
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
                            elif B<=4:
                                if B==4:
                                    I=3
                                    print("L'IA a pris",I,"batons.")
                                    B=B-I
                                    print("Il reste",B,"baton.")
                                    print("Vous avez perdu.")
                                    break
                                if B==2:
                                    I=1
                                    print("L'IA a pris",I,"batons.")
                                    B=B-I
                                    print("Il reste",B,"baton")
                                    print("Vous avez perdu")
                                    break
                                if B==3:
                                    I=2
                                    print("L'IA a pris",I,"batons.")
                                    B=B-I
                                    print("Il reste",B,"baton")
                                    print("Vous avez perdu")                          
                                    break
                          
        if J==3:
                if B>1:#corrige le bug,qui avec cette combinaison 2,3,2,3,3, faisait continuer le programme en dessous de 1 car le precedent J est egale a 3 ce qui l'active, bug pas compris mais resolu
                    I=3
                    print("L'IA a pris",I,"batons.")
                    B=B-I
                    print("Il reste",B,"batons.")
                    while B!=1:
                        J=input("Prenez entre 1 et 3 batons:")
                        J=int(J)
                        print("Vous avez pris",J,"batons.")
                        B=B-J
                        print("Il reste",B,"batons.")
                        if B<=1:
                            print("Vous avez gagné.")
                            break
                        else:
                            print("Tour terminé,à vous de jouer.")
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
                            elif B<=4:
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
                                    print("Vous avez perdu.")
                                    break
                                if B==2:
                                    I=1
                                    print("L'IA a pris",I,"baton.")
                                    B=B-I
                                    print("Il reste",B,"baton.")
                                    print("Vous avez perdu")
                                    break
                           
                       
Jeu2()
