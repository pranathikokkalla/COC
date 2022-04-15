import random
from time import sleep,time
import math
from colorama import Fore, Back, Style 
from src.building import *

class King():

    def __init__(self):

        self.cols = 1
        self.rows = 1
        self.start_row = 3
        self.end_row = 3
        self.start_col = 49
        self.end_col = 49
        self.king_status = 0
        self.king_damage = 30
        self.king_health = 120.0
        self.king_speed = 1
        self.king_livestat = 1
        self.bg_pixel = Back.BLUE+' '+Style.RESET_ALL

    def king_move(self,key,flag,king):
    
        if(key == 'w'):
            if((king.start_row!=0 and king.king_speed ==1) or (king.start_row>=2 and king.king_speed ==2)):
                if(flag[king.start_row-king.king_speed][king.start_col] == 1 and flag[king.start_row-king.king_speed][king.end_col] == 1):
                    if(king.king_speed == 2):
                       if(flag[king.start_row-1][king.start_col] == 1 and flag[king.start_row-1][king.end_col] == 1):
                          king.start_row -= king.king_speed
                          king.end_row -= king.king_speed
                    else:
                        king.start_row -= king.king_speed
                        king.end_row -= king.king_speed      
                elif(king.king_speed == 2):
                    if(flag[king.start_row-1][king.start_col] == 1 and flag[king.start_row-1][king.end_col] == 1):
                        king.start_row -= 1
                        king.end_row -= 1
    
        if(key == 's'):
            if((king.end_row!=49 and king.king_speed ==1) or (king.end_row<=47 and king.king_speed ==2)):
                if(flag[king.end_row+king.king_speed][king.start_col] == 1 and flag[king.end_row+king.king_speed][king.end_col] == 1):
                    if(king.king_speed == 2):
                        if(flag[king.end_row+1][king.start_col] == 1 and flag[king.end_row+1][king.end_col] == 1):
                           king.start_row += king.king_speed
                           king.end_row += king.king_speed
                    else:
                        king.start_row += king.king_speed
                        king.end_row += king.king_speed
                elif(king.king_speed == 2):
                    if(flag[king.end_row+1][king.start_col] == 1 and flag[king.end_row+1][king.end_col] == 1):
                        king.start_row += 1
                        king.end_row += 1
    
        if(key == 'a'):
            if((king.start_col!=0 and king.king_speed ==1) or (king.start_col>=2 and king.king_speed ==2)):
                if(flag[king.start_row][king.start_col-king.king_speed] == 1 and flag[king.end_row][king.start_col-king.king_speed] == 1):
                    if(king.king_speed == 2):
                        if(flag[king.start_row][king.start_col-1] == 1 and flag[king.end_row][king.start_col-1] == 1):
                           king.start_col -= king.king_speed
                           king.end_col -= king.king_speed
                    else:
                        king.start_col -= king.king_speed
                        king.end_col -= king.king_speed
                elif(king.king_speed == 2):
                    if(flag[king.start_row][king.start_col-1] == 1 and flag[king.end_row][king.start_col-1] == 1):
                        king.start_col -= 1
                        king.end_col -= 1
    
        if(key == 'd'):
            if((king.end_col!=99 and king.king_speed ==1) or (king.end_col<=97 and king.king_speed ==2)):
                if(flag[king.start_row][king.end_col+king.king_speed] == 1 and flag[king.end_row][king.end_col+king.king_speed] == 1):
                    if(king.king_speed == 2):
                        if(flag[king.start_row][king.end_col+1] == 1 and flag[king.end_row][king.end_col+1] == 1):
                           king.start_col += king.king_speed
                           king.end_col += king.king_speed
                    else:
                        king.start_col += king.king_speed
                        king.end_col += king.king_speed
                elif(king.king_speed == 2):
                    if(flag[king.start_row][king.end_col+1] == 1 and flag[king.end_row][king.end_col+1] == 1):
                        king.start_col += 1
                        king.end_col += 1               
    
        return king   
    

