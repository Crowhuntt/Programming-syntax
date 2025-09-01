#class

class Dog:
  kind = 'canine' # class variable shared by all instances
  def __init__(self, name):
    self.name = name # instance variable unique to each instance
    
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
