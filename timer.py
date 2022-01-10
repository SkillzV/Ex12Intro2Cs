#############################################################
# FILE : game.py
# WRITER 1: Nitzan Ventura , nitzanv2 , 207378688
# WRITER 2: Shani Amoils , shani.amoils , 212076616
# EXERCISE : intro2cs1 ex2 2021
# STUDENTS I DISCUSSED WITH:
# DESCRIPTION:
#############################################################

import time
import threading

EMPTY = ""


class Timer:
    """
    A class for a timer in the game of Boggle.
    """

    def __init__(self, max_time: float, max_time_reached_delegate, on_interval):
        self.max_time = max_time
        self.__on_interval = on_interval
        self.__on_countdown_reached = max_time_reached_delegate
        self._game_control_thread = threading.Thread(
            target=Timer.run_timer, args=(self,))
        self._game_control_thread.daemon = True

    def countdown(self):
        self._game_control_thread.start()

    def run_timer(self):
        t = self.max_time
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            time.sleep(1)
            self.__on_interval(timer)
            t -= 1
        self.__max_time_reached()

    def __max_time_reached(self):
        self.__on_countdown_reached()

    def get_current_time(self):
        return self.__cur_time