def king_attack(king,flag,walls,th,cannons,huts,wizards):

    townhall=Townhall()
   

    #townhall attack

    if(king.start_row == townhall.start_row-1 and king.start_col >= townhall.start_col-1 and king.end_col <= townhall.end_col+1):
        if(th.townhall_livestat==1):
            th.townhall_health-=king.king_damage
            if(th.townhall_health<=0):
                th.townhall_livestat=0
            return flag      
    elif(king.start_row == townhall.end_row+1 and king.start_col >= townhall.start_col-1 and king.end_col <= townhall.end_col+1):
        if(th.townhall_livestat==1):
            th.townhall_health-=king.king_damage
            if(th.townhall_health<=0):
                th.townhall_livestat=0
            return flag      
    elif(king.start_col == townhall.start_col-1 and king.start_row >= townhall.start_row-1 and king.end_row <= townhall.end_row+1):
        if(th.townhall_livestat==1):
            th.townhall_health-=king.king_damage
            if(th.townhall_health<=0):
                th.townhall_livestat=0
            return flag      
    elif(king.start_col == townhall.end_col+1 and king.start_row >= townhall.start_row-1 and king.end_row <= townhall.end_row+1):
        if(th.townhall_livestat==1):
            th.townhall_health-=king.king_damage
            if(th.townhall_health<=0):
                th.townhall_livestat=0
            return flag  

    #wall attack

    for wall in walls:
        if(king.start_row == wall.start_row-1 and king.start_col >= wall.start_col-1 and king.end_col <= wall.end_col+1):
            if(wall.live_stat==1):
                wall.health-=king.king_damage
                if(wall.health<=0):
                    wall.live_stat=0  
                break       
        elif(king.start_row == wall.end_row+1 and king.start_col >= wall.start_col-1 and king.end_col <= wall.end_col+1):
            if(wall.live_stat==1):
                wall.health-=king.king_damage
                if(wall.health<=0):
                    wall.live_stat=0   
                break    
        elif(king.start_col == wall.start_col-1 and king.start_row >= wall.start_row-1 and king.end_row <= wall.end_row+1):
            if(wall.live_stat==1):
                wall.health-=king.king_damage
                if(wall.health<=0):
                    wall.live_stat=0  
                break   
        elif(king.start_col == wall.end_col+1 and king.start_row >= wall.start_row-1 and king.end_row <= wall.end_row+1):
            if(wall.live_stat==1):
                wall.health-=king.king_damage
                if(wall.health<=0):
                    wall.live_stat=0     
                break           

    #cannon attack

    for cannon in cannons:
        if(king.start_row == cannon.start_row-1 and king.start_col >= cannon.start_col-1 and king.end_col <= cannon.end_col+1):
            if(cannon.cannon_livestat==1):
                cannon.cannon_health-=king.king_damage
                if(cannon.cannon_health<=0):
                    cannon.cannon_livestat=0
        elif(king.start_row == cannon.end_row+1 and king.start_col >= cannon.start_col-1 and king.end_col <= cannon.end_col+1):
            if(cannon.cannon_livestat==1):
                cannon.cannon_health-=king.king_damage
                if(cannon.cannon_health<=0):
                    cannon.cannon_livestat=0
        elif(king.start_col == cannon.start_col-1 and king.start_row >= cannon.start_row-1 and king.end_row <= cannon.end_row+1):
            if(cannon.cannon_livestat==1):
                cannon.cannon_health-=king.king_damage
                if(cannon.cannon_health<=0):
                    cannon.cannon_livestat=0
        elif(king.start_col == cannon.end_col+1 and king.start_row >= cannon.start_row-1 and king.end_row <= cannon.end_row+1):
            if(cannon.cannon_livestat==1):
                cannon.cannon_health-=king.king_damage
                if(cannon.cannon_health<=0):
                    cannon.cannon_livestat=0
    
    #wizard attack
    for wiz in wizards:
        if(king.start_row == wiz.start_row-1 and king.start_col >= wiz.start_col-1 and king.end_col <= wiz.start_col+1):
            if(wiz.wiz_livestat==1):
                wiz.wiz_health-=king.king_damage
                if(wiz.wiz_health<=0):
                    wiz.wiz_livestat=0
        elif(king.start_row == wiz.start_row+1 and king.start_col >= wiz.start_col-1 and king.end_col <= wiz.start_col+1):
            if(wiz.wiz_livestat==1):
                wiz.wiz_health-=king.king_damage
                if(wiz.wiz_health<=0):
                    wiz.wiz_livestat=0  
        elif(king.start_col == wiz.start_col-1 and king.start_row >= wiz.start_row-1 and king.end_row <= wiz.start_row+1):
            if(wiz.wiz_livestat==1):
                wiz.wiz_health-=king.king_damage
                if(wiz.wiz_health<=0):
                    wiz.wiz_livestat=0
        elif(king.start_col == wiz.start_col+1 and king.start_row >= wiz.start_row-1 and king.end_row <= wiz.start_row+1):
            if(wiz.wiz_livestat==1):
                wiz.wiz_health-=king.king_damage
                if(wiz.wiz_health<=0):
                    wiz.wiz_livestat=0

    #hut attack

    for hut in huts:
        if(king.start_row == hut.start_row-1 and king.start_col >= hut.start_col-1 and king.end_col <= hut.end_col+1):
            if(hut.hut_livestat==1):
                hut.hut_health-=king.king_damage
                if(hut.hut_health<=0):
                    hut.hut_livestat=0
        if(king.start_row == hut.end_row+1 and king.start_col >= hut.start_col-1 and king.end_col <= hut.end_col+1):
            if(hut.hut_livestat==1):
                hut.hut_health-=king.king_damage
                if(hut.hut_health<=0):
                    hut.hut_livestat=0
        if(king.start_col == hut.start_col-1 and king.start_row > hut.start_row-1 and king.end_row < hut.end_row+1):
            if(hut.hut_livestat==1):
                hut.hut_health-=king.king_damage
                if(hut.hut_health<=0):
                    hut.hut_livestat=0
        if(king.start_col == hut.end_col+1 and king.start_row > hut.start_row-1 and king.end_row < hut.end_row+1):
            if(hut.hut_livestat==1):
                hut.hut_health-=king.king_damage
                if(hut.hut_health<=0):
                    hut.hut_livestat=0

    return flag            

