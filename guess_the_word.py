# Justin Young
# CIS256 Fall 2026
# Programming Assignment 4

import random

wordlist = ["apple", "banana", "cherry", "dragonfruit", "elderberry", "fig", "grape", "honeydew"]

word = random.choice(wordlist)
guessed_word = ['_' for i in range (0, len(word))]
word.split()
total_attempts = 0
game_over = False
max_attempts = len(word)

def guess_letter(guessed_letter):
    guessed_letter = guessed_letter.lower()
    letter_was_present = False
    i = 0
    for letter in word:
        if letter == guessed_letter:
            guessed_word[i] = guessed_letter
            letter_was_present = True
        i += 1
    if letter_was_present == False:
        total_attempts += 1
    return letter_was_present

def attempts_remaining():
    return max_attempts - total_attempts

def is_game_over():
    if attempts_remaining() <= 0:
        return True
    else:
        return False

while is_game_over() is False:
    user_input = input("Guess a letter: ")
    result = guess_letter(user_input)
    if result == True:
        print(f"Good guess!")
    else:
        print(f"Try again. {attempts_remaining()} guesses left")
    print("".join(guessed_word))
