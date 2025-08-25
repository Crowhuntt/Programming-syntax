#for - for statement iterates over the items of any sequence

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
for user, status in users:
    if status == 'inactive':
        del users[user]

#######################################################################################
