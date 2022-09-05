
#!/usr/bin/env python

# -*- coding: utf-8 -*-


import random


# - - - - - - - - - - - - - - - - - -

# Déclarations des classes

# - - - - - - - - - - - - - - - - - -


class Personnage:

    "Ceci est une classe permettant de créer un personnage dans mon super RPG"


    def __init__(self) :

        self.nom = 'nobody'

        self.prenom = 'nobody'

        self.niveau = 0

        self.classe = 'aucune classe'


    def presentation(self) :

        "Affiche quelques unes des valeurs stockées dans le personnage"

        print(self.nom, ' ',self.prenom)

        print(self.classe, ' de niveau ',self.niveau)


    def perdre_un_niveau(self) :

        "Cette méthode permet de réduire le niveau de 1"

        self.niveau +=-1


    def combat(self,adversaire) :

        "Ceci est une méthode qui renvoie le nom du combattant qui perd"

        perdant = ''

        test = True

        while test :

            valeur1 = random.randint(1,6)+self.niveau

            valeur2 = random.randint(1,6)+adversaire.niveau

            if valeur1>valeur2 :

                perdant = adversaire

                test = False

            elif valeur2>valeur1 :

                perdant = self

                test = False

        perdant.perdre_un_niveau()

        return(perdant)


# - - - - - - - - - - - - - - - - - -

# Déclarations des fonctions

# - - - - - - - - - - - - - - - - - -


# - - - - - - - - - - - - - - - - - -

# Corps du programme

# - - - - - - - - - - - - - - - - - -


bob_skywalker = Personnage()

bob_skywalker.nom = "Skywalker"

bob_skywalker.prenom = "Bob"

bob_skywalker.niveau = 1

bob_skywalker.classe = "Jedi raté"


perso2 = Personnage()

perso2.nom = "De nom je n'ai pas"

perso2.prenom = "Yoda"

perso2.niveau = 3

perso2.classe = "Vieux Jedi"


print(bob_skywalker.combat(perso2).nom, " vient de perdre un combat")

print(bob_skywalker.combat(perso2).nom, " vient de perdre un combat")