from .. import setup
from .. import constants as c


class Enemy():
    """Base class for all enemies (Goombas, Koopas, etc.)"""
    pass


    def setup_enemy(self):
        """Sets up various values for enemy"""
        pass


    def set_velocity(self):
        """Sets velocity vector based on direction"""
        pass



    def get_image(self):
        """Get the image frames from the sprite sheet"""
        pass


    def handle_state(self):
        """Enemy behavior based on state"""
        pass


    def walking(self):
        """Default state of moving sideways"""
        pass


    def falling(self):
        """For when it falls off a ledge"""
        pass

    def jumped_on(self):
        """Placeholder for when the enemy is stomped on"""
        pass


    def death_jumping(self):
        """Death animation"""
        pass


    def start_death_jump(self, direction):
        """Transitions enemy into a DEATH JUMP state"""
        pass


    def animation(self):
        """Basic animation, switching between two frames"""
        pass


    def update(self, game_info, *args):
        """Updates enemy behavior"""
        pass




class Goomba():

    def __init__(self):
        pass


    def setup_frames(self):
        """Put the image frames in a list to be animated"""
        pass


    def jumped_on(self):
        """When Mario squishes him"""
        pass



class Koopa():

    def __init__():
        pass


    def setup_frames(self):
        """Sets frame list"""
        pass


    def jumped_on(self):
        """When Mario jumps on the Koopa and puts him in his shell"""
        pass


    def shell_sliding(self):
        """When the koopa is sliding along the ground in his shell"""
        pass
