# Justin Young
# CIS256 Fall 2026
# Programming Assignment 4

import random


class Game:
    WORDLIST = [
        "apple", "banana", "cherry", "dragonfruit", "elderberry", "fig",
        "grape", "honeydew"
    ]

    def __init__(self):
        self.word = random.choice(self.WORDLIST)
        self.guessed_word = ['_' for i in range(len(self.word))]
        self.word.split()
        self.total_incorrect_guesses = 0
        self.max_incorrect_guesses = len(self.word)
        self.guessed_letters = set()

    def guess_letter(self, guessed_letter):
        guessed_letter = guessed_letter.lower()
        letter_was_present = False
        i = 0
        for letter in self.word:
            if letter == guessed_letter:
                self.guessed_word[i] = guessed_letter
                letter_was_present = True
            i += 1
        if letter_was_present == False:
            if guessed_letter not in self.guessed_letters:
                self.guessed_letters.add(guessed_letter)
                self.total_incorrect_guesses += 1
        return letter_was_present

    def attempts_remaining(self):
        return self.max_incorrect_guesses - self.total_incorrect_guesses

    def is_game_over(self):
        if self.attempts_remaining() <= 0:
            return True

        if "".join(self.guessed_word) == self.word:
            return True

        return False


def main():
    game = Game()
    while game.is_game_over() is False:
        user_input = input("Guess a letter: ")
        result = game.guess_letter(user_input)
        if result == True:
            print("Good guess!")
        else:
            print(f"Try again. {game.attempts_remaining()} incorrect guesses left")
        print("".join(game.guessed_word) + "\n")
        if game.is_game_over():
            print(f"The word was: {game.word}")


if __name__ == "__main__":
    main()
