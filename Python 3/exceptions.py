#error
#exception
# Errors detected during execution are called exceptions and are not unconditionally fatal

10 * (1/0)
# ZeroDivisionError: division by zero

4 + spam*3
# NameError: name 'spam' is not defined

'2' + 2
# TypeError: can only concatenate str (not "int") to str

#######################################################################################
#except - It is possible to write programs that handle selected exceptions
# If no exception occurs, the except clause is skipped and execution of the try statement is finished
# If an exception occurs during execution of the try clause, the rest of the clause is skipped. Then, if its type matches the exception named after the except keyword, the except clause is executed, and then execution continues after the try/except block
# If an exception occurs which does not match the exception named in the except clause, it is passed on to outer try statements; if no handler is found, it is an unhandled exception and execution stops with an error message

while True:
    try: # Tries to run the code below
        x = int(input("Please enter a number: "))
        break
    except ValueError: # Enter when exception occurs
        print("Oops!  That was no valid number.  Try again...")

# A try statement may have more than one except clause
except (RuntimeError, TypeError, NameError):
  print("Oops! Error!")

# The except clause may specify a variable after the exception name
# The variable is bound to the exception instance which typically has an args attribute that stores the arguments
try:
    raise Exception('spam', 'eggs')
except Exception as inst: # The variable 'inst' is bound to the exception instance
    print(type(inst))    # Exception type
    print(inst.args)     # Arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly
    x, y = inst.args     # Unpack args
    print('x =', x)
    print('y =', y)
# <class 'Exception'>
# ('spam', 'eggs')
# ('spam', 'eggs')
# x = spam
# y = eggs

# The most common pattern for handling Exception is to print or log the exception and then re-raise it (allowing a caller to handle the exception as well):
import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise

# The try … except statement has an optional 'else' clause, which, when present, must follow all except clauses
# It is useful for code that must be executed if the try clause does not raise an exception
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

#######################################################################################
#raise - The raise statement allows the programmer to force a specified exception to occur

raise NameError('HiThere')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     raise NameError('HiThere')
# NameError: HiThere

#The sole argument to raise indicates the exception to be raised
raise ValueError  # shorthand for 'raise ValueError()'

# If you need to determine whether an exception was raised but don’t intend to handle it, a simpler form of the raise statement allows you to re-raise the exception
try:
    raise NameError('HiThere') # raise exception
except NameError:   # exception martches so we enter
    print('An exception flew by!') # handle exception, in this case just print a message
    raise # re-raise exception. Now an error will stop the execution
# An exception flew by!
# Traceback (most recent call last):
#  File "<stdin>", line 2, in <module>
#     raise NameError('HiThere')
# NameError: HiThere


#8.6. User-defined Exceptions?
https://docs.python.org/3/tutorial/errors.html


