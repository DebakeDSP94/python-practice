# Description: This script is used to demonstrate the use of the re.sub() function and the re.VERBOSE flag.

import re

# The sub() method for Regex objects is passed two arguments.
# The first argument is a string to replace any matches.
# The second is the string for the regular expression.
# The sub() method returns a string with the substitutions applied.

namesRegex = re.compile(r'Agent \w+')
result = namesRegex.sub(
    'REDACTED', 'Agent Alice gave the secret documents to Agent Bob.')
print(result)

# Sometimes you may need to use the matched text itself as part of the substitution.
# In the first argument to sub(), you can type \1, \2, \3, and so on, to mean “Enter the text of group 1, 2, 3, and so on, in the substitution.”

agentNamesRegex = re.compile(r'Agent (\w)\w*')
result = agentNamesRegex.sub(r'\1****',
                             'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(result)

# The re.VERBOSE argument allows you to add whitespace and comments to the string passed to re.compile().
# This can make it much more readable.

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # area code with or without parens
    (\s|-|\.)?  # separator
    \d{3}  # first 3 digits
    (\s|-|\.)  # separator
    \d{4}  # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE | re.IGNORECASE | re.DOTALL)
result = phoneRegex.findall(
    'Cell: 415-555-9999 Work: 212-555-0000 ext 12345')
print(result)

# The re.IGNORECASE argument is passed to re.compile() will make the matching case-insensitive.
