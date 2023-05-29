# repetition regex

import re

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())

mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My number is 415-555-4242')
print(mo.group())

mo = phoneRegex.search('My number is 555-4242')
print(mo.group())

# The ? matches zero or one of the preceding group.
# The (wo)? part of the regular expression means that the pattern wo is an optional group.
# The regex will match text that has zero instances or one instance of wo in it.
# This is why the regex matches both 'Batwoman' and 'Batman'.

batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The Adventures of Batwowowowoman')
print(mo.group())

# The * (called the star or asterisk) means “match zero or more”—the group that precedes the star can occur any number of times in the text.

batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The Adventures of Batwoman')
print(mo.group())

mo = batRegex.search('The Adventures of Batwowowowoman')
print(mo.group())

# The + (or plus) means “match one or more.”
# The group preceding a plus must appear at least once.
# It is not optional.

regex = re.compile(r'\+\*\?')
mo = regex.search('I learned about +*? regex syntax')
print(mo.group())

# To match an actual plus sign, asterisk, or question mark, you need to escape them with a backslash: \+, \*, or \?.

haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('He said "HaHaHa"')
print(mo.group())

# (Ha){3} matches the string 'HaHaHa' but not the string 'Ha'.

haRegex = re.compile(r'(Ha){3,5}')
mo = haRegex.search('He said "HaHaHa"')
print(mo.group())

mo = haRegex.search('He said "HaHaHaHaHa"')
print(mo.group())

# (Ha){3,5} will match 'HaHaHa', 'HaHaHaHa', and 'HaHaHaHaHa'.
# But not 'HaHaHaHaHaHa' (6 Ha's).

# By default, Python’s regular expressions are greedy, which means that in ambiguous situations they will match the longest string possible.

digitRegex = re.compile(r'(\d){3,5}')
mo = digitRegex.search('1234567890')
print(mo.group())

# To make it non-greedy, use the ?.
# Like so:

digitRegex = re.compile(r'(\d){3,5}?')
mo = digitRegex.search('1234567890')
print(mo.group())

# The ? character after the {3,5} makes the regex non-greedy, which matches the shortest string possible, 12345.

phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
mo = phoneRegex.search('My numbers are 415-555-1234,555-4242,212-555-0000')
print(mo.group())
