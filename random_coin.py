import random
heads = 0
for i in range(1, 1001):
    if random.randint(0, 1) == 1:
        heads += 1
    if i == 500:
        print('Halfway done!')
print('Heads came up ' + str(heads) + ' times.')

# The random.randint() function call evaluates to a random integer value between
# the two integers that you pass it. Since you are passing 0 and 1, you will get
# either 0 or 1 back. If random.randint(0, 1) returns 0, then the code adds 1 to
# the heads variable. Otherwise, it does nothing. After 1,000 iterations of this
# code, the program prints the value of the heads variable. This will be a number
# close to 500, but probably not exactly 500. (After all, it is random.)
# The random.randint() function call evaluates to a random integer value between
# the two integers that you pass it. Since you are passing 0 and 1, you will get
# either 0 or 1 back. If random.randint(0, 1) returns 0, then the code adds 1 to
# the heads variable. Otherwise, it does nothing. After 1,000 iterations of this
# code, the program prints the value of the heads variable. This will be a number
