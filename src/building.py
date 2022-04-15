import random
from time import sleep,time
import math
from colorama import Fore, Back, Style 

class Building():
        
        def __init__(self):
            
           
            self.start_row = 0
            self.start_col = 0
            
    
class Cannon(Building):
    
    def __init__(self):
        Building.__init__(self)

        self.cols = 1
        self.rows = 1 
        self.end_row=0
        self.end_col=0
        self.cannon_health = 100
        self.cannon_damage=20
        self.cannon_livestat=1
        self.cannon_range=6
        self.cannon_target=-1
        self.cannon_time=-0.5
        self.bg_pixel = Back.GREEN+'C'+Style.RESET_ALL

class Wizard(Building):      

    def __init__(self):
        Building.__init__(self)
        
        self.cols = 1
        self.rows = 1
        self.wiz_health = 100
        self.wiz_damage=20
        self.wiz_livestat=1
        self.wiz_range=6
        self.wiz_time=-0.5
        self.wiz_target=-1
        self.bg_pixel = Back.GREEN+' '+Style.RESET_ALL  

class Hut(Building):
    
    def __init__(self):
        Building.__init__(self)

        self.cols = 1
        self.rows = 1
        self.end_row = 0
        self.end_col = 0
        self.hut_health = 50
        self.hut_livestat = 1
        self.bg_pixel = Back.GREEN+' '+Style.RESET_ALL

class Wall(Building):
    
    def __init__(self):
        Building.__init__(self)

        self.rows = 1
        self.cols = 1
        self.end_row = 0
        self.end_col=0
        self.health = 35
        self.live_stat = 1
        self.bg_pixel = Back.LIGHTWHITE_EX+' '+Style.RESET_ALL        

class Townhall():

    def __init__(self):

        self.cols = 3
        self.rows = 4
        self.start_row = 24
        self.end_row = 27
        self.start_col = 48
        self.end_col = 50
        self.townhall_health = 150
        self.townhall_livestat=1
        self.bg_pixel = Back.GREEN+' '+Style.RESET_ALL
