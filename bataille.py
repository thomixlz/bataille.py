"""
=== Règles : ===

- On distribue les 52 cartes du paquets aux joueurs. (26 cartes par joueur).
- Chacun tire la carte du dessus de son paquet et la montre
- Celui qui a la carte la plus forte ramasse les autres cartes.

- Lorsque deux joueurs posent en même temps deux cartes de même valeur il y a "bataille". Les 2 cartes sont supprimés de la partie 

- Le gagnant est celui qui remporte toutes les cartes du paquet.

=== Infos : ===

L'as est la plus forte carte, puis roi, dame, valet, 10, 9, 8, 7, 6, 5, 4, 3, 2 

======================================================================================================================
======================================================================================================================
======================================================================================================================
======================================================================================================================

"""


CROUGE = '\033[91m'
CJAUNE = "\033[33m"
CVERT = "\033[32m"
CBLEU = "\033[34m"
CGRIS = "\033[90m"
CVIOLET = "\033[94m"

CSOULIGNE = "\033[4m"

CEND = '\033[0m'

#############################################################
#################   OUTILS DE BASE         ##################
#############################################################

formeDesCartes = ['Coeur', 'Carreau', 'Pique', 'Trèfle']
nomDesCartes = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
valeurDesCartes = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,'9': 9, '10': 10, 'Valet': 11, 'Dame': 12, 'Roi': 13, 'As': 99}


import random
from itertools import product


# Fonction : Création de mon deck de carte avec 52 cartes

def creationDuDecks(liste_formesDesCartes,liste_nomDesCartes):
    monDeck = []
    for suite, rank in product(liste_formesDesCartes,liste_nomDesCartes):
         monDeck.append((rank,suite))
    return monDeck


# Fonction : Melange mon Deck de 52 cartes

def melangeDeck(monDeck):
    random.shuffle(monDeck)
    return monDeck


#Fonction : Sépare mon Deck en 2 Deck de 26 cartes

def separeDeck(monDeck):
    moitierListe = len(monDeck)//2
    return monDeck[:moitierListe], monDeck[moitierListe:]


#Fonction : Recupère la valeur de la carte

def value(maCarte,dic_valeurDesCartes): 
        return dic_valeurDesCartes.get(maCarte[0])


#############################################################
#################  LE JEU DE LA BATAILLE  ###################
#############################################################

#Appel : Création du deck de 52 cartes
monDeckPrincipal = creationDuDecks(formeDesCartes,nomDesCartes)

#Appel : Mélange mon deck de 52 cartes
monDeckPrincipalMelange = melangeDeck(monDeckPrincipal)

#Appel: Sépare mon Deck mélanger en 2 deck de 26 cartes : 
deckJoueur1, deckJoueur2 = separeDeck(monDeckPrincipalMelange)


compteurTour = 1
bataille = True

while len(deckJoueur1) > 0 and len(deckJoueur2) > 0 :


    #### INFO DE PARTIE ####
    
    print(CJAUNE + "[ Manche",compteurTour,"]"+ CEND)
    print(CVIOLET + "Nombre de cartes restantes Joueur 1 = ", len(deckJoueur1), "!" + CEND)
    print(CVIOLET + "Nombre de cartes restantes Joueur 2 = ", len(deckJoueur2), "!\n" + CEND)

    #Tir la première carte du deck du JOUEUR 1 (Carte du dessus)

    carteJoueur1 = deckJoueur1[0]

    print(CBLEU + "JOUEUR 1 =" + CEND)
    print("[ Carte",compteurTour,"] =", carteJoueur1[0], "de",carteJoueur1[1], "!\n")

    print(CROUGE + "VS\n" +CEND)

    #Tir la première carte du deck du JOUEUR 2 (Carte du dessus)

    carteJoueur2 = deckJoueur2[0]


    print(CBLEU + "JOUEUR 2 =" + CEND)
    print("[ Carte",compteurTour,"] =", carteJoueur2[0], "de",carteJoueur2[1], "!\n")

    #Calcul la value de la carte du JOUEUR 1

    valeurCarteJoueur1 = value(carteJoueur1,valeurDesCartes)

    #Calcul la value de la carte du JOUEUR 2

    valeurCarteJoueur2 = value(carteJoueur2,valeurDesCartes)

    #Supprime donc du deck la carte piocher par le JOUEUR 1

    deckJoueur1.pop(0)

    #Supprime donc du deck la carte piocher par le JOUEUR 2

    deckJoueur2.pop(0)

    #Ajoute les cartes au gagnant

    if valeurCarteJoueur1 > valeurCarteJoueur2:
        deckJoueur1.append(carteJoueur1)
        deckJoueur1.append(carteJoueur2)
        print(CVERT + "Le joueur 1 à gagné la manche",compteurTour, "!\n" + CEND)
        print("=======================================================================\n")

    elif valeurCarteJoueur2 > valeurCarteJoueur1:
        deckJoueur2.append(carteJoueur2)
        deckJoueur2.append(carteJoueur1)
        print(CVERT +"Le joueur 2 à gagné la manche",compteurTour, "!\n"+ CEND)
        print("=======================================================================\n")
            

    else : 
        print(CVERT + "Bataille ! Les 2 cartes sortent de la partie\n" + CEND)
        print("=======================================================================\n")

    compteurTour += 1


if len(deckJoueur1) == 0:
    print(CSOULIGNE + "|||||||||||| JOUEUR 2 WIN ||||||||||||\n" + CEND)
else : print(CSOULIGNE + "|||||||||||| JOUEUR 1 WIN ||||||||||||\n" + CEND)

