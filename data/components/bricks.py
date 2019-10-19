import pygame as pg
from .. import setup
from .. import constants as c
from . import powerups
from . import coin


class Brick():
    """Bricks that can be destroyed"""
    def __init__(self):
        """Initialize the object"""
        pass


    def get_image(self):
        """Extracts the image from the sprite sheet"""
        pass


    def setup_frames(self):
        """Set the frames to a list"""
        pass


    def setup_contents(self):
        """Put 6 coins in contents if needed"""
        pass


    def update(self):
        """Updates the brick"""



    def handle_states(self):
        """Determines brick behavior based on state"""
        pass


    def resting(self):
        """State when not moving"""
        pass


    def bumped(self):
        """Action during a BUMPED state"""
        pass


    def start_bump(self):
        """Transitions brick into BUMPED state"""
        pass


    def opened(self):
        """Action during OPENED state"""


class BrickPiece(pass):
    """Pieces that appear when bricks are broken"""
    def __init__(self):

        pass


    def setup_frames(self):
        """create the frame list"""
        pass


    def get_image(self):
        """Extract image from sprite sheet"""
        pass


    def update(self):
        """Update brick piece"""
        pass

    def check_if_off_screen(self):
        """Remove from sprite groups if off screen"""
        pass
