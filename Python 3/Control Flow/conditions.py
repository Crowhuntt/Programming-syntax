#if

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('One')
else:
    print('More than one')
    
#######################################################################################
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
    
#######################################################################################
# break - The break statement breaks out of the innermost enclosing for or while loop
# continue - The continue statement continues with the next iteration of the loop

for num in range(2, 6):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")
    break
# Found an even number 2
# Found an odd number 3

#######################################################################################


