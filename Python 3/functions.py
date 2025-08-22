#functions
#print and #printf

# Required argument (age)
# Optional argument (city). If not passed, default one will be set
def student(age, city='Euskadi', glasses=False):
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
