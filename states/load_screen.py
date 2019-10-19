from .. import setup, tools
from .. import constants as c
from .. import game_sound
from ..components import info


class LoadScreen():
    def __init__(self):
        pass

    def startup(self):
        pass

    def set_next_state(self):
        """Sets the next state"""
        pass

    def set_overhead_info_state(self):
        """sets the state to send to the overhead info object"""



    def update(self, surface, keys, current_time):
        """Updates the loading screen"""
        pass




class GameOver():
    """A loading screen with Game Over"""
    pass


    def set_next_state(self):
        """Sets next state"""
        pass

    def set_overhead_info_state(self):
        """sets the state to send to the overhead info object"""
        pass

    def update(self):
        pass


class TimeOut(LoadScreen):
    """Loading Screen with Time Out"""
    def __init__(self):
        pass

    def set_next_state(self):
        """Sets next state"""
        pass

    def set_overhead_info_state(self):
        """Sets the state to send to the overhead info object"""
        pass

    def update(self):
        pass
