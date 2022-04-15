import random
from time import sleep,time
import math
from colorama import Fore, Back, Style 

class Archer():

    def __init__(self):
     
        self.cols=1
        self.rows=1
        self.start_row=0
        self.start_col=0
        self.arch_status=0
        self.arch_health=35.0
        self.arch_damage=2.5
        self.arch_livestat=1
        self.arch_speed=2
        self.arch_range=5
        self.arch_target=-1
        self.bg_pixel=Back.RED+' '+Style.RESET_ALL