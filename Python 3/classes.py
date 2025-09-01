#class

class Dog:
  kind = 'canine' # class variable shared by all instances
  def __init__(self, name): # instance variable unique to each instance
    self.name = name 
  def add_trick(self, trick): # instance function
    self.tricks.append(trick)
    
d = Dog('Fido')
e = Dog('Buddy')
d.kind
# 'canine'
e.kind
# 'canine'
d.name
# 'Fido'
e.name
# 'Buddy'
d.add_trick('roll over')
d.tricks
# ['roll over']

#######################################################################################
#iter - The iter() function returns an iterator object that defines the method __next__() which accesses elements in the container one at a time

s = 'abc'
it = iter(s)
it
# <str_iterator object at 0x10c90e650>
next(it)
# 'a'
next(it)
# 'b'
next(it)
# 'c'
next(it)
# Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#    next(it)
# StopIteration
