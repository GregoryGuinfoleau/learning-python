# Day 1 - Codecademy Python 3
# Data Types & Basic Operations
# April 8, 2026

# ======================
# DATA TYPES
# ======================

# Integer (nombres entiers)
age = 32
surf_sessions = 5

# Float (nombres décimaux)
water_temp = 18.5
wave_height = 1.2

# String (texte)
city = "Lima"
country = "Peru"

# Boolean (vrai/faux)
is_sunny = True
too_cold = False


# ======================
# BASIC OPERATIONS
# ======================

# Addition, soustraction, multiplication, division
result = 10 + 5      # 15
result = 10 - 3      # 7
result = 4 * 3       # 12
result = 10 / 2      # 5.0

# Puissance (**)
squared = 5 ** 2     # 25 (5 au carré)
cubed = 2 ** 3       # 8 (2 au cube)

# Modulo (%) - reste de la division
reste = 10 % 3       # 1 (10 divisé par 3 = 3, reste 1)
reste = 15 % 4       # 3 (15 divisé par 4 = 3, reste 3)


# ======================
# STRING CONCATENATION
# ======================

# Assembler des strings avec +
first_name = "Gregory"
last_name = "Guinfoleau"
full_name = first_name + " " + last_name
print(full_name)     # Gregory Guinfoleau

# Répéter un string avec *
laugh = "ha" * 3
print(laugh)         # hahaha


# ======================
# MULTI-LINE STRINGS
# ======================

# String sur plusieurs lignes avec triple quotes
long_text = """
Ceci est un texte
qui prend plusieurs lignes
et garde sa mise en forme
"""
print(long_text)


# ======================
# COMMENTS
# ======================

# Ceci est un commentaire sur une ligne
# Les commentaires sont ignorés par Python
# Ils servent à expliquer le code

# Il n'y a pas de commentaire multi-lignes officiel en Python
# Mais on peut utiliser """ pour ça (même si techniquement
# c'est un string qui n'est assigné à rien) """


# ======================
# CE QUE J'AI COMPRIS
# ======================

# - Python a plusieurs types de données de base
# - On peut faire des calculs mathématiques directement
# - Le modulo (%) est utile pour savoir si un nombre est pair/impair
# - Les strings peuvent être assemblés avec +
# - Les commentaires avec # aident à documenter le code
