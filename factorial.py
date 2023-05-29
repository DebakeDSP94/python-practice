# def factorial(n):
#    if n == 0:
#       return 1
#    else:
#       return n * factorial(n-1)
import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')

# logging.disable(logging.CRITICAL)
logging.debug('Start of program')

# logging.debug() will call basicConfig() automatically if no logging
# configuration has been done for the current process.
# logging.basicConfig() does nothing if the root logger already has handlers
# configured for it.


def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))

    logging.debug('End of factorial(%s)' % (n))
    return total


print(factorial(5))
