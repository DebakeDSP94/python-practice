# plaintext files

# open a file for writing
# open() returns a file object
# 'w' for write mode
# 'a' for append mode
# 'r' for read mode
# 'wb' for write binary mode
# 'rb' for read binary mode

# write mode will overwrite the file
# append mode will append to the end of the file

# write mode will create a new file if it doesn't exist
# append mode will create a new file if it doesn't exist

# linux open user documents/helloworld.txt

import shelve
from pathlib import Path
dataFolder = Path('/home/stuart/Documents')
helloFile = open(dataFolder / 'helloworld.txt', 'w')
helloFile.write('Hello world! Suck it!\n')
helloFile.close()

# read mode will read the file
# readlines() will return a list of strings
# read() will return a single string

helloFile = open(dataFolder / 'helloworld.txt', 'r')
helloContent = helloFile.read()
print(helloContent)
helloFile.close()

helloFile = open(dataFolder / 'helloworld.txt', 'a')
helloFile.write('Hello world! just kidding!\n')
helloFile.close()

helloFile = open(dataFolder / 'helloworld.txt', 'r')
helloContent = helloFile.read()
print(helloContent)
helloFile.close()

baconFile = open(dataFolder / 'bacon.txt', 'w')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

baconFile = open(dataFolder / 'bacon.txt', 'r')
content = baconFile.read()
baconFile.close()
print(content)

baconFile = open(dataFolder / 'bacon.txt', 'a')
baconFile.write('\n\nBacon is delicious.')
baconFile.close()

baconFile = open(dataFolder / 'bacon.txt', 'r')
content = baconFile.read()
baconFile.close()
print(content)

# shelve module
# shelve module lets you store Python values in a binary file
# shelve module will let you add Save and Open features to your program
# shelve module will let you have your program automatically restore data
# to variables from the hard drive

# shelve module has open(), close(), keys(), values(), items(), get(), and
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
print(type(shelfFile))
print(shelfFile['cats'])
shelfFile.close()
