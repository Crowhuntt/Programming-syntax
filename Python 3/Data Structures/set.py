#set {}
# Mutable: Elements can be added or removed
# Unordered: Does not maintain the order of elements
# Unique Elements: Duplicate values are automatically removed
# Heterogeneous: Can store different data types

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # duplicates have been removed
# {'orange', 'banana', 'pear', 'apple'}

'orange' in basket
# True
'berry' in basket
# False

a = set('abracadabra') # str to set
# {'a', 'r', 'b', 'c', 'd'}
b = set('alacazam')
# {'r', 'd', 'b'}
a & b 
# {'a', 'c'}

# List comprehension example
a = {x for x in 'abracadabra' if x not in 'abc'} # set of 'abracadabra' = {'a', 'r', 'b', 'c', 'd'} with if condition
a
# {'r', 'd'}
