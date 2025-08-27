#dictionary
# Ordered: Maintains the order of elements
# Mutable: Elements can be modified after creation
# Unique Elements: Duplicate values are automatically removed
# Heterogeneous: Can store different data types

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127 # append
tel
# {'jack': 4098, 'sape': 4139, 'guido': 4127}
tel['jack']
# 4098

del tel['sape'] # delete
tel['irv'] = 4127 # append
tel
# {'jack': 4098, 'guido': 4127, 'irv': 4127}

# Performing list(dict) on a dictionary returns a list of all the keys used in the dictionary, in insertion order
list(tel)
# ['jack', 'guido', 'irv']

# if you want it sorted, just use sorted(dict) instead
sorted(tel)
# ['guido', 'irv', 'jack']

# To check whether a single key is in the dictionary, use the in keyword.
'guido' in tel
# True
'jack' not in tel
# False

#######################################################################################
