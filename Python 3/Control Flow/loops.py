#for - for statement iterates over the items of any sequence

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
for user, status in users:
    if status == 'inactive':
        del users[user]

#######################################################################################
#range - If you do need to iterate over a sequence of numbers

for i in range(5):
    print(i)
    
list(range(5, 10))
# [5, 6, 7, 8, 9]

list(range(0, 10, 3))
# [0, 3, 6, 9]

list = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(list)):
    print(i, list[i])
# 0 Mary
# 1 had
# 2 a
# 3 little
# 4 lamb

#######################################################################################
#looping a dictionary
#items() - When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
# gallahad the pure
# robin the brave

#######################################################################################
#zip - To loop over two or more sequences at the same time, the entries can be paired with the zip() function

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
# What is your name?  It is lancelot.
# What is your quest?  It is the holy grail.
# What is your favorite color?  It is blue.

#######################################################################################
#reversed - To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function

for i in reversed(range(1, 6, 2)):
    print(i)
# 5
# 3
# 1

#######################################################################################
#sorted - To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)
# apple
# apple
# banana
# orange
# orange
# pear

#######################################################################################
#set() - Using set() on a sequence eliminates duplicate elements
# The use of sorted() in combination with set() over a sequence is an idiomatic way to loop over unique elements of the sequence in sorted order

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
# apple
# banana
# orange
# pear

#######################################################################################
#while - The while statement is used for repeated execution as long as an expression is true

while_stmt ::= "while" assignment_expression ":" suite
               ["else" ":" suite]
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
# 1
# 2
# 3
