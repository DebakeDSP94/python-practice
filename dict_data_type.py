myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat['size'])
print(myCat['color'])
print(myCat['disposition'])
print('My cat has ' + myCat['color'] + ' fur.')

# Dictionaries vs. Lists

spam = {12345: 'Luggage Combination', 42: 'The Answer'}
print(spam[12345])
print(spam[42])

eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
ham = {'species': 'cat', 'age': 8, 'name': 'Zophie'}
print(eggs == ham)

print(list(eggs.keys()))
print('name' in eggs.keys())
print(list(eggs.values()))
print(list(eggs.items()))

for k in eggs.keys():
    print(k)

for v in eggs.values():
    print(v)

for k, v in eggs.items():
    print(k, v)

if 'color' in eggs:
    print(eggs['color'])

print(eggs)

picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')


# setdefault() method
eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
eggs.setdefault('color', 'black')
print(eggs)
eggs.setdefault('color', 'orange')
print(eggs)
