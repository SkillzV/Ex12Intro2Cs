import boggle_board_randomizer as bbr
from cube import Cube
from typing import List, Tuple, Dict, Any


def path_in_border(path):
    for spot in path:
        y_coord = spot[0]
        x_coord = spot[1]
        if not 0 <= x_coord <= bbr.BOARD_SIZE -1:
            return False
        if not 0 <= y_coord <= bbr.BOARD_SIZE -1:
            return False
    return True


def is_valid_path(board: List[List[str]], path: List[Tuple[int, int]], words: Any):
    word = ""
    if path_in_border(path):
        for coordinate in path:
            y = coordinate[0]
            x = coordinate[1]
            word += board[y][x]
    if word in words and word != "":
        return word
    return None



def find_length_n_paths(n, board, words):
    pass

def find_length_n_words(n, board, words):
    pass

def max_score_paths(board, words):
    pass