def queen_attack(king,flag,walls,th,cannons,huts,wizards,prev_key):

    if(prev_key=='d'):
        #townhall attack
    
        if(th.townhall_livestat==1):            
            for i in range(0, th.rows) :
                for j in range(0, th.cols) : 
                    if(i+th.start_row>=king.start_row-2 and i+th.start_row<=king.end_row+2 and j+th.start_col>=king.start_col+6 and j+th.start_col<=king.end_col+10):
                        th.townhall_health-=king.king_damage
                        if(th.townhall_health<=0):
                            th.townhall_livestat=0
                            break
        #wall attack
    
        for wall in walls:
            if(wall.live_stat==1):
                if(wall.start_row>=king.start_row-2 and wall.start_row<=king.end_row+2 and wall.start_col>=king.start_col+6 and wall.start_col<=king.end_col+10):
                    wall.health-=king.king_damage
                    if(wall.health<=0):
                        wall.live_stat=0
    
        #cannon attack
    
        for cannon in cannons:
            if(cannon.cannon_livestat==1):
                if(cannon.start_row>=king.start_row-2 and cannon.start_row<=king.end_row+2 and cannon.start_col>=king.start_col+6 and cannon.start_col<=king.end_col+10):
                    cannon.cannon_health-=king.king_damage
                    if(cannon.cannon_health<=0):
                        cannon.cannon_livestat=0

        #wizard attack
        for wiz in wizards:
            if(wiz.wiz_livestat==1):
                if(wiz.start_row>=king.start_row-2 and wiz.start_row<=king.end_row+2 and wiz.start_col>=king.start_col+6 and wiz.start_col<=king.end_col+10):
                    wiz.wiz_health-=king.king_damage
                    if(wiz.wiz_health<=0):
                        wiz.wiz_livestat=0                
    
        #hut attack
    
        for hut in huts:
            if(hut.hut_livestat==1):
                if(hut.start_row>=king.start_row-2 and hut.start_row<=king.end_row+2 and hut.start_col>=king.start_col+6 and hut.start_col<=king.end_col+10):
                    hut.hut_health-=king.king_damage
                    if(hut.hut_health<=0):
                        hut.hut_livestat=0

    if(prev_key=='a'):
        #townhall attack
    
        if(th.townhall_livestat==1):            
            for i in range(0, th.rows) :
                for j in range(0, th.cols) : 
                    if(i+th.start_row>=king.start_row-2 and i+th.start_row<=king.end_row+2 and j+th.start_col<=king.start_col-6 and j+th.start_col>=king.end_col-10):
                        th.townhall_health-=king.king_damage
                        if(th.townhall_health<=0):
                            th.townhall_livestat=0
                            break
        #wall attack
    
        for wall in walls:
            if(wall.live_stat==1):
                if(wall.start_row>=king.start_row-2 and wall.start_row<=king.end_row+2 and wall.start_col<=king.start_col-6 and wall.start_col>=king.end_col-10):
                    wall.health-=king.king_damage
                    if(wall.health<=0):
                        wall.live_stat=0
    
        #cannon attack
    
        for cannon in cannons:
            if(cannon.cannon_livestat==1):
                if(cannon.start_row>=king.start_row-2 and cannon.start_row<=king.end_row+2 and cannon.start_col<=king.start_col-6 and cannon.start_col>=king.end_col-10):
                    cannon.cannon_health-=king.king_damage
                    if(cannon.cannon_health<=0):
                        cannon.cannon_livestat=0

        #wizard attack

        for wiz in wizards:
            if(wiz.wiz_livestat==1):
                if(wiz.start_row>=king.start_row-2 and wiz.start_row<=king.end_row+2 and wiz.start_col<=king.start_col-6 and wiz.start_col>=king.end_col-10):
                    wiz.wiz_health-=king.king_damage
                    if(wiz.wiz_health<=0):
                        wiz.wiz_livestat=0                
    
        #hut attack
    
        for hut in huts:
            if(hut.hut_livestat==1):
                if(hut.start_row>=king.start_row-2 and hut.start_row<=king.start_row+2 and hut.start_col<=king.start_col-6 and hut.start_col>=king.start_col-10):
                    hut.hut_health-=king.king_damage
                    if(hut.hut_health<=0):
                        hut.hut_livestat=0    

    if(prev_key=='w'):
        #townhall attack
    
        if(th.townhall_livestat==1):            
            for i in range(0, th.rows) :
                for j in range(0, th.cols) : 
                    if(i+th.start_row>=king.start_row-10 and i+th.start_row<=king.end_row-6 and j+th.start_col>=king.start_col-2 and j+th.start_col<=king.end_col+2):
                        th.townhall_health-=king.king_damage
                        if(th.townhall_health<=0):
                            th.townhall_livestat=0
                            break
        #wall attack
    
        for wall in walls:
            if(wall.live_stat==1):
                if(wall.start_row>=king.start_row-10 and wall.start_row<=king.end_row-6 and wall.start_col>=king.start_col-2 and wall.start_col<=king.end_col+2):
                    wall.health-=king.king_damage
                    if(wall.health<=0):
                        wall.live_stat=0
    
        #cannon attack
    
        for cannon in cannons:
            if(cannon.cannon_livestat==1):
                if(cannon.start_row>=king.start_row-10 and cannon.start_row<=king.end_row-6 and cannon.start_col>=king.start_col-2 and cannon.start_col<=king.end_col+2):
                    cannon.cannon_health-=king.king_damage
                    if(cannon.cannon_health<=0):
                        cannon.cannon_livestat=0

        #wizard attack

        for wiz in wizards:
            if(wiz.wiz_livestat==1):
                if(wiz.start_row>=king.start_row-10 and wiz.start_row<=king.end_row-6 and wiz.start_col>=king.start_col-2 and wiz.start_col<=king.end_col+2):
                    wiz.wiz_health-=king.king_damage
                    if(wiz.wiz_health<=0):
                        wiz.wiz_livestat=0                
    
        #hut attack
    
        for hut in huts:
            if(hut.hut_livestat==1):
                if(hut.start_row>=king.start_row-10 and hut.start_row<=king.end_row-6 and hut.start_col>=king.start_col-2 and hut.start_col<=king.end_col+2):
                    hut.hut_health-=king.king_damage
                    if(hut.hut_health<=0):
                        hut.hut_livestat=0    

    if(prev_key=='s'):
        #townhall attack
    
        if(th.townhall_livestat==1):            
            for i in range(0, th.rows) :
                for j in range(0, th.cols) : 
                    if(i+th.start_row>=king.start_row+6 and i+th.start_row<=king.end_row+10 and j+th.start_col>=king.start_col-2 and j+th.start_col<=king.end_col+2):
                        th.townhall_health-=king.king_damage
                        if(th.townhall_health<=0):
                            th.townhall_livestat=0
                            break
        #wall attack
    
        for wall in walls:
            if(wall.live_stat==1):
                if(wall.start_row>=king.start_row+6 and wall.start_row<=king.end_row+10 and wall.start_col>=king.start_col-2 and wall.start_col<=king.end_col+2):
                    wall.health-=king.king_damage
                    if(wall.health<=0):
                        wall.live_stat=0
    
        #cannon attack
    
        for cannon in cannons:
            if(cannon.cannon_livestat==1):
                if(cannon.start_row>=king.start_row+6 and cannon.start_row<=king.end_row+10 and cannon.start_col>=king.start_col-2 and cannon.start_col<=king.end_col+2):
                    cannon.cannon_health-=king.king_damage
                    if(cannon.cannon_health<=0):
                        cannon.cannon_livestat=0

        #wizard attack

        for wiz in wizards:
            if(wiz.wiz_livestat==1):
                if(wiz.start_row>=king.start_row+6 and wiz.start_row<=king.end_row+10 and wiz.start_col>=king.start_col-2 and wiz.start_col<=king.end_col+2):
                    wiz.wiz_health-=king.king_damage
                    if(wiz.wiz_health<=0):
                        wiz.wiz_livestat=0                
    
        #hut attack
    
        for hut in huts:
            if(hut.hut_livestat==1):
                if(hut.start_row>=king.start_row+6 and hut.start_row<=king.end_row+10 and hut.start_col>=king.start_col-2 and hut.start_col<=king.end_col+2):
                    hut.hut_health-=king.king_damage
                    if(hut.hut_health<=0):
                        hut.hut_livestat=0   

