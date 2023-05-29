# regex character classes

import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
result = phoneRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(result)

phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
result = phoneRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(result)


digitRegex = re.compile(r'0|1|2|3|4|5|6|7|8|9')

lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree'

# one or more digits, one space, one or more word characters
xmasRegex = re.compile(r'\d+\s\w+')
result = xmasRegex.findall(lyrics)
print(result)

vowelRegex = re.compile(r'[aeiouAEIOU]')  # vowel regex
result = vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
print(result)

letterRegex = re.compile(r'[a-zA-Z]')  # letter regex
result = letterRegex.findall('Robocop eats baby food. BABY FOOD.')
print(result)

doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')  # double vowel regex
result = doubleVowelRegex.findall('Robocop eats baby food. BABY FOOD.')
print(result)

consonantRegex = re.compile(r'[^aeiouAEIOU]')  # consonant regex
result = consonantRegex.findall('Robocop eats baby food. BABY FOOD.')
print(result)
