
import pygame as pg
from .. import setup
from .. import constants as c

class Flag():
    """Flag on top of the flag pole at the end of the level"""
    def __init__(self):
        pass


    def setup_images(self):
        """Sets up a list of image frames"""
        pass


    def get_image(self):
        """Extracts image from sprite sheet"""
        pass


    def update(self):
        """Updates behavior"""
        pass


    def handle_state(self):
        """Determines behavior based on state"""
        pass


    def sliding_down(self):
        """State when Mario reaches flag pole"""
        pass


class Pole():
    """Pole that the flag is on top of"""
    def __init__(self):
        pass


    def setup_frames(self):
        """Create the frame list"""
        pass


    def get_image(self):
        """Extracts image from sprite sheet"""
        pass


    def update(self):
        """Placeholder for update, since there is nothing to update"""
        pass


class Finial():
    """The top of the flag pole"""
    def __init__(self):
        pass

    def setup_frames(self):
        """Creates the self.frames list"""
        pass

    def get_image(self):
        """Extracts image from sprite sheet"""
        pass


    def update(self):
        pass
