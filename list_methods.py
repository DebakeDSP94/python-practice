spam = ['apples', 'bananas', 'tofu', 'cats']
spam.index('apples')
print(spam.index('apples'))
spam.index('cats')
print(spam.index('cats'))

spam.append('dogs')
print(spam)
spam.insert(1, 'chicken')
print(spam)
spam.remove('bananas')
print(spam)
del spam[0]
print(spam)

spam = [2, 5, 3.14, 1, -7]
print(spam)
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
print(spam)
spam.sort()
print(spam)

spam.sort(key=str.lower)
print(spam)
