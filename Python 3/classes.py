#class

class Dog:
  """A simple example class""" # Docstrings - Documentation
  kind = 'canine' # class variable shared by all instances
  def __init__(self, name): # instance variable unique to each instance. Class instantiation automatically invokes __init__() for the newly created class instance
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
#Inheritance

class Person: # Class
  def __init__(self, name):
    self.firstname = name
  def printname(self):
    print(self.firstname)
    
class Student(Person): # Class that inherits from Person
  pass

x = Student("Mike") # Create an instance of Person
x.printname()
# 'Mike'

# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function
class Student(Person):
  def __init__(self, name):
  # add properties etc

# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function
class Student(Person):
  def __init__(self, name):
    Person.__init__(self, name)

# Python also has a super() function that will make the child class inherit all the methods and properties from its parent
class Student(Person):
  def __init__(self, name, age):
    super().__init__(name)
    self.age = age
  def welcome(self):
    print("Hi", self.name, ", you are", self.age, "years old.")

x = Student("Mike", 20)
x.welcome()
# Hi Mike, you are 20 years old.

#######################################################################################
#variable
#scopes - if no 'global' or 'nonlocal' statement is in effect – assignments to names always go into the innermost scope

def scope_test():
  def do_local():
    spam = "local spam"
  def do_nonlocal():
    nonlocal spam
    spam = "nonlocal spam"
  def do_global():
    global spam
    spam = "global spam"

  spam = "test spam"
  do_local()
  print("After local assignment:", spam)
  do_nonlocal()
  print("After nonlocal assignment:", spam)
  do_global()
  print("After global assignment:", spam)
scope_test()
print("In global scope:", spam)

# After local assignment: test spam
# After nonlocal assignment: nonlocal spam
# After global assignment: nonlocal spam
# In global scope: global spam

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
