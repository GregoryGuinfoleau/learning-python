# Day02 - Codecademy Python 3
# Project Initials ASCII and Customer's receipt
# Date: April 9, 2026

# ======================
# [SECTION 1 - 2 basics projects]
# ======================

# D'abord, j'ai été invité à faire de l'art ASCII. L'objectif était d'afficher ses initiales
# avec du code.

# name = gregory guinfoleau
# fun_anecdote = "I cheated on a Python admission test using AI because I was afraid 
# of failing. I felt so guilty that I confessed to the examiner the next week.
# He appreciated my honesty and let me retake it - and I'm now studying
# to pass it for real!"

initial = "G"

print(" " + initial*3 + " " + " "*2 + initial*3 + " ")
print(initial + " "*3 + initial + " " + initial + " "*3 + initial)
print(initial + " "*5 + initial)
print(initial + " " + initial*3 + " " + initial + " " + initial*3)
print(initial + " "*3 + initial + " " + initial + " "*3 + initial)
print(initial + " "*3 + initial + " " + initial + " "*3 + initial)
print(" " + initial*3 + " " + " "*2 + initial*3 + " ")




# Ensuite, customer's receipt :

lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00

stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15

sales_tax = .088

customer_one_total = 0
customer_one_itemization = ""


customer_one_total += lovely_loveseat_price
customer_one_itemization += (lovely_loveseat_description +" ")

customer_one_total += luxurious_lamp_price
customer_one_itemization += (luxurious_lamp_description)

customer_one_tax = customer_one_total*sales_tax

customer_one_total += customer_one_tax

print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)

# pour ajouter des éléments à une variable, utiliser le +=

# ======================
# [SECTION 2 - Interaction with user]
# ======================

# we can assign variables with user input
# The input() function requires a prompt message, 
# which it will print out for the user before they enter 
# the new information
# Exemple :

favorite_fruit = input("What is your favorite fruit? ")
# What is your favorite fruit? mango

print("Oh cool! I like " + favorite_fruit + " too, but I think my favorite fruit is apple.")
# Oh cool! I like mango too, but I think my favorite fruit is apple.


# ======================
# [SECTION 3 - Boolean expressions and Relational Operators]
# ======================


# A Boolean expression is a statement that can either be true or false. 
# The statement must be answered by true or false only, and it must be verifiable
# with evidence. It cannot rely on interpretation or opinion.

# Exemple :
# The Earth revolves around the Sun. this is a boolean statement
# Chocolate ice cream tastes better than vanilla. this is an opinion

# - Relational operators compare two values and return True or False based 
# on the operands. 
# For this reason, they're called comparison operators.

1 == 1     # Evaluates to True as the operands are the same 

1 != 1     # Evaluates to False as the operands are the same 

2 != 4     # Evaluates to True as the operands are different 

3 == 5     # Evaluates to False as the operands are different
 
'7' == 7   # Evaluates to False as the operands are different types 

2 > 1      # greater than
2 >= 2     # greater than or equal to
3 < 4      # less than
3 <= 3     # less than or equal to

# - Logical operators are used to combine multiple Boolean expressions.
# --> and : combines two boolean expressions and evaluates
#  as True if both its components are True, but False otherwise.

# Exemple :
credits = 120
gpa = 3.4

if credits >= 120 and gpa >= 2.0 :
  print("You meet the requirements to graduate!")

# --> or : combines two expressions into a
# larger expression that is True if either component is True.

# Exemple :
credits = 118
gpa = 2.0

if credits >= 120 or gpa >= 2.0 :
  print("You have met at least one of the requirements.")




# ======================
# [SECTION 4 - If Statement]
# ======================

# Understanding boolean variables and expressions is essential because they are the building blocks of
# conditional statements

# Conditionals take an expression, 
# which is code that evaluates to determine a value, 
# and checks if it is True or False. If it’s True, 
# we can tell our program to do one thing — 
# we can even account for False to do another. 
# As we write more complex programs, conditionals allow
# us to address multiple scenarios and make our programs
# more robust. 

# The Python if statement is used to determine the execution 
# of code based on the evaluation of a Boolean expression.
#  - If the if statement expression evaluates to True, 
# then the indented code following the statement 
# is executed. - If the expression evaluates to
#  False then the indented code following the if 
# statement is skipped and the program executes the next 
# line of code which is indented at the same level 
# as the if statement.

# Exemple :

user_name = 'angela_catlady_87'

if user_name == "Dave":
  print("Get off my computer Dave!")

if user_name == "angela_catlady_87":
  print("I know it is you, Dave! Go away!"
)



# ======================
# CE QUE J'AI COMPRIS
# ======================

# ✅ Points clés retenus :
# - Multiplication de strings : "G"*3 répète le caractère 3 fois
# - Opérateur += pour ajouter à une variable (x += 5 équivaut à x = x + 5)
# - input() demande à l'utilisateur d'entrer quelque chose
# - Boolean : True ou False, utilisé pour les conditions
# - Opérateurs de comparaison : == (égal), != (différent), >, <, >=, <=
# - if statement : exécute du code seulement si la condition est True
# - Indentation importante en Python : le code indenté fait partie du if

# 📝 À revoir :
# - Les opérateurs logiques 'and', 'or', 'not' (pas encore totalement à l'aise)
# - Comment combiner plusieurs conditions dans un if
