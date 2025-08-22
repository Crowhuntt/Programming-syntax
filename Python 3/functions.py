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
