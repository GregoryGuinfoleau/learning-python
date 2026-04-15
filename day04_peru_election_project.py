# Day 4 - Exercice perso
# Projet : Analyse des résultats du 1er tour des élections présidentielles 2021 du Pérou
# Date: April 15, 2026
# ======================
# SECTION 1 - Environnement virtuel (venv)
# ======================
# Un venv est une "bulle" isolée pour un projet Python.
# Il permet d'installer des bibliothèques sans toucher au système.
# Toujours l'activer avant de travailler :
#   python3 -m venv ~/DataScience/venv
#   source ~/DataScience/venv/bin/activate
# ======================
# SECTION 2 - Charger un fichier CSV avec pandas
# ======================
# pandas est une bibliothèque d'analyse de données.
# read_csv() ouvre un fichier CSV et le stocke dans un DataFrame (df).
# Paramètres importants :
#   encoding="latin-1"  → pour les fichiers avec accents en espagnol
#   sep=";"             → quand le séparateur est un point-virgule et non une virgule
# Exemple :
#   import pandas as pd
#   df = pd.read_csv("fichier.csv", encoding="latin-1", sep=";")
# ======================
# SECTION 3 - Explorer et analyser les données
# ======================
# df.head()    → affiche les 5 premières lignes
# df.columns   → affiche la liste exacte des colonnes
# Groupby + sum + sort_values : même logique qu'un GROUP BY / SUM / ORDER BY en SQL
# Exemple :
#   resultats = df.groupby("DEPARTAMENTO")["VOTOS_P16"].sum().sort_values(ascending=False)
#   print(resultats)
# ======================
# CE QUE J'AI COMPRIS
# ======================
# - Linux est sensible à la casse : "Resultados" ≠ "resultados"
# - Un fichier .csv peut utiliser ";" comme séparateur au lieu de ","
# - Si pandas voit une seule colonne, c'est souvent un problème de séparateur
# - Lima concentre un volume de votes massivement supérieur aux autres régions
# - Le fichier inclut la diaspora (Qatar, Roumanie...) — à filtrer pour l'analyse interne
# - La logique pandas est proche du SQL : groupby = GROUP BY, sum = SUM, sort_values = ORDER BY
# - Ce qui était difficile : la syntaxe pandas, le venv, les erreurs d'encodage
# ======================
# EXERCICE PRATIQUE
# ======================
# Prochaine étape : calculer le % de votes P16 par département
# (plutôt que les valeurs brutes, pour corriger le biais de Lima)