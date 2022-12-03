import random
from hangman_words import word_list
from hangman_art import stages, logo
import os
clear = lambda: os.system('cls')

print(logo)

chosen_word = random.choice(word_list)
#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

word_length = len(chosen_word)
end_of_game = False
lives = 6
display = ["_"] * word_length

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()

    if guess in display:
        print(f"You've already guessed {guess}. Guess another letter")

    #Check guessed letter
    for position, letter in enumerate(chosen_word):
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
