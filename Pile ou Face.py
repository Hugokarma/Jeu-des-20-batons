import random
nom1=input("entrez votre nom : ") 
choix=input ("entrez pile ou face : ")


piece=random.randint(1,2)
if piece == 1:
    print("pile")
    if choix == "pile" :
        print("vous commencez")
    else :
        print("l'ordinateur commence")
else :
    print("face")
    if choix == "face" :
        print("vous commencez")
    else :
        print("l'ordinateur commence")


