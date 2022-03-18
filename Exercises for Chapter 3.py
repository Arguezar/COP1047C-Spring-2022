"""
Created on Tue Mar 15 19:31:55 2022

@author: arguez, arlene
"""
'''
1) Write a program that simulates a fortune cookie. The program should display one of five
unique fortunes, at random, each time it’s run.
'''
import random
user_question = input('Would like to know your fortune? \n Enter y for yes, n for no: ')

fortune_list = ['Confucius says ''No fortune telling for you today!',
                'You will always have change for the bus!',
                'You will take a course at MDC!',
                'If you buy cows you will be a farmer!',
                'Do waste your money on lottery tickets!']                
fortune = random.choice(fortune_list)

if user_question == 'y':
    print (fortune)
else:
    print ("May you have Good luck in the future, thanks for playing!")


'''
2) Write a program that flips a coin 100 times and then tells you the number of heads and
tails.
'''
import random

heads = 0
tails = 0
flips = 0

while flips < 100:
    flips = flips + 1
    rand = random.randint(0,2)
    if rand == 1:
        heads = heads + 1
    else:
        tails = tails + 1

print ('A coin was flipped 100 times, landing on heads', heads, 'times and', tails, 'times on tails.')



'''''
4) Write the pseudocode for a program where the player and the computer trade places in
the number guessing game. That is, the player picks a random number between 1 and 100
that the computer has to guess. Before you start, think about how you guess. If all goes
well, try coding the game.
'''
    #PSEUDOCODE: Player guessing computers number. 
''' 
    1. User (player) will see: "Welcome to 'Guess My Number!"
    2. Then user will see: "I'm thinking of a number between 1 and 100."
    3. Next a question is posed to user:  "Try to guess it in as few attempts as possible."
    4. The initial values are set as random numbers between 1 and 100.
    5. The user then enters a number with the prompt: "Take a guess: ".
    6. The count of attempts (tries) at guessing a number starts at 1.
    7. If the first number guessed by the user is not equal to the number selected 
        a prompt appears for them to enter either a lower number or a higher number 
    8. The tries count increases by one, until the correct or matching number is entered.
    9. Once the user has entered the matching number the two lines will appear
        (including the matching number and number of attempts it took  for the user to guess):
        "You guessed it!  The number was (matching number here)."
        "And it only took you, (number of tries) tries!"
    10. User is then prompted to end the game by pressing the enter key to exit.
'''