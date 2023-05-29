# using the debugger
# ------------------------------------
import pdb


def add_one(num):
    result = num + 1
    print(result)
    return result


pdb.set_trace()
add_one(5)
# ------------------------------------
# pdb commands
# ------------------------------------
# c - continue
# w - shows the context of the current line it is executing.
# a - print the argument list of the current function
# s - Execute the current line and stop at the first possible occasion.
# n - Continue execution until the next line in the current function is reached or it returns.
# r - Continue execution until the current function returns.
# l - List source code for the current file.
# p - Print the value of the expression.
# q - Quit the debugger/execution.
# ------------------------------------

# ------------------------------------
# set breakpoint
