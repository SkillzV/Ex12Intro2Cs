#############################################################
# FILE : game.py
# WRITER 1: Nitzan Ventura , nitzanv2 , 207378688
# WRITER 2: Shani Amoils , shani.amoils , 212076616
# EXERCISE : intro2cs1 ex2 2021
# STUDENTS I DISCUSSED WITH:
# DESCRIPTION: a file containing four requested functions
#############################################################
import boggle_board_randomizer as bbr
from typing import List, Tuple, Dict, Any, Set

START = (0, 0)
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
TOP_LEFT = (-1, -1)
BOT_LEFT = (1, -1)
TOP_RIGHT = (-1, 1)
BOT_RIGHT = (1, 1)
DIRECTIONS = [RIGHT, UP, DOWN, LEFT,
              TOP_RIGHT, TOP_LEFT, BOT_LEFT, BOT_RIGHT]
PATH = 'P'
WORD = 'W'
EMPTY = ""
MAX = 'M'


def path_in_border(path):
    for spot in path:
        y_coord = spot[0]
        x_coord = spot[1]
        if not 0 <= x_coord <= bbr.BOARD_SIZE - 1:
            return False
        if not 0 <= y_coord <= bbr.BOARD_SIZE - 1:
            return False
    return True


def is_real_path(path: List[Tuple[int, int]]):
    """
    a function that checks if every coordinate in a path is adjacent to
    the previous coordinate
    :param path: a list of coordinates indicating a path
    :return: True if every coordinate is adjacent and false otherwise.
    """

    if len(path) >= 2:
        for i in range(len(path) - 1):
            first = path[i]
            second = path[i + 1]
            distance = second[0] - first[0], second[1] - first[1]
            if distance not in DIRECTIONS:
                return False
    return True


def is_valid_path(board: List[List[str]], path: List[Tuple[int, int]],
                  words: Any):
    word = EMPTY
    if path_in_border(path) and is_real_path(path):
        for coordinate in path:
            y = coordinate[0]
            x = coordinate[1]
            word += board[y][x]
    if word in words and word != EMPTY:
        return word
    return None


def legal_phrase(phrase: str, words: Set[str]) -> bool:
    """
    a function that checks if a given phrase is
    found in a word from a word collection
    :param phrase: a phrase indicating the path
    :param words: a collection of words
    :return: True if found, False otherwise
    """
    length = len(phrase)
    if phrase in words:
        return True
    for word in words:
        if len(word) >= length and word[:length] == phrase:
            return True
    return False


def filter_words_by_length(words, n, count_longer: bool):
    if n == 0 or n == 1:
        return {}

    return {w for w in words if (len(w) == n and not count_longer) \
            or (len(w) >= n and count_longer)}


def find_length_n_paths(n, board, words):
    filtered_words = filter_words_by_length(words, n, True)
    words_found, result_paths = find_words(n,
                                           board,
                                           filtered_words,
                                           PATH)
    return result_paths


def find_words(n: int,
               board: List[List[str]],
               words: Set[str], end: str):
    words_found: List[str] = []
    result_paths: List[List[Tuple[int, int]]] = []
    row_length = len(board)
    col_length = len(board[0])

    for y in range(row_length):
        for x in range(col_length):
            build_words((y, x),
                        n,
                        board,
                        words,
                        [(y, x)],
                        board[y][x],
                        words_found,
                        result_paths, end)
    return words_found, result_paths


def gone_past_length(word, path, n, end):
    if end == PATH:
        if len(path) > n:
            return True
    if end == WORD:
        if len(word) > n:
            return True
    return False


def reached_length(word, path, n, end):
    if end == PATH:
        if len(path) == n:
            return True
    if end == WORD:
        if len(word) == n:
            return True
    return False


def build_words(start_location: Tuple[int, int],
                n: int,
                board: List[List[str]],
                words: Set[str],
                cur_path: List[Tuple[int, int]],
                word: str,
                words_found: List[str],
                result_paths: List[List[Tuple[int, int]]],
                end: str):
    if gone_past_length(word, cur_path, n, end):
        return
    if not path_in_border(cur_path):
        return
    if reached_length(word, cur_path, n, end):
        if word in words:
            if word in words_found:
                result_paths.append(cur_path[:])
            else:
                words_found.append(word)
                result_paths.append(cur_path[:])

    for direction in DIRECTIONS:
        new_location = (start_location[0] + direction[0],
                        start_location[1] + direction[1])
        if path_in_border([new_location]) and new_location not in cur_path:
            new_y, new_x = new_location[0], new_location[1]
            cur_path.append((new_y, new_x))
            word += board[new_y][new_x]
            build_words(new_location, n, board, words,
                        cur_path, word, words_found, result_paths, end)
            cur_path.pop()
            last_word_len = len(board[new_location[0]][new_location[1]])
            word = word[:(len(word) - last_word_len)]


def find_length_n_words(n, board, words):
    filtered_words = filter_words_by_length(words, n, False)
    words_found, result_paths = find_words(n,
                                           board,
                                           filtered_words,
                                           WORD)
    return result_paths


def build_word(start_location, board, cur_path, word,
               built_word: str,
               words_paths_dict: Dict[str, List[Tuple[int, int]]]):
    # finished = False
    # while not finished:
    for direction in DIRECTIONS:
        if len(built_word) >= len(word):
            break
        new_location = (start_location[0] + direction[0],
                        start_location[1] + direction[1])
        if path_in_border([new_location]) and \
                new_location not in cur_path:
            new_y, new_x = new_location[0], new_location[1]
            built_word += board[new_y][new_x]
            cur_path.append(new_location)
            length = len(built_word)
            # if built word matches start of word:
            if built_word == word[:length]:
                # if finished:
                if built_word == word:
                    if word in words_paths_dict:
                        if len(cur_path) > len(words_paths_dict[word]):
                            words_paths_dict[word] = cur_path[:]
                    else:
                        words_paths_dict[word] = cur_path[:]
                    # finished = True
                # if not finished:
                else:
                    build_word(new_location,
                               board, cur_path[:], word,
                               built_word, words_paths_dict)
                    cur_path.pop()
                    last_word_len = len(
                        board[new_y][new_x])
                    built_word = built_word[:(len(built_word) - last_word_len)]
            else:
                cur_path.pop()
                last_word_len = len(
                    board[new_y][new_x])
                built_word = built_word[:(len(built_word) - last_word_len)]
        # finished = True


def find_ideal_path(word: str,
                    words_paths_dict: Dict[str, List[Tuple[int, int]]],
                    board: List[List[str]]):
    cur_path = []
    built_word = ""
    for row in range(len(board)):
        for col in range(len(board[0])):
            length = len(board[row][col])
            location = (row, col)
            if board[row][col] == word[:length]:
                built_word += board[row][col]
                cur_path.append(location)
                if built_word != word:
                    build_word(location, board, cur_path, word, built_word
                               , words_paths_dict)
                cur_path.pop()
                last_word_len = len(
                    board[row][col])
                built_word = built_word[:(len(built_word) - last_word_len)]


def max_score_paths(board, words):
    words_paths_dict = {}
    for word in words:
        find_ideal_path(word, words_paths_dict, board)
    word_paths = []
    for value in words_paths_dict.values():
        word_paths.append(value)
    return word_paths

