#os - The os module provides dozens of functions for interacting with the operating system

import os
os.getcwd() # Return the current working directory
# 'C:\\Python313'
os.chdir('/server/accesslogs') # Change current working directory
os.system('mkdir today') # Run the command mkdir in the system shell
# 0
dir(os) # returns a list of all module functions
help(os) # returns an extensive manual page created from the module's docstrings

#######################################################################################
#glob - The glob module provides a function for making file lists from directory wildcard searches

import glob
glob.glob('*.py')
# ['primes.py', 'random.py', 'quote.py']

#######################################################################################
#sys -  Common utility scripts often need to process command line arguments
# These arguments are stored in the sys module’s argv attribute as a list

#######################################################################################
#re - The re module provides regular expression tools for advanced string processing

import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
# ['foot', 'fell', 'fastest']
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
# 'cat in the hat'

#######################################################################################
#math - The math module gives access to the underlying C library functions for floating-point math

import math
math.cos(math.pi / 4)
# 0.70710678118654757
math.log(1024, 2)
# 10.0

#######################################################################################
#random - The random module provides tools for making random selections

import random
random.choice(['apple', 'pear', 'banana'])
# 'apple'
random.sample(range(100), 10) # sampling without replacement
# [30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
random.random() # random float from the interval [0.0, 1.0)
# 0.17970987693706186
random.randrange(6)    # random integer chosen from range(6)
# 4

#######################################################################################
#statistics - The statistics module calculates basic statistical properties (the mean, median, variance, etc.) of numeric data

import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(data)
# 1.6071428571428572
statistics.median(data)
# 1.25
statistics.variance(data)
# 1.3720238095238095

#######################################################################################
#urllib.request
#urlopen
# There are a number of modules for accessing the internet and processing internet protocols.
# Two of the simplest are urllib.request for retrieving data from URLs and smtplib for sending mail

from urllib.request import urlopen
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()             # Convert bytes to a str
        if line.startswith('datetime'):
            print(line.rstrip())         # Remove trailing newline
# datetime: 2022-01-01T01:36:47.689215+00:00

import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
From: soothsayer@example.org

Beware the Ides of March.
""")
server.quit()
#######################################################################################
#datetime - The datetime module supplies classes for manipulating dates and times in both simple and complex ways

#######################################################################################
#zlib #gzip #bz2 #lzma #zipfile #tarfile.
# Common data archiving and compression formats

#######################################################################################
#timeit - Performance measurement tool

#######################################################################################
#doctest -  The doctest module provides a tool for scanning a module and validating tests embedded in a program’s docstrings.

#######################################################################################
#unittest - Allows a more comprehensive set of tests to be maintained in a separate file


