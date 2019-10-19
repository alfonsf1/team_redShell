

import pygame as pg
from . import setup
from . import constants as c

class Sound(object):
    """Handles all sound for the game"""
    def __init__(self, overhead_info):
        pass



    def set_music_mixer(self):
        """Sets music for level"""
        pass


    def update(self, game_info, mario):
        """Updates sound object with game info"""
        pass

    def  handle_state(self):
        """Handles the state of the soundn object"""
        pass


    def play_music(self, key, state):
        """Plays new music"""
        pass

    def stop_music(self):
        """Stops playback"""
        pass
