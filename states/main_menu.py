import pygame as pg
from .. import setup, tools
from .. import constants as c
from .. components import info, mario


class Menu():
    def __init__(self):
        """Initializes the state"""
        pass

    def startup(self):
        """Called every time the game's state becomes this one.  Initializes
        certain values"""
        pass


    def setup_cursor(self):
        """Creates the mushroom cursor to select 1 or 2 player game"""
        pass


    def setup_mario(self):
        """Places Mario at the beginning of the level"""
        pass


    def setup_background(self):
        """Setup the background image to blit"""
        pass



    def get_image(self, x, y, width, height, dest, sprite_sheet):
        """Returns images and rects to blit onto the screen"""
        pass


    def update(self):
        """Updates the state every refresh"""
        pass


    def update_cursor(self):
        """Update the position of the cursor"""
        pass


    def reset_game_info(self):
        """Resets the game info in case of a Game Over and restart"""
        pass
