def div42(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')


print(div42(2))
print(div42(12))
print(div42(0))
print(div42(1))

print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats.')
    else:
        print('That is not that many cats.')
except ValueError:
    print('You did not enter a number.')

# The try and except statements are similar to the if and else statements.
