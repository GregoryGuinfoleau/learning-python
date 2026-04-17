# Day 6/7 - Codecademy Python 3
# Lists and methods
# Date: April 16/17, 2026

# ======================
# [SECTION 1 - Lists methods]
# ======================

# .insert() allows to add an element to a 
# specific index in a list. 
# The .insert() method takes in two inputs:
#  - The index you want to insert into.
#  - The element you want to insert at the specified index.

# Exemple :
civilisations = ["Paijanense", "Mochica", "Chimu", "Inca"]
print(civilisations)
civilisations.insert(3, "Chachapoyas") 
print(civilisations)


# The .pop() method in Python removes an element
# from a list at a specif#ied index and returns that element.
# It takes one input, the index for the element I wnat to remove

# Ex : 
civilisations.pop(1) # -> va retirer "mochica"
print(civilisations)

# si on ne met pas d'index comm ceci civilisation.pop(), ca retirera le dernier élement


# ======================
# [SECTION 2 - Fonction Range]
# ======================

# Pour créer facilement une liste de chiffres, plutôt que de le staper un par un, il existe la
# fonction range()
# 
# Exemple :
zerotoseven = range(8)
print(list(zerotoseven))

#  2 choses
# - l'input encodé doit être 1 en plus que le dernier chiffre de la liste désiré
# - la fonction créé un objet. 
# En effet si on avait ecrit print(zero_to_seven), le résultat aurait été
# range(0,8) --> ce qu'on appelle un range object
# si on veut voir le résultat en forme de liste, 
# il faut utiliser la fonction list pour convertir l'objet en liste. 

# on peut aussi choisir que la liste démarre et termine a un chiffe particulier. Dans ce cas, on utilise alors 2 input
troisaquinze = range(3, 16)
print(list(troisaquinze))

# Autre option, on peut ajouter une troisième valeur qui "sautera" 
# la suite de chiffre selon la valeur désirée

troisaquinzesaute = range(3,16,3)
print(list(troisaquinzesaute))

# il sortirait [3,6,9,12,15]

# ======================
# [SECTION 3 - fonction len()]
# ======================

# Pour savoir combine il y a d'item dans une liste, il existe 
# la fonction len()
# Exemple :
troisaquinzesaute_len = len(troisaquinzesaute)
print(troisaquinzesaute_len) # on obtiendrait certainement 5

# ======================
# [SECTION 4 - slicing a list]
# ======================

# Pour extraire une partie d'une liste, il existe le slicing
troisaquinze_sliced = troisaquinze[4:10]
print(list(troisaquinze_sliced))
# même principe, l'index de la valeur première pour le début de liste désiré
# deuxième valeur, valeur désiré + 1.

# Il est aussi possible de sélectionner les x premiers éléments d'une liste
# ex :
premiers_elements = troisaquinze[:3]
print(list(premiers_elements))
# Cela nous donnera les les éléments de l'index 0 jusqu'à 2 (l'index 3 est exclu)

# Même principe pour sélectionner les x derniers éléments d'une liste
# ex :
derniers_elements = troisaquinze[-3:]
print(list(derniers_elements))
# ici le code coupe de l'éléments -3 jusqu'au dernier éléments de la liste
# ici , nous aurions donc [13, 14, 15]

# Enfin on peut choisir la liste moins  x derniers éléments
# ex:
liste_moins_derniers_elements = troisaquinze[:-2]
print(list(liste_moins_derniers_elements))


# ======================
# [SECTION 4 - method .count]
# ======================

# Sin on veut compter combine d'occurence d'un item il y a dans un liste
# on peut utiliser .count
# Ex:
votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]
jake_votes = votes.count("Jake")
print(jake_votes)
#

# ======================
# [SECTION 5 - method .sort]
# ======================

# Avec cette méthode, il est possible de classer les items d'une liste par ordre alphabétique,
# numérique. Par défaut, l'ordre se fait de manière ascendante.
# Ex :
civilisations.sort()
print(civilisations)
# pour faire de manière descendante, ajouter la valeur reverse
civilisations.sort(reverse=True)
print(civilisations)

# ======================
# [SECTION 5 - fonction sorted()]
# ======================

# La fonction sorted() est différente de la méthod .sort
# niveau syntaxe, la fonction vient avant la liste
# elle produit une nouvelle liste plutôt que la modifier

# ex:
civilisations_sorted = sorted(civilisations)
print(civilisations_sorted)


# ======================
# CE QUE J'AI COMPRIS
# ======================

# une méthode modifie la liste choisie
# une fonction elle produit une valeur attribuable à une variable
# - Point clé 2
# - Point clé 3
# - Ce qui était difficile / ce que je veux revoir

# ======================
# EXERCICE PRATIQUE (optionnel)
# ======================

# Si je veux tester ce que j'ai appris avec un exercice perso