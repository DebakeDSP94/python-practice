# This is a guess the number game.
import random
print('Hello. What is your name?')
name = input()
secretNumber = random.randint(1, 20)
print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break  # This condition is the correct guess!
if guess == secretNumber:
    print('Good job, ' + name + '! You guessed my number in ' +
          str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))

# The break statement causes the execution to jump out of the loop without
# running the rest of the code in the loop. The continue statement causes the
# execution to jump back to the start of the loop, skipping the rest of the
# code inside the loop for the current iteration.
# The continue statement causes the program execution to immediately jump back
# to the start of the loop and reevaluate the loop’s condition. (This is also
# what happens when the execution reaches the end of the loop.) In essence, the
# continue statement says, “Go back to the start of the loop.”
# The break statement causes the program execution to immediately leave the
# loop, without reevaluating the loop’s condition. The program continues
# execution at the line after the loop’s end.
# The continue statement is useful when you want to skip over a loop iteration
# prematurely to go back to the start of the loop. The break statement is
# useful when you want to exit out of a loop prematurely if, for example, you
# have already found what you are looking for in a list.
# The continue statement and break statement are similar in a way, because
# they both disrupt the normal flow of execution by jumping to another part of
# your code. The difference between continue and break is that continue jumps
