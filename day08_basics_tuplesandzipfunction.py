# Day 8 - Codecademy Python 3
# [Tuples and zip function]
# Date: April 20, 2026

# ======================
# [SECTION 1 - Tuples]
# ======================

# ust like lists, tuples can hold a sequence of items and have a few key advantages:
# Tuples are more memory efficient than lists
# Tuples have a slightly higher time efficiency than lists

# because tuples are immutable

# tuples are defined with parentheses () with comma-separated values.

# tuples are capable of holding one item as long as it is followed by a comma
my_tuple = ('abc',)
# ... can hold objects of different data types. 
my_tuple = ('abc', 123, 'def', 456, 789, 'ghi')


# ======================
# [SECTION 2 - Tuple Indexing and Slicing]
# ======================

# Items in a tuple can be accessed with their index
print(my_tuple[0]) # prints abc

# We can also apply slicing
print(my_tuple[3:5]) # prints (456, 789)


# ======================
# [SECTION 3 - Common Built-in Functions]
# ======================

# len()
print(len(my_tuple)) # prints 6

# max()
# The built-in function max() returns the tuple’s maximum value.
# this requires all of the values to be of the same data type
my_tuple = (65, 2, 88, 101, 25)
max(my_tuple) # returns 101
 
my_tuple = ('orange', 'blue', 'red', 'green')
max(my_tuple) # returns "red"
 
my_tuple = ('abc', 234, 567, 'def')
max(my_tuple) # throws an error!

# min()
# The built-in function min() returns the tuple’s minimum value
my_tuple = (65, 2, 88, 101, 25)
min(my_tuple) # returns 2
my_tuple = ('orange', 'blue', 'red', 'green')
min(my_tuple) # returns "blue"
my_tuple = ('abc', 234, 567, 'def')
min(my_tuple) # throws an error!


#.index()
# The built-in method `.index()’ takes in a value as the argument to find its index in the tuple
my_tuple = ('abc', 234, 567, 'def')
my_tuple.index('abc') # returns 0
my_tuple.index(567) # returns 2

#.count()
# The built-in method `.count()’ takes in a value as the argument to find the number of occurrences in the tuple.
my_tuple = ('abc', 'abc', 2, 3, 4)
my_tuple.count('abc') # returns 2
my_tuple.count(3) # returns 1


# ======================
# [SECTION 4 - Zip function]
# ======================


# The zip() function allows us to quickly combine associated data-sets 
# without needing to rely on multi-dimensional lists. 

names = ["Jenny", "Alexus", "Sam", "Grace"]
heights = [61, 70, 67, 64]


# The zip() function takes two (or more) lists as inputs and returns an OBJECT that contains a list of pairs. 
# Each pair contains one element from each of the inputs.
names_and_heights = zip(names, heights)

converted_list = list(names_and_heights)
print(converted_list) 
# return [('Jenny', 61), ('Alexus', 70), ('Sam', 67), ('Grace', 64)]

# Our data set has been converted from a zip memory object to an actual list (denoted by [ ])

# Our inner lists don’t use square brackets [ ] around the values. This is because they have been converted into tuples 


# ======================
# CE QUE J'AI COMPRIS
# ======================

# - Les tuples sont des listes qu'on ne peut pas modifier.
# elles ont l'avantage d'être plus rapide
# on peut acceder aux item avec l'index et le slicing. on peut obtenir des infos avec diifentes fonction

# enfin, on peut assembler des liste ensemble avec la fonction zip !
