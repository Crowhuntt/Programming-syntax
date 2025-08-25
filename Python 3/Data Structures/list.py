#list []

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple') # Return the number of times x appears in the list
# 2

fruits.index('banana') # Return zero-based index in the list of the first item whose value is equal to x
# 3

ruits.reverse() # Reverse the elements of the list in place
fruits
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

fruits.append('grape') # Add an item to the end of the list

fruits.insert(index, value) # Insert an item at a given position.

fruits.sort() # Sort the items of the list in place
fruits
# ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

fruits.pop() # Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list.
# 'pear'

del fruits[0] # Remove an item from a list given its index. Differs from pop() because doesn't return any value
del fruits[2:4]

fruits.remove('orange') # Remove the first item from the list whose value is equal to x

fruits.clear() # Remove all items from the list

fruits.copy() # Return a shallow copy of the list
