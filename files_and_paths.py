# linux file paths are case sensitive
# windows file paths are not case sensitive
# os.path.join() will join paths together
# os.sep will return the correct path separator for the current OS
# os.getcwd() will return the current working directory
# linux and mac use / for path separator
# linux and mac use /Users/username for home folder
# linux and mac use . for current folder
# linux and mac use .. for parent folder
# linux and mac use / for root folder
# linux and mac use ~ for home folder

import os

print(os.path.join('usr', 'bin', 'spam'))  # usr/bin/spam
print(os.sep)  # /
print(os.getcwd())  # /Users/username
print(os.path.abspath('.'))  # /Users/username
print(os.path.abspath('./Scripts'))  # /Users/username/Scripts
print(os.path.isabs('.'))  # False
print(os.path.isabs(os.path.abspath('.')))  # True
print(os.path.relpath('/Users', '/'))  # Users
print(os.path.relpath('/Users', '/spam/eggs'))  # ../../Users
print(os.getcwd())  # /Users/username

path = '/Users/username/Documents/Python/automate-the-boring-stuff/Chapter 8'
print(os.path.basename(path))  # Chapter 8
# /Users/username/Documents/Python/automate-the-boring-stuff
print(os.path.dirname(path))
# ('/Users/username/Documents/Python/automate-the-boring-stuff', 'Chapter 8')
print(os.path.split(path))
# ['', 'Users', 'username', 'Documents', 'Python', 'automate-the-boring-stuff', 'Chapter 8']
print(path.split(os.path.sep))

print(os.path.exists(path))  # True
print(os.path.isfile(path))  # False
print(os.path.isdir(path))  # True


# File Reading/Writing
# Compare this snippet from file_reading_writing.py:
# helloFile = open('/Users/username/hello.txt')
# helloContent = helloFile.read()
# print(helloContent)
# sonnetFile = open('/Users/username/sonnet29.txt')
# print(sonnetFile.readlines())
