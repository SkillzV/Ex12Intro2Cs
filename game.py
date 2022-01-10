import boggle_board_randomizer as bbr

from timer import Timer
from typing import List, Tuple

MAX_TIME = 180


class Game:
    def __init__(self):
        with open('boggle_dict.txt') as file:
            words = file.read().splitlines()

        self.__words = set(words)
        self.__board = bbr.randomize_board()
        self.__score = 0
        self.__path = []
        self.__built_word = ""
        self.__last_input_length = 0
        self.__found_words = []

    def end_game(self):
        print("Time's Up!")

    def shuffle_board(self):
        self.__board = bbr.randomize_board()

    def reset_score(self):
        self.__score = 0

    def add_to_score(self, value: int):
        self.__score += value

    def get_score(self):
        return self.__score

    def get_words(self):
        return self.__words

    def get_board(self):
        return self.__board

    def get_cur_path(self):
        return self.__path

    def get_built_word(self):
        return self.__built_word

    def add_value_to_path(self, value: str, location):
        self.__path.append(location)
        self.__built_word += value.upper()
        self.__last_input_length = len(value)

    def reset_path_and_word(self):
        self.__path = []
        self.__built_word = ""

    def pop_last_entry(self):
        length = len(self.__built_word)
        self.__built_word = \
            self.get_built_word()[:length - self.__last_input_length]
        self.__path.pop()

    def reset_found_words(self):
        self.__found_words = []

    def add_to_found_words(self) -> bool:
        if self.__built_word in self.__words and self.__built_word \
                not in self.__found_words:
            self.__found_words.append(self.__built_word)
            print('added word', self.__built_word)
            return True
        else:
            return False
