# Justin Young
# CIS256 Fall 2026
# Programming Assignment 4

import random

wordlist = [
       "giraffe", "elephant", "dumpster", "building", "racetrack", "table", "pig", "dig", "throw", "flag", "python", "snake", "apple", "fruit", "flight"
        ]

word = random.choice(wordlist)
guessed_word = ['_' for i in range (0, len(word))]
word.split()
guessed_letters = []

game_over = False

print(f"word: {word}")

def guess_letter(guessed_letter):
    letter_was_present = False
    guessed_letter = guessed_letter.lower()
    i = 0
    for letter in word:
        print(f"  letter: {letter}")
        print(f"  guessed_letter: {guessed_letter}")
        if letter == guessed_letter:
            guessed_word[i] = guessed_letter
            letter_was_present = True
        i += 1
    return letter_was_present

while game_over is False:
    user_input = input("Guess a letter: ")
    result = guess_letter(user_input)
    if result == True:
        print(f"PRESENT {guessed_word}")
    else:
        print("NOT PRESENT")
