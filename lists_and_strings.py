import copy
list('Hello')
print(list('Hello'))

name = 'Zophie'
print(name[0])
print(name[-2])
print(name[0:4])
print('Zo' in name)
print('z' in name)
print('p' not in name)
for i in name:
    print('* * * ' + i + ' * * *')

name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
print(name)
print(newName)


def eggs(someParameter):
    someParameter.append('Hello')


spam = [1, 2, 3]
eggs(spam)
print(spam)


spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
cheese[1] = 42
print(spam)
print(cheese)
