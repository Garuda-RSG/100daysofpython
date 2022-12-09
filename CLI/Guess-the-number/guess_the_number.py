#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_guess(number, guess, turns):
    """Checks the guess against the answer and returns the number of remaining turns"""
    if guess < number:
        print("Too Low")
        return turns - 1
    elif guess > number:
        print("Too High")
        return turns - 1
    else:
        print(f"You got it! The answer was {number}")

def set_difficulty():
    difficulty = input("Chose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    
    number = random.randint(2, 99)
    print(f"Pssst, the correct answer is {number}")
    
    turns = set_difficulty()
   
    
    guess = 0
    while guess != number:
        print(f"You have {turns} remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns = check_guess(number, guess, turns)
        if turns == 0:
            print("You have run out of guesses, You Lose")
            return
        elif guess != number:
            print("Guess again")

        
game()