def eagle_attack(king,flag,walls,th,cannons,huts,wizards,row,col,key):

    if(key=='d'):
        #townhall attack
    
        if(th.townhall_livestat==1):            
            for i in range(0, th.rows) :
                for j in range(0, th.cols) : 
                    if(i+th.start_row>=row-4 and i+th.start_row<=row+4 and j+th.start_col>=col+12 and j+th.start_col<=col+20):
                        th.townhall_health-=king.king_damage
                        if(th.townhall_health<=0):
                            th.townhall_livestat=0
                            break
        #wall attack
    
        for wall in walls:
            if(wall.live_stat==1):
                if(wall.start_row>=row-4 and wall.start_row<=row+4 and wall.start_col>=col+12 and wall.start_col<=col+20):
                    wall.health-=king.king_damage
                    if(wall.health<=0):
                        wall.live_stat=0
    
        #cannon attack
    
        for cannon in cannons:
            if(cannon.cannon_livestat==1):
                if(cannon.start_row>=row-4 and cannon.start_row<=row+4 and cannon.start_col>=col+12 and cannon.start_col<=col+20):
                    cannon.cannon_health-=king.king_damage
                    if(cannon.cannon_health<=0):
                        cannon.cannon_livestat=0

        #wizard attack
        for wiz in wizards:
            if(wiz.wiz_livestat==1):
                if(wiz.start_row>=row-4 and wiz.start_row<=row+4 and wiz.start_col>=col+12 and wiz.start_col<=col+20):
                    wiz.wiz_health-=king.king_damage
                    if(wiz.wiz_health<=0):
                        wiz.wiz_livestat=0                
    
        #hut attack
    
        for hut in huts:
            if(hut.hut_livestat==1):
                if(hut.start_row>=row-4 and hut.start_row<=row+4 and hut.start_col>=col+12 and hut.start_col<=col+20):
                    hut.hut_health-=king.king_damage
                    if(hut.hut_health<=0):
                        hut.hut_livestat=0

    if(key=='a'):
        #townhall attack
    
        if(th.townhall_livestat==1):            
            for i in range(0, th.rows) :
                for j in range(0, th.cols) : 
                    if(i+th.start_row>=row-4 and i+th.start_row<=row+4 and j+th.start_col<=col-12 and j+th.start_col>=col-20):
                        th.townhall_health-=king.king_damage
                        if(th.townhall_health<=0):
                            th.townhall_livestat=0
                            break
        #wall attack
    
        for wall in walls:
            if(wall.live_stat==1):
                if(wall.start_row>=row-4 and wall.start_row<=row+4 and wall.start_col<=col-12 and wall.start_col>=col-20):
                    wall.health-=king.king_damage
                    if(wall.health<=0):
                        wall.live_stat=0
    
        #cannon attack
    
        for cannon in cannons:
            if(cannon.cannon_livestat==1):
                if(cannon.start_row>=row-4 and cannon.start_row<=row+4 and cannon.start_col<=col-12 and cannon.start_col>=col-20):
                    cannon.cannon_health-=king.king_damage
                    if(cannon.cannon_health<=0):
                        cannon.cannon_livestat=0

        #wizard attack

        for wiz in wizards:
            if(wiz.wiz_livestat==1):
                if(wiz.start_row>=row-4 and wiz.start_row<=row+4 and wiz.start_col<=col-12 and wiz.start_col>=col-20):
                    print("entered")
                    wiz.wiz_health-=king.king_damage
                    if(wiz.wiz_health<=0):
                        wiz.wiz_livestat=0                
    
        #hut attack
    
        for hut in huts:
            if(hut.hut_livestat==1):
                if(hut.start_row>=row-4 and hut.start_row<=row+4 and hut.start_col<=col-12 and hut.start_col>=col-20):
                    hut.hut_health-=king.king_damage
                    if(hut.hut_health<=0):
                        hut.hut_livestat=0   

    if(key=='w'):
        #townhall attack
    
        if(th.townhall_livestat==1):            
            for i in range(0, th.rows) :
                for j in range(0, th.cols) : 
                    if(i+th.start_row>=row-20 and i+th.start_row<=row-12 and j+th.start_col>=col-4 and j+th.start_col<=col+4):
                        th.townhall_health-=king.king_damage
                        if(th.townhall_health<=0):
                            th.townhall_livestat=0
                            break
        #wall attack
    
        for wall in walls:
            if(wall.live_stat==1):
                if(wall.start_row>=row-20 and wall.start_row<=row-12 and wall.start_col>=col-4 and wall.start_col<=col+4):
                    wall.health-=king.king_damage
                    if(wall.health<=0):
                        wall.live_stat=0
    
        #cannon attack
    
        for cannon in cannons:
            if(cannon.cannon_livestat==1):
                if(cannon.start_row>=row-20 and cannon.start_row<=row-12 and cannon.start_col>=col-4 and cannon.start_col<=col+4):
                    cannon.cannon_health-=king.king_damage
                    if(cannon.cannon_health<=0):
                        cannon.cannon_livestat=0

        #wizard attack

        for wiz in wizards:
            if(wiz.wiz_livestat==1):
                if(wiz.start_row>=row-20 and wiz.start_row<=row-12 and wiz.start_col>=col-4 and wiz.start_col<=col+4):
                    wiz.wiz_health-=king.king_damage
                    if(wiz.wiz_health<=0):
                        wiz.wiz_livestat=0                
    
        #hut attack
    
        for hut in huts:
            if(hut.hut_livestat==1):
                if(hut.start_row>=row-20 and hut.start_row<=row-12 and hut.start_col>=col-4 and hut.start_col<=col+4):
                    hut.hut_health-=king.king_damage
                    if(hut.hut_health<=0):
                        hut.hut_livestat=0    

    if(key=='s'):
        #townhall attack
    
        if(th.townhall_livestat==1):            
            for i in range(0, th.rows) :
                for j in range(0, th.cols) : 
                    if(i+th.start_row>=row+12 and i+th.start_row<=row+20 and j+th.start_col>=col-4 and j+th.start_col<=col+4):
                        th.townhall_health-=king.king_damage
                        if(th.townhall_health<=0):
                            th.townhall_livestat=0
                            break
        #wall attack
    
        for wall in walls:
            if(wall.live_stat==1):
                if(wall.start_row>=row+12 and wall.start_row<=row+20 and wall.start_col>=col-4 and wall.start_col<=col+4):
                    wall.health-=king.king_damage
                    if(wall.health<=0):
                        wall.live_stat=0
    
        #cannon attack
    
        for cannon in cannons:
            if(cannon.cannon_livestat==1):
                if(cannon.start_row>=row+12 and cannon.start_row<=row+20 and cannon.start_col>=col-4 and cannon.start_col<=col+4):
                    cannon.cannon_health-=king.king_damage
                    if(cannon.cannon_health<=0):
                        cannon.cannon_livestat=0

        #wizard attack

        for wiz in wizards:
            if(wiz.wiz_livestat==1):
                if(wiz.start_row>=row+12 and wiz.start_row<=row+20 and wiz.start_col>=col-4 and wiz.start_col<=col+4):
                    wiz.wiz_health-=king.king_damage
                    if(wiz.wiz_health<=0):
                        wiz.wiz_livestat=0                
    
        #hut attack
    
        for hut in huts:
            if(hut.hut_livestat==1):
                if(hut.start_row>=row+12 and hut.start_row<=row+20 and hut.start_col>=col-4 and hut.start_col<=col+4):
                    hut.hut_health-=king.king_damage
                    if(hut.hut_health<=0):
                        hut.hut_livestat=0                                                              


                                                
            
    
    


