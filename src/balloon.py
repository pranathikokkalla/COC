import random
from time import sleep,time
import math
from colorama import Fore, Back, Style 

class Balloon():

    def __init__(self):
     
        self.cols=1
        self.rows=1
        self.start_row=0
        self.start_col=0
        self.ball_status=0
        self.ball_health=70.0
        self.ball_damage=10
        self.ball_livestat=1
        self.ball_speed=2
        self.ball_target=-1
        self.bg_pixel=Back.YELLOW+' '+Style.RESET_ALL