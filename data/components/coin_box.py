import pygame as pg
from .. import setup
from .. import constants as c
from . import powerups
from . import coin



class Coin_box(pg.sprite.Sprite):
    """Coin box sprite"""
    def __init__(self):
    pass


    def get_image(self):
        """Extract image from sprite sheet"""
        pass


    def setup_frames(self):
        """Create frame list"""
        pass


    def update(self, game_info):
        """Update coin box behavior"""
        pass

    def handle_states(self):
        """Determine action based on RESTING, BUMPED or OPENED
        state"""
        pass


    def resting(self):
        """Action when in the RESTING state"""
        pass

    def bumped(self):
        """Action after Mario has bumped the box from below"""
        pass


    def start_bump(self, score_group):
        """Transitions box into BUMPED state"""
        pass


    def opened(self):
        """Placeholder for OPENED state"""
        pass
