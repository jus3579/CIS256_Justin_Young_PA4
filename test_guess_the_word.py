# Justin Young
# CIS256 Fall 2026
# Programming Assignment 4

from guess_the_word import Game


# The selected word should come from the predefined list in the class
def test_selected_word():
    game = Game()
    assert (game.word in Game.WORDLIST)


# A correct guess should reveal the letter
def test_guess_letter_corrrect():
    game = Game()
    selected_word = game.word
    index = 1
    assert (game.guessed_word[index] == '_')
    game.guess_letter(selected_word[1])
    assert (game.guessed_word[index] == game.word[index])


# An incorrect guess should not reveal a letter
def test_guess_letter_incorrrect():
    game = Game()
    index = 1
    assert (game.guessed_word[index] == '_')
    game.guess_letter('z')
    assert (game.guessed_word[index] == '_')


# The count of incorrect guesses should increase when a wrong guess is made
def test_increment_incorrect_attempt_count():
    game = Game()
    assert (game.total_incorrect_guesses) == 0
    game.guess_letter('z')
    assert (game.total_incorrect_guesses) == 1


# The incorrect guess count should only increase if an incorrect guess is unique
def test_dont_increment_incorrect_attempt_count_on_existing_guess():
    game = Game()
    assert (game.total_incorrect_guesses) == 0
    game.guess_letter('z')
    assert (game.total_incorrect_guesses) == 1
    game.guess_letter('z')
    assert (game.total_incorrect_guesses) == 1


def test_attempts_remaining():
    game = Game()
    assert (game.total_incorrect_guesses) == 0
    assert (game.attempts_remaining() == len(game.word))
    game.guess_letter('z')
    assert (game.total_incorrect_guesses) == 1
