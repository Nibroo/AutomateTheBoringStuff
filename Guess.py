# Just a Guess Game

import random
print('Hello. What is Your name?')

name = input()
secretNumber = random.randint(1,100)
print('Well, ' + name + ', I am thinking of a number between 1 to 100')

for guessTaken in range(1,10):
        print('Take a Guess.')
        guess = int(input())
        if guess < secretNumber:
            print('Your Guess is too low')
        elif guess > secretNumber:
            print('Your Guess is too high')
        else:
            break

if guess == secretNumber:
        print('Good job, ' + name + ', Congratulations. you only took ' + str(guessTaken) + ' times to guess it!')
else:
        print('Nope. The Number I was thinking of was ' + str(secretNumber))
        
# Did you have fun making it?
