#!/usr/bin/python3

spam = 'Hello world!'
print(spam.upper())
print(spam.lower())
print(spam)
print(spam.islower())
print(spam.isupper())
print(spam.upper().isupper())
print(spam.lower().islower())
print(spam.isalpha())
print(spam.isalnum())
print(spam.isdecimal())
print(spam.isspace())
print(spam.istitle())
print(spam.startswith('Hello'))
print(spam.endswith('world!'))
print(spam.startswith('Hello world!'))
print(spam.endswith('Hello world!'))
print(spam.split())
print(spam.split('o'))
print(spam.split('l'))
print(spam.split('ll'))

print('Hello'.rjust(10))
print('Hello'.rjust(20))
print('Hello World'.rjust(20))
print('Hello'.ljust(10))
print('Hello'.rjust(20, '*'))
print('Hello'.ljust(20, '-'))
print('Hello'.center(20))
print('Hello'.center(20, '='))

','.join(['cats', 'rats', 'bats'])
print(','.join(['cats', 'rats', 'bats']))
' '.join(['My', 'name', 'is', 'Simon'])
print(' '.join(['My', 'name', 'is', 'Simon']))
'ABC'.join(['My', 'name', 'is', 'Simon'])
print('ABC'.join(['My', 'name', 'is', 'Simon']))

spam = 'Hello'.rjust(10)
spam = spam.strip()
print(spam)
spam = 'Hello'.rjust(10)
spam = spam.lstrip()
print(spam)
spam = 'Hello'.rjust(10)
spam = spam.rstrip()
print(spam)

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))
print(spam.strip('Spam'))

print(spam.replace('Spam', 'Eggs'))
print(spam.replace('Spam', ''))
print(spam.replace('p', 'XYZ'))
print(spam.replace('Spam', 'Eggs', 1))

name = 'Alice'
place = 'Main Street'
time = '6 pm'
food = 'turnips'
print('Hello ' + name + ', you are invited to a party at ' +
      place + ' at ' + time + '. Please bring ' + food + '.')
print('Hello %s, you are invited to a party at %s at %s. Please bring %s.' %
      (name, place, time, food))
print('Hello %s, you are invited to a party at %s at %s. Please bring a %s.' %
      (name, place, time, food))
