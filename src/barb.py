import random
from time import sleep,time
import math
from colorama import Fore, Back, Style 

class Barb():

    def __init__(self):

        self.cols=1
        self.rows=1
        self.start_row=0
        self.start_col=0
        # self.end_row=0
        # self.end_col=0
        self.barb_status=0
        self.barb_health=70.0
        self.barb_damage=5
        self.barb_livestat=1
        self.barb_speed=1
        self.barb_target=-1
        self.bg_pixel=Back.MAGENTA+' '+Style.RESET_ALL