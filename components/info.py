import pygame as pg
from .. import setup
from .. import constants as c
from . import flashing_coin


class Character():
    """Parent class for all characters used for the overhead level info"""
    def __init__(self):
        pass


class OverheadInfo():
    """Class for level information like score, coin total,
        and time remaining"""
    def __init__(self):
        pass


    def create_image_dict(self):
        """Creates the initial images for the score"""
        pass


    def get_image(self):
        """Extracts image from sprite sheet"""
        pass


    def create_score_group(self):
        """Creates the initial empty score (000000)"""
        pass


    def create_info_labels(self):
        """Creates the labels that describe each info"""
        pass


    def create_load_screen_labels(self):
        """Creates labels for the center info of a load screen"""
        pass

    def create_countdown_clock(self):
        """Creates the count down clock for the level"""
        pass


    def create_label(self):
        """Creates a label (WORLD, TIME, MARIO)"""
        pass


    def set_label_rects(self):
        """Set the location of each individual character"""
        pass


    def create_coin_counter(self):
        """Creates the info that tracks the number of coins Mario collects"""
        pass


    def create_flashing_coin(self):
        """Creates the flashing coin next to the coin total"""
        pass


    def create_mario_image(self):
        """Get the mario image"""
        pass


    def create_game_over_label(self):
        """Create the label for the GAME OVER screen"""
        pass


    def create_time_out_label(self):
        """Create the label for the time out screen"""
        pass


    def create_main_menu_labels(self):
        """Create labels for the MAIN MENU screen"""
        pass


    def update(self):
        """Updates all overhead info"""
        pass


    def handle_level_state(self):
        """Updates info based on what state the game is in"""
        pass


    def update_score_images(self):
        """Updates what numbers are to be blitted for the score"""
        pass


    def update_count_down_clock(self):
        """Updates current time"""
        pass


    def update_coin_total(self):
        """Updates the coin total and adjusts label accordingly"""
        pass


    def draw(self):
        """Draws overhead info based on state"""
        pass



    def draw_main_menu_info(self):
        pass

    def draw_loading_screen_info(self):
        """Draws info for loading screen"""
        pass


    def draw_level_screen_info(self):
        """Draws info during regular game play"""
        pass


    def draw_game_over_screen_info(self):
        """Draws info when game over"""
        pass


    def draw_time_out_screen_info(self):
        """Draws info when on the time out screen"""
        pass
