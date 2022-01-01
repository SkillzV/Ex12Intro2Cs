#############################################################
# FILE : game.py
# WRITER 1: Nitzan Ventura , nitzanv2 , 207378688
# WRITER 2: Shani Amoils , shani.amoils , 212076616
# EXERCISE : intro2cs1 ex2 2021
# STUDENTS I DISCUSSED WITH:
# DESCRIPTION:
#############################################################

import time

EMPTY = ""


class Timer:
    """
    A class for a timer in the game of Boggle.
    """

    def __init__(self, max_time: float, max_time_reached_delegate):
        self.max_time = max_time
        self.on_countdown_reached = max_time_reached_delegate

    def countdown(self):
        t = self.max_time
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            print(timer)
            time.sleep(1)
            t -= 1
        self.__max_time_reached()

    def __max_time_reached(self):
        self.on_countdown_reached()
