# This is a rock paper scissors game.
# I will try to do this without looking at the answers.
# The output should look like this:
# ROCK, PAPER, SCISSORS
# 0 Wins, 0 Losses, 0 Ties
# Enter your move: (r)ock (p)aper (s)cissors or (q)uit
# p
# PAPER versus...
# PAPER
# It is a tie!
# 0 Wins, 1 Losses, 1 Ties
# Enter your move: (r)ock (p)aper (s)cissors or (q)uit
# s
# SCISSORS versus...
# PAPER
# You win!
# 1 Wins, 1 Losses, 1 Ties
# Enter your move: (r)ock (p)aper (s)cissors or (q)uit
# q

import random, sys

print("WELCOME TO ROCK, PAPER, SCISSORS")

wins = 0
losses = 0
ties = 0

while True:  # main game loop
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))
    while True:  # The player input loop.
        print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
        playerMove = input()
        if playerMove == "q":
            sys.exit()  # quit program
        if playerMove == "r" or playerMove == "p" or playerMove == "s":
            break  # break player out of player input loop
        print("Type one of r, p, s, or q.")

    # Display:
    if playerMove == "r":
        print("ROCK versus...")
    elif playerMove == "p":
        print("PAPER versus...")
    elif playerMove == "s":
        print("SCISSORS versus...")

    # Display what the computer chose:
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = "r"
        print("ROCK")
    elif randomNumber == 2:
        computerMove = "p"
        print("PAPER")
    elif randomNumber == 3:
        computerMove = "s"
        print("SCISSORS")

    # Display and record the win/loss/tie:
    if playerMove == computerrMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1
