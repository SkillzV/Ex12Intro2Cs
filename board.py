EMPTY = ""
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
DIAGONAL_LEFT_UP = (-1, -1)
DIAGONAL_LEFT_DOWN = (1, -1)
DIAGONAL_RIGHT_UP = (-1, 1)
DIAGONAL_RIGHT_DOWN = (1, 1)

class Board:
    def __init__(self, num_of_rows : int, num_of_columns: int):
        self.__board = []
        for i in range(num_of_rows):
            row = []
            for j in range(num_of_columns):
                row.append(EMPTY)
            self.__board.append(row)
        # self.__directions = [UP, DOWN, LEFT, RIGHT, DIAGONAL_LEFT_UP,
        #                      DIAGONAL_LEFT_DOWN, DIAGONAL_RIGHT_UP,
        #                      DIAGONAL_RIGHT_DOWN]

    def shuffle_cubes(self):
        pass


