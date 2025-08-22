#functions
#print and #printf

# Required argument (age)
# Optional argument (city). If not passed, default one will be set
# (glasses) Type hints: glasses argument is expected to be bool (just a hint, not requiered. wont return error if not bool)
# -> return type. Function returns a string
def student(age, city='Euskadi', glasses:bool=False) -> str:
    print(f"The student has {age} ages and lives in {city}. Wears glasses: {glasses}.")

# Call the function by keywords
student(17)
# The student has 17 ages and lives in Euskadi. Wears glasses: False.

# Call the function by position
student(17, 'Madrid', True)
# The student has 17 ages and lives in Madrid. Wears glasses: True.

# Call the function by position and keyword
student(17, glasses=True)
# The student has 17 ages and lives in Euskadi. Wears glasses: True.

# Positional-only and keyword-only parameters
# Positional-only parameters are placed before a / (forward-slash)
# To mark parameters as keyword-only, indicating the parameters must be passed by keyword argument, place an * in the arguments list just before the first keyword-only parameter.
# If / and * are not present in the function definition, arguments may be passed to a function by position or by keyword.
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

#*arg y *args
def fruits(best, *arguments, **keywords):
    print(f"Best fruit: {best}.")
    print("Rest of fruits: ")
    for arg in arguments:
        print(arg)
    print("Even more fruits: ")
    for kw in keywords:
        print(f"{kw}: {keywords[kw]}")
        
fruits("Strawberry", "Banana", "Apple", worst="Kiwi", worse="Orange")

# Best fruit: Strawberry.
# Rest of fruits: 
# Banana
# Apple
# Even more fruits: 
# worst: Kiwi
# worse: Orange

#######################################################################################
#Lambda Expressions - Small anonymous functions can be created with the lambda keyword

# This function returns the sum of its two arguments: lambda a, b: a+b
def make_incrementor(n):
    return lambda x: x + n
    
f = make_incrementor(42)
f(0)
# 42
f(1)
# 43

# Sort by second key
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs
# [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

#######################################################################################
#Documentation - Document a function

def my_function():
    """Do nothing, but document it.
    No, really, it doesn't do anything.
    """
    pass
    
print(my_function.__doc__)
# Do nothing, but document it.
# No, really, it doesn't do anything.
