# matching at the start or ends of a string
#
import re

# ^ matches the start of the string
beginsWithHelloRegex = re.compile(r'^Hello')
mo = beginsWithHelloRegex.search('Hello world!')
print(mo.group())

mo = beginsWithHelloRegex.search('He said hello.')  # returns None
print(mo == None)

endsWithWorldRegex = re.compile(r'world!$')  # $ matches the end of the string
mo = endsWithWorldRegex.search('Hello world!')
print(mo.group())

# ^ matches the start of the string, $ matches the end of the string
allDigitsRegex = re.compile(r'^\d+$')
mo = allDigitsRegex.search('1234567890')
print(mo.group())

mo = allDigitsRegex.search('12345xyz67890')  # returns None
print(mo == None)

# . matches any character except newline
atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)

# .* matches anything *any number of times*
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

# .* is greedy, it will match the longest string possible
# .*? is non-greedy, it will match the shortest string possible

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('First Name: <Al> Last Name: <Sweigart>')
print(mo.group())

serve = '<To serve humans> for dinner.>'
nongreedyRegex = re.compile(r'<(.*?)>')
mo = nongreedyRegex.search(serve)
print(mo.group())

greedyRegex = re.compile(r'<(.*)>')
mo = greedyRegex.search(serve)
print(mo.group())

# . matches any character except newline

prime = 'Serve the public trust.\nProtect the innocent.\nUpload the law.'
print(prime)
dotStar = re.compile(r'.*')
mo = dotStar.search(prime)
print(mo.group())

# re.DOTALL as the second argument to re.compile()
# re.DOTALL is a shortcut to pass re.DOTALL as the second argument
# to re.compile().

dotStar = re.compile(r'.*', re.DOTALL)
mo = dotStar.search(prime)
print(mo.group())

# re.I is a shortcut for re.IGNORECASE
vowelRegex = re.compile(r'[aeiou]', re.I)
mo = vowelRegex.findall(
    'Al, why does your programming book talk about RoboCop so much?')
print(mo)
