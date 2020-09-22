"""
Module docstring
"""

import random

from classes.player import Player

class Engine:
    """
    Class docstring
    """

    def __init__(self, words):
        """
        Method docstring
        """
        self._init_attributes(words)
        self._init_methods()

    def main_loop(self):
        """
        Method docstring
        """
        while self.keep_playing:
            self._game_loop()
            self.player.add_points(self.count)
            answer = input('voulez-vous continuer ? (y/n)')
            if answer == "n":
                print("merci d'avoir joué avec nous !")
                self.keep_playing = False
            self._reinit_game()

    def ask_letter(self):
        """
        Method docstring
        """
        letter = str(input('Entrez une lettre : ')).lower()
        letter = self._normalize(letter)
        if not letter:
            letter = self.ask_letter()
        self.letters += letter
        return letter

    def check_letter_in_word(self, letter):
        """
        Method docstring
        """
        return letter in self.word

    def print_word(self):
        """
        Method docstring
        """
        word = ""
        for letter in self.word:
            word += letter if letter in self.letters else "*"
        print(word)
        return "*" not in word

    def _game_loop(self):
        while self.count > 0 and not self.print_word():
            self.ask_letter()
            self.count -= 1

    def _normalize(self, letter):
        """
        Method docstring
        """
        if not len(letter) == 1 \
            or not letter.isalpha() \
            or letter in "éèàûîôêâñëç":
            return False
        return letter

    def _get_random_word(self):
        """
        Method docstring
        """
        random.shuffle(self.words)
        self.word = self.words[0]

    def _init_attributes(self, words):
        """
        Method docstring
        """
        self.word = ""
        self.letters = ""
        self.count = 8
        self.words = words
        self.keep_playing = True

    def _init_methods(self):
        """
        Method docstring
        """
        self.player = Player()
        self._get_random_word()
        self.main_loop()

    def _reinit_game(self):
        self.count = 8
        self.letters = ""
        self._get_random_word()
