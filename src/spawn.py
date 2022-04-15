import random
from time import sleep,time
import math
from colorama import Fore, Back, Style 
from src.king import *
from src.barb import *
from src.archer import *
from src.balloon import *

def king_spawn():
    
    king = King()
    king.king_status = 1
    
    return king


def barb_spawn1():
    
    barb = Barb()
    barb.barb_status = 1
    barb.start_row = 3
    barb.start_col = 9

    return barb

def barb_spawn2():
    
    barb = Barb()
    barb.barb_status = 1
    barb.start_row = 43
    barb.start_col = 9

    return barb

def barb_spawn3():
    
    barb = Barb()
    barb.barb_status = 1
    barb.start_row = 43
    barb.start_col = 90

    return barb   

def archer_spawn1():
    
    archer = Archer()
    archer.arch_status = 1
    archer.start_row = 3
    archer.start_col = 10    

    return archer

def archer_spawn2():
    
    archer = Archer()
    archer.arch_status = 1
    archer.start_row = 43
    archer.start_col = 10    

    return archer

def archer_spawn3():
    
    archer = Archer()
    archer.arch_status = 1
    archer.start_row = 44
    archer.start_col = 90    

    return archer

def balloon_spawn1():

    balloon=Balloon()
    balloon.ball_status=1
    balloon.start_row=3
    balloon.start_col=11

    return balloon

def balloon_spawn2():
    
    balloon=Balloon()
    balloon.ball_status=1
    balloon.start_row=43
    balloon.start_col=11

    return balloon

def balloon_spawn3():
    
    balloon=Balloon()
    balloon.ball_status=1
    balloon.start_row=45
    balloon.start_col=90

    return balloon