__author__ = 'justinarmstrong'

import pygame as pg
from .. import constants as c
from .. import setup


class Powerup():
    """Base class for all powerup_group"""
    def __init__(self, x, y):
        pass


    def setup_powerup(self):
        """This separate setup function allows me to pass a different
        setup_frames method depending on what the powerup is"""
        pass


    def get_image(self):
        """Get the image frames from the sprite sheet"""
        pass


    def update(self):
        """Updates powerup behavior"""
        pass


    def sliding(self):
        """Action for when powerup slides along the ground"""
        pass


    def falling(self):
        """When powerups fall of a ledge"""
        pass


class Mushroom():
    """Powerup that makes Mario become bigger"""
    pass


class LifeMushroom():
    """1up mushroom"""
    def __init__(self):
        pass

    def setup_frames(self):
        pass


class FireFlower():
    """Powerup that allows Mario to throw fire balls"""
    def __init__(self, x, y, name=c.FIREFLOWER):
        pass


    def setup_frames(self):
        """Sets up frame list"""
        pass


    def handle_state(self):
        """Handle behavior based on state"""
        pass


    def revealing(self):
        """Animation of flower coming out of box"""
        pass


    def resting(self):
        """Fire Flower staying still on opened box"""
        pass


    def animation(self):
        """Method to make the Fire Flower blink"""
        pass


class Star():
    """A powerup that gives mario invincibility"""
    def __init__(self)
        pass


    def setup_frames(self):
        """Creating the self.frames list where the images for the animation
        are stored"""
        pass


    def handle_state(self):
        """Handles behavior based on state"""
        pass


    def revealing(self):
        """When the star comes out of the box"""
        pass


    def animation(self):
        """sets image for animation"""
        pass

    def start_bounce(self):
        """Transitions into bouncing state"""
        pass


    def bouncing(self):
        """Action when the star is bouncing around"""
        pass


class FireBall():
    """Shot from Fire Mario"""
    def __init__(self):
        pass

    def setup_frames(self):
        """Sets up animation frames"""
        pass


    def get_image(self):
        """Get the image frames from the sprite sheet"""
        pass


    def update(self):
        """Updates fireball behavior"""
        pass

    def handle_state(self):
        """Handles behavior based on state"""
        pass


    def animation(self):
        """adjusts frame for animation"""
        pass


    def explode_transition(self):
        """Transitions fireball to EXPLODING state"""
        pass


    def check_if_off_screen(self, viewport):
        """Removes from sprite group if off screen"""
        pass
