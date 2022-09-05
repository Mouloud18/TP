#!/usr/bin/env python

# -*- coding: utf-8 -*-


import mes_classes


# - - - - - - - - - - - - - - - - - -

# Corps du programme

# - - - - - - - - - - - - - - - - - -


bob_skywalker = mes_classes.Personnage()

bob_skywalker.nom = "Skywalker"

bob_skywalker.prenom = "Bob"

bob_skywalker.niveau = 1

bob_skywalker.classe = "Jedi raté"


print("On crée bob_skywalker et l'identifiant de l'objet est ",id(bob_skywalker))


perso2 = mes_classes.Personnage()

perso2.nom = "Skywalker"

perso2.prenom = "Bob"

perso2.niveau = 1

perso2.classe = "Jedi raté"


print("On crée perso2 et l'identifiant de l'objet est ",id(perso2))


print(bob_skywalker==perso2)


input("Appuyer sur ENTREE")