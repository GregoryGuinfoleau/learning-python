# Day 03 - Codecademy Python 3
# [Boolean suite]
# Date: April 10 2026

# ======================
# [SECTION 1 - Boolean operators suite]
# ======================

# --> not
# when applied to any boolean expression it reverses the boolean value
# Exemple :
credits = 120
gpa = 1.8

if not credits >= 120 :
  print("You do not have enough credits to graduate.")
if not gpa >= 2.0 :
  print("Your GPA is not high enough to graduate.")
if not credits >= 120 and not gpa >= 2.0 :
  print("You do not meet either requirement to graduate!")


# ======================
# [SECTION 2 - Else statement]
# ======================

# else statements allow us to elegantly describe what we want our 
# code to do when certain conditions are not met.

# it always appear in conjunction with if statements.

# Exemple :
credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else:
  print("You do not meet the requirements to graduate.")



# ======================
# [SECTION 3 - elif statements]
# ======================



# We can use elif statements to control the order we want our program 
# to check each of our conditional statements. 
# First, the if statement is checked, then each elif statement is 
# checked from top to bottom, then finally the else code is executed
# if none of the previous conditions have been met.



# Exemple :

grade = 86

if grade >= 90 :
  print("A")
elif grade >= 80 :
  print("B")
elif grade >= 70 :
  print("C")
elif grade >= 60 :
  print("D")
else:
  print("F")




# ======================
# CE QUE J'AI COMPRIS
# ======================

# les conditions if, elif, else paraît très puissant.
# les opérateurs aussi. la gymnastique logique du not n'est pas évidente pour moi


# - J'ai eu du mal avec mon dernier exercice, j'ai confondu == et =
# pour rappel = attribue une valeur ; == regarde si c'est la même valeur
# - J'ai eu difficile pour concatener la phrase et les variables, j'avais 
# mis des + au départ, qui ne focntionnent qu'avec des 'string'

# ======================
# EXERCICE PRATIQUE (optionnel)
# ======================

print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

# Write an if statement below:
if planet == 1:
  weight = (weight*0.91)/2.205
  planet_name = "Venus"
elif planet == 2:
   weight = (weight*0.38)/2.205
   planet_name = "Mars"
elif planet == 3:
  weight = (weight*2.34)*0.4536
  planet_name = "Jupiter"
elif planet == 4:
  weight = (weight*1.06)/2.205
  planet_name = "Saturn"
elif planet == 5:
  weight = (weight*0.92)/2.205
  planet_name = "Uranus"
elif planet == 6:
  weight = (weight*1.19)*0.4536
  planet_name = "Neptune"

print("Cody's weight on", planet_name, ":", weight, "kg")