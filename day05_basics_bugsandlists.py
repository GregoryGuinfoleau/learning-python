# Day 4 - Codecademy Python 3
# [Titre du sujet - Bugs]
# Date: April 15, 2026

# ======================
# [SECTION 1 - Errors or bugs]
# ======================

# SyntaxError: Error caused by not following the proper structure (syntax) of the language.
# NameError: Errors reported when the interpreter detects a variable that is unknown.
# TypeError: Errors thrown when an operation is applied to an object of an inappropriate type.



# ======================
# [SECTION 2 - List]
# ======================

# a list is one of the many built-in data structures that allows us to work with a collection of data in sequential order.
# A list begins and ends with square brackets ([ and ]).
# Each item is separated by a comma (,)
# It’s considered good practice to insert a space ( ) after each comma, but the code will run just fine even without the space.
# Lists can contain any data type

# Exemple : mixed_list_common = ["Mia", 27, False, 0.5]

# A list doesn’t have to contain anything. We can create an empty list because we’re planning on filling it up later based on some other input.

# En utilisant une "method", on peut par exemple ajouter un élément à une liste, ou en enlever

# Exemple :
ma_liste_course["banane", "fromage", "petit pois"]
ma_liste_course.append("bières")
ma_liste_course.remove("petit pois")

# On peut additionner des listes ensemble avec +
# liste1 = [1, 2, 3]
# liste 2 = [4, 5, 6]
# liste 3 = liste1 + liste2
# on peut également rajouter un élément avec le + et des []. Ex : liste4 = liste3 + [7]

# On peut aussi, mettre une liste dans une liste !
# Ex : Civilisations_Perou = [["Paijanense", -10000], ["Mochica", 100], ["Chimu", 900], ["Inca", 1400]] 

# On peut accéder à un élément d'un sous liste : epoque_mochica = Civilisations_Perou[1][1]

