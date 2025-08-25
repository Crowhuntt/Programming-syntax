#tuple ()
# Immutable: Once created, elements cannot be modified
# Ordered: Maintains the order of elements
# Allows Duplicates: Can contain duplicate values
# Heterogeneous: Can store different data types

tuple = 12345, 54321, 'hello!'
tuple = (12345, 54321, 'hello!')

tuple[0]
# 12345

new = tuple, (1, 2, 3, 4, 5) # Nest 
new
# ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

tuple[0] = 88888 # ERROR! Inmutable. Elements cannot be modified
# TypeError: 'tuple' object does not support item assignment

empty = () # Initialize a tuple with 0 elements
singleton = 'hello', # Initialize a tuple with 1 element
