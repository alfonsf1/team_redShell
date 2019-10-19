

import pygame as pg
from .. import setup, tools
from .. import constants as c
from . import powerups


class Mario():
    def __init__(self):
        pass


    def setup_timers(self):
        """Sets up timers for animations"""
        pass


    def setup_state_booleans(self):
        """Sets up booleans that affect Mario's behavior"""
        pass


    def setup_forces(self):
        """Sets up forces that affect Mario's velocity"""
        pass


    def setup_counters(self):
        """These keep track of various total for important values"""
        pass


    def load_images_from_sheet(self):
        pass


    def get_image(self):
        """Extracts image from sprite sheet"""
        pass


    def update(self):
        """Updates Mario's states and animations once per frame"""
        pass


    def handle_state(self, keys, fire_group):
        """Determines Mario's behavior based on his state"""
        pass


    def standing(self):
        """This function is called if Mario is standing still"""
        pass


    def get_out_of_crouch(self):
        """Get out of crouch"""
        pass


    def check_to_allow_jump(self):
        """Check to allow Mario to jump"""
        pass


    def check_to_allow_fireball(self, keys):
        """Check to allow the shooting of a fireball"""
        pass


    def shoot_fireball(self):
        """Shoots fireball, allowing no more than two to exist at once"""
        pass


    def count_number_of_fireballs(self):
        """Count number of fireballs that exist in the level"""
        pass


    def walking(self):
        """This function is called when Mario is in a walking state
        It changes the frame, checks for holding down the run button,
        checks for a jump, then adjusts the state if necessary"""

        pass


    def calculate_animation_speed(self):
        """Used to make walking animation speed be in relation to
        Mario's x-vel"""
        pass


    def jumping(self):
        """Called when Mario is in a JUMP state."""
        pass


    def falling(self):
        """Called when Mario is in a FALL state"""
        pass


    def jumping_to_death(self):
        """Called when Mario is in a DEATH_JUMP state"""
        pass

    def start_death_jump(self):
        """Used to put Mario in a DEATH_JUMP state"""
        pass


    def changing_to_big(self):
        """Changes Mario's image attribute based on time while
        transitioning to big"""
        pass


    def timer_between_these_two_times(self):
        """Checks if the timer is at the right time for the action. Reduces
        the ugly code."""
        pass


    def set_mario_to_middle_image(self):
        """During a change from small to big, sets mario's image to the
        transition/middle size"""
        pass


    def set_mario_to_small_image(self):
        """During a change from small to big, sets mario's image to small"""
        pass


    def set_mario_to_big_image(self):
        """During a change from small to big, sets mario's image to big"""
        pass


    def become_big(self):
        pass


    def changing_to_fire(self):
        """Called when Mario is in a BIG_TO_FIRE state (i.e. when
        he obtains a fire flower"""
        pass


    def changing_to_small(self):
        """Mario's state and animation when he shrinks from big to small
        after colliding with an enemy"""
        pass


    def adjust_rect(self):
        """Makes sure new Rect has the same bottom and left
        location as previous Rect"""
        pass

    def become_small(self):
        pass


    def flag_pole_sliding(self):
        """State where Mario is sliding down the flag pole"""
        pass


    def sitting_at_bottom_of_pole(self):
        """State when mario is at the bottom of the flag pole"""
        pass


    def set_state_to_bottom_of_pole(self):
        """Sets Mario to the BOTTOM_OF_POLE state"""
        pass


    def walking_to_castle(self):
        """State when Mario walks to the castle to end the level"""
        pass



    def check_for_special_state(self):
        """Determines if Mario is invincible, Fire Mario or recently hurt"""
        pass


    def check_if_invincible(self):
        pass


    def change_frame_list(self):
        pass


    def check_if_fire(self):
        pass


    def check_if_hurt_invincible(self):
        """Check if Mario is still temporarily invincible after getting hurt"""
        pass

    def hurt_invincible_check(self):
        """Makes Mario invincible on a fixed interval"""
        pass


    def check_if_crouching(self):
        """Checks if mario is crouching"""
        pass


    def animation(self):
        """Adjusts Mario's image for animation"""
        pass
