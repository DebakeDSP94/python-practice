# raise and assert statements

# raise statement
# The raise statement is useful when you need to raise an exception in a code
# block. The raise statement consists of the following:
# The raise keyword
# A call to the Exception() function
# A string with a helpful error message passed to the Exception() function
# Here is an example of how to use the raise statement to raise an exception
# with a custom error message:
# raise Exception('This is the error message.')


import traceback


def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of length 1.')
    if (width < 2) or (height < 2):
        raise Exception(
            '"width" and "height" must be greater than or equal to 2.')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


boxPrint('*', 15, 5)
boxPrint('O', 5, 15)
# boxPrint('**', 15, 5)

try:
    raise Exception('This is the error message.')
except:
    errorFile = open('errorInfo.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')

# The traceback.format_exc() function returns a string value of the traceback
# obtained from calling traceback.format_exc(). You can then write this
# string to a file to review later. (You can also just call traceback.print_exc()
# to print it on the screen immediately.)


# assert statement
# An assert statement consists of the following:
# The assert keyword
# A condition (that is, an expression that evaluates to True or False)
# A comma
# A string to display when the condition is False
# Here is an example of how to use an assert statement:
# assert condition, 'Error message'

# The assert statement is a sanity check to make sure your code isn’t doing
# something obviously wrong. These sanity checks are performed by assert
# statements. If the sanity check fails, then an AssertionError exception is
# raised. In code, an assert statement consists of the following:

# assert False, 'This is the error message.'

market_2nd = {'ns': 'green', 'ew': 'red'}


def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'Neither light is red!' + str(
        intersection)


switchLights(market_2nd)

print(market_2nd)
switchLights(market_2nd)
print(market_2nd)
switchLights(market_2nd)
print(market_2nd)
switchLights(market_2nd)
