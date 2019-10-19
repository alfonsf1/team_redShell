import pygame as pg
from .. import setup
from .. import constants as c


class Digit():
    """Individual digit for score"""
    pass


class Score(object):
    """Scores that appear, float up, and disappear"""
    def __init__(self):
        pass


    def create_image_dict(self):
        """Creates the dictionary for all the number images needed"""
        pass


    def get_image(self):
        """Extracts image from sprite sheet"""
        pass


    def create_digit_list(self):
        pass


    def set_rects_for_images(self):
        """Set the rect attributes for each image in self.image_list"""
        pass


    def update():
        """Updates score movement"""
        pass


    def draw(self):
        """Draws score numbers onto screen"""
        pass


    def check_to_delete_floating_scores(self, score_list, level_info):
        """Check if scores need to be deleted"""
        pass
