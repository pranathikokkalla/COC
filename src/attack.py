import random
from time import sleep,time
import math
from colorama import Fore, Back, Style 

def barb_wall_attack(barb,walls):
    for wall in walls:
        if(barb.start_row == wall.start_row-1 and barb.start_col >= wall.start_col-1 and barb.start_col <= wall.end_col+1):
            if(wall.live_stat==1):
               wall.health-=barb.barb_damage
               if(wall.health<=0):
                 wall.live_stat=0  
               break       
        elif(barb.start_row == wall.end_row+1 and barb.start_col >= wall.start_col-1 and barb.start_col <= wall.end_col+1):
           if(wall.live_stat==1):
              wall.health-=barb.barb_damage
              if(wall.health<=0):
                 wall.live_stat=0   
              break    
        elif(barb.start_col == wall.start_col-1 and barb.start_row >= wall.start_row-1 and barb.start_row <= wall.end_row+1):
           if(wall.live_stat==1):
              wall.health-=barb.barb_damage
              if(wall.health<=0):
                wall.live_stat=0  
              break   
        elif(barb.start_col == wall.end_col+1 and barb.start_row >= wall.start_row-1 and barb.start_row <= wall.end_row+1):
           if(wall.live_stat==1):
              wall.health-=barb.barb_damage
              if(wall.health<=0):
                wall.live_stat=0     
              break    

def barb_attack(barbarians,townhall,walls,huts,cannons,wizards,flag):
    for barb in barbarians:
        if(barb.barb_livestat==0):
            continue

        if(barb.barb_target<len(huts) and barb.barb_target>-1):
           if(huts[barb.barb_target].hut_livestat==0):
                barb.barb_target=-1
        if(barb.barb_target==5):
            if(townhall.townhall_livestat==0):
                barb.barb_target=-1        
        if(barb.barb_target>5 and barb.barb_target<len(cannons)+6):
            if(cannons[barb.barb_target-6].cannon_livestat==0):
                barb.barb_target=-1
        if(barb.barb_target>len(cannons)+5):
            if(wizards[barb.barb_target-len(cannons)-6].wiz_livestat==0):
                barb.barb_target=-1        

        if(barb.barb_target==-1):
            mindist=100000
            dist = 0
            for i in range(0,len(huts)):
                dist=math.sqrt((barb.start_row-huts[i].start_row)**2+(barb.start_col-huts[i].start_col)**2)
                if(huts[i].hut_livestat==1 and dist<=mindist):
                    mindist=dist
                    barb.barb_target=i
            if(townhall.townhall_livestat==1):            
                for i in range(0, townhall.rows) :
                    for j in range(0, townhall.cols) : 
                      dist=math.sqrt((i+townhall.start_row-barb.start_row)**2+(j+townhall.start_col-barb.start_col)**2) 
                      if(dist<=mindist):
                        mindist=dist
                        barb.barb_target=5
                        break         
            for i in range(0,len(cannons)):
                dist=math.sqrt((barb.start_row-cannons[i].start_row)**2+(barb.start_col-cannons[i].start_col)**2)
                if(cannons[i].cannon_livestat==1 and dist<=mindist):
                    mindist=dist
                    barb.barb_target=i+6
            for i in range(0,len(wizards)):
                dist=math.sqrt((barb.start_row-wizards[i].start_row)**2+(barb.start_col-wizards[i].start_col)**2)
                if(wizards[i].wiz_livestat==1 and dist<=mindist):
                    mindist=dist
                    barb.barb_target=i+len(cannons)+6 

        if(barb.barb_target<len(huts) and barb.barb_target>-1):
                if(barb.start_row>huts[barb.barb_target].start_row and barb.start_col<huts[barb.barb_target].start_col):
                    if(flag[barb.start_row-1][barb.start_col+1]):
                       barb.start_row=barb.start_row-1
                       barb.start_col=barb.start_col+1
                    else:
                        barb_wall_attack(barb,walls)
                if(barb.start_row<huts[barb.barb_target].start_row and barb.start_col<huts[barb.barb_target].start_col):
                    if(flag[barb.start_row+1][barb.start_col+1]):
                      barb.start_row=barb.start_row+1
                      barb.start_col=barb.start_col+1
                    else:
                        barb_wall_attack(barb,walls)
                if(barb.start_row<huts[barb.barb_target].start_row and barb.start_col>huts[barb.barb_target].start_col):
                    if(flag[barb.start_row+1][barb.start_col-1]):
                       barb.start_row=barb.start_row+1
                       barb.start_col=barb.start_col-1
                    else:
                        barb_wall_attack(barb,walls)
                if(barb.start_row>huts[barb.barb_target].start_row and barb.start_col>huts[barb.barb_target].start_col):
                    if(flag[barb.start_row-1][barb.start_col-1]):
                       barb.start_row=barb.start_row-1
                       barb.start_col=barb.start_col-1
                    else:
                        barb_wall_attack(barb,walls)
                if(barb.start_row==huts[barb.barb_target].start_row and barb.start_col<huts[barb.barb_target].start_col-1):
                    if(flag[barb.start_row][barb.start_col+1]):
                       barb.start_col=barb.start_col+1
                    else:
                        barb_wall_attack(barb,walls)
                if(barb.start_row==huts[barb.barb_target].start_row and barb.start_col>huts[barb.barb_target].start_col+1):
                    if(flag[barb.start_row][barb.start_col-1]):
                       barb.start_col=barb.start_col-1
                    else:
                        barb_wall_attack(barb,walls)
                if(barb.start_row<huts[barb.barb_target].start_row-1 and barb.start_col==huts[barb.barb_target].start_col):
                    if(flag[barb.start_row+1][barb.start_col]):
                        barb.start_row=barb.start_row+1
                    else:
                        barb_wall_attack(barb,walls)
                if(barb.start_row>huts[barb.barb_target].start_row+1 and barb.start_col==huts[barb.barb_target].start_col):
                    if(flag[barb.start_row-1][barb.start_col]):
                        barb.start_row=barb.start_row-1
                    else:
                        barb_wall_attack(barb,walls)
                if(barb.start_row == huts[barb.barb_target].start_row-1 and barb.start_col >= huts[barb.barb_target].start_col-1):
                     huts[barb.barb_target].hut_health-=barb.barb_damage
                     if(huts[barb.barb_target].hut_health<=0):
                        huts[barb.barb_target].hut_livestat=0
                        barb.barb_target=-1
                elif(barb.start_row == huts[barb.barb_target].start_row+1 and barb.start_col >= huts[barb.barb_target].start_col-1):
                      huts[barb.barb_target].hut_health-=barb.barb_damage
                      if(huts[barb.barb_target].hut_health<=0):
                         huts[barb.barb_target].hut_livestat=0
                         barb.barb_target=-1
                elif(barb.start_col == huts[barb.barb_target].start_col-1 and barb.start_row > huts[barb.barb_target].start_row-1):
                    huts[barb.barb_target].hut_health-=barb.barb_damage
                    if(huts[barb.barb_target].hut_health<=0):
                       huts[barb.barb_target].hut_livestat=0
                       barb.barb_target=-1
                elif(barb.start_col == huts[barb.barb_target].start_col+1 and barb.start_row > huts[barb.barb_target].start_row-1):
                    huts[barb.barb_target].hut_health-=barb.barb_damage
                    if(huts[barb.barb_target].hut_health<=0):
                      huts[barb.barb_target].hut_livestat=0  
                      barb.barb_target=-1
        
        if(barb.barb_target==5):    
                if(barb.start_row<townhall.start_row and barb.start_row<townhall.end_row and barb.start_col>townhall.end_col):
                    if(flag[barb.start_row+1][barb.start_col-1]==0):
                        barb_wall_attack(barb,walls) 
                    else:    
                        barb.start_row=barb.start_row+1
                        barb.start_col=barb.start_col-1
                if(barb.start_row>townhall.start_row and barb.start_row>townhall.end_row and barb.start_col>townhall.end_col):
                    if(flag[barb.start_row-1][barb.start_col-1]==0):
                        barb_wall_attack(barb,walls)
                    else:
                        barb.start_row=barb.start_row-1
                        barb.start_col=barb.start_col-1
                if(barb.start_row>townhall.start_row and barb.start_row>townhall.end_row and barb.start_col<townhall.start_col):
                    if(flag[barb.start_row-1][barb.start_col+1]==0):
                        barb_wall_attack(barb,walls)
                    else:
                        barb.start_row=barb.start_row-1
                        barb.start_col=barb.start_col+1
                if(barb.start_row<townhall.start_row and barb.start_row<townhall.end_row and barb.start_col<townhall.start_col):
                    if(flag[barb.start_row+1][barb.start_col+1]==0):
                        barb_wall_attack(barb,walls)
                    else:
                        barb.start_row=barb.start_row+1
                        barb.start_col=barb.start_col+1
                if(barb.start_row>=townhall.start_row and barb.start_row<=townhall.end_row and barb.start_col<townhall.start_col-1):
                    if(flag[barb.start_row][barb.start_col+1]==0):
                        barb_wall_attack(barb,walls)
                    else:
                       barb.start_col=barb.start_col+1
                if(barb.start_row>=townhall.start_row and barb.start_row<=townhall.end_row and barb.start_col>townhall.end_col+1):
                    if(flag[barb.start_row][barb.start_col-1]==0):
                        barb_wall_attack(barb,walls)
                    else:
                       barb.start_col=barb.start_col-1
                if(barb.start_row<townhall.start_row-1 and barb.start_col>=townhall.start_col and barb.start_col<=townhall.end_col):
                    if(flag[barb.start_row+1][barb.start_col]==0):
                        barb_wall_attack(barb,walls)
                    else:
                        barb.start_row=barb.start_row+1
                if(barb.start_row>townhall.end_row+1 and barb.start_col>=townhall.start_col and barb.start_col<=townhall.end_col):
                    if(flag[barb.start_row-1][barb.start_col]==0):
                        barb_wall_attack(barb,walls)
                    else:
                       barb.start_row=barb.start_row-1
                if(barb.start_row == townhall.start_row-1 and barb.start_col >= townhall.start_col-1 and barb.start_col <= townhall.end_col+1):
                   if(townhall.townhall_livestat==1):
                     townhall.townhall_health-=barb.barb_damage
                     if(townhall.townhall_health<=0):
                        townhall.townhall_livestat=0   
                        barb.barb_target=-1 
                elif(barb.start_row == townhall.end_row+1 and barb.start_col >= townhall.start_col-1 and barb.start_col <= townhall.end_col+1):
                   if(townhall.townhall_livestat==1):
                      townhall.townhall_health-=barb.barb_damage
                      if(townhall.townhall_health<=0):
                        townhall.townhall_livestat=0  
                        barb.barb_target=-1   
                elif(barb.start_col == townhall.start_col-1 and barb.start_row >= townhall.start_row-1 and barb.start_row <= townhall.end_row+1):
                    if(townhall.townhall_livestat==1):
                        townhall.townhall_health-=barb.barb_damage
                        if(townhall.townhall_health<=0):
                            townhall.townhall_livestat=0  
                            barb.barb_target=-1   
                elif(barb.start_col == townhall.end_col+1 and barb.start_row >= townhall.start_row-1 and barb.start_row <= townhall.end_row+1):
                    if(townhall.townhall_livestat==1):
                        townhall.townhall_health-=barb.barb_damage
                        if(townhall.townhall_health<=0):
                            townhall.townhall_livestat=0    
                            barb.barb_target=-1

        if(barb.barb_target>5 and barb.barb_target<len(cannons)+6):
                if(barb.start_row>cannons[barb.barb_target-6].start_row and barb.start_col<cannons[barb.barb_target-6].start_col):
                    if(flag[barb.start_row-1][barb.start_col+1]):
                        barb.start_row=barb.start_row-1
                        barb.start_col=barb.start_col+1
                    else:
                        barb_wall_attack(barb,walls)
                if(barb.start_row<cannons[barb.barb_target-6].start_row and barb.start_col<cannons[barb.barb_target-6].start_col):
                    if(flag[barb.start_row+1][barb.start_col+1]):
                        barb.start_row=barb.start_row+1
                        barb.start_col=barb.start_col+1
                    else:
                        barb_wall_attack(barb,walls)
                if(barb.start_row<cannons[barb.barb_target-6].start_row and barb.start_col>cannons[barb.barb_target-6].start_col):
                    if(flag[barb.start_row+1][barb.start_col-1]):
                        barb.start_row=barb.start_row+1
                        barb.start_col=barb.start_col-1
                    else:
                        barb_wall_attack(barb,walls)
                if(barb.start_row>cannons[barb.barb_target-6].start_row and barb.start_col>cannons[barb.barb_target-6].start_col):
                    if(flag[barb.start_row-1][barb.start_col-1]):
                        barb.start_row=barb.start_row-1
                        barb.start_col=barb.start_col-1
                    else:
                        barb_wall_attack(barb,walls)
                if(barb.start_row==cannons[barb.barb_target-6].start_row and barb.start_col<cannons[barb.barb_target-6].start_col-1):
                    if(flag[barb.start_row][barb.start_col+1]):
                        barb.start_col=barb.start_col+1
                    else:
                        barb_wall_attack(barb,walls)
                if(barb.start_row==cannons[barb.barb_target-6].start_row and barb.start_col>cannons[barb.barb_target-6].start_col+1):
                    if(flag[barb.start_row][barb.start_col-1]):
                        barb.start_col=barb.start_col-1
                    else:
                        barb_wall_attack(barb,walls)
                if(barb.start_row<cannons[barb.barb_target-6].start_row-1 and barb.start_col==cannons[barb.barb_target-6].start_col):
                    if(flag[barb.start_row+1][barb.start_col]):
                        barb.start_row=barb.start_row+1
                    else:
                        barb_wall_attack(barb,walls)
                if(barb.start_row>cannons[barb.barb_target-6].start_row+1 and barb.start_col==cannons[barb.barb_target-6].start_col):
                    if(flag[barb.start_row-1][barb.start_col]):
                        barb.start_row=barb.start_row-1
                    else:
                        barb_wall_attack(barb,walls)
                if(barb.start_row == cannons[barb.barb_target-6].start_row-1 and barb.start_col >= cannons[barb.barb_target-6].start_col-1):
                     cannons[barb.barb_target-6].cannon_health-=barb.barb_damage
                     if(cannons[barb.barb_target-6].cannon_health<=0):
                        cannons[barb.barb_target-6].cannon_livestat=0
                        barb.barb_target=-1
                elif(barb.start_row == cannons[barb.barb_target-6].start_row+1 and barb.start_col >= cannons[barb.barb_target-6].start_col-1):
                      cannons[barb.barb_target-6].cannon_health-=barb.barb_damage
                      if(cannons[barb.barb_target-6].cannon_health<=0):
                         cannons[barb.barb_target-6].cannon_livestat=0
                         barb.barb_target=-1
                elif(barb.start_col == cannons[barb.barb_target-6].start_col-1 and barb.start_row > cannons[barb.barb_target-6].start_row-1):
                    cannons[barb.barb_target-6].cannon_health-=barb.barb_damage
                    if(cannons[barb.barb_target-6].cannon_health<=0):
                       cannons[barb.barb_target-6].cannon_livestat=0
                       barb.barb_target=-1
                elif(barb.start_col == cannons[barb.barb_target-6].start_col+1 and barb.start_row > cannons[barb.barb_target-6].start_row-1):
                    cannons[barb.barb_target-6].cannon_health-=barb.barb_damage
                    if(cannons[barb.barb_target-6].cannon_health<=0):
                      cannons[barb.barb_target-6].cannon_livestat=0  
                      barb.barb_target=-1          

        if(barb.barb_target>len(cannons)+5):
                if(barb.start_row>wizards[barb.barb_target-6-len(cannons)].start_row and barb.start_col<wizards[barb.barb_target-6-len(cannons)].start_col):
                    if(flag[barb.start_row-1][barb.start_col+1]):
                        barb.start_row=barb.start_row-1
                        barb.start_col=barb.start_col+1
                    else:
                        barb_wall_attack(barb,walls)
                if(barb.start_row<wizards[barb.barb_target-6-len(cannons)].start_row and barb.start_col<wizards[barb.barb_target-6-len(cannons)].start_col):
                    if(flag[barb.start_row+1][barb.start_col+1]):
                        barb.start_row=barb.start_row+1
                        barb.start_col=barb.start_col+1
                    else:
                        barb_wall_attack(barb,walls)
                if(barb.start_row<wizards[barb.barb_target-6-len(cannons)].start_row and barb.start_col>wizards[barb.barb_target-6-len(cannons)].start_col):
                    if(flag[barb.start_row+1][barb.start_col-1]):
                        barb.start_row=barb.start_row+1
                        barb.start_col=barb.start_col-1
                    else:
                        barb_wall_attack(barb,walls)
                if(barb.start_row>wizards[barb.barb_target-6-len(cannons)].start_row and barb.start_col>wizards[barb.barb_target-6-len(cannons)].start_col):
                    if(flag[barb.start_row-1][barb.start_col-1]):
                        barb.start_row=barb.start_row-1
                        barb.start_col=barb.start_col-1
                    else:
                        barb_wall_attack(barb,walls)
                if(barb.start_row==wizards[barb.barb_target-6-len(cannons)].start_row and barb.start_col<wizards[barb.barb_target-6-len(cannons)].start_col-1):
                    if(flag[barb.start_row][barb.start_col+1]):
                        barb.start_col=barb.start_col+1
                    else:
                        barb_wall_attack(barb,walls)
                if(barb.start_row==wizards[barb.barb_target-6-len(cannons)].start_row and barb.start_col>wizards[barb.barb_target-6-len(cannons)].start_col+1):
                    if(flag[barb.start_row][barb.start_col-1]):
                        barb.start_col=barb.start_col-1
                    else:
                        barb_wall_attack(barb,walls)
                if(barb.start_row<wizards[barb.barb_target-6-len(cannons)].start_row-1 and barb.start_col==wizards[barb.barb_target-6-len(cannons)].start_col):
                    if(flag[barb.start_row+1][barb.start_col]):
                        barb.start_row=barb.start_row+1
                    else:
                        barb_wall_attack(barb,walls)
                if(barb.start_row>wizards[barb.barb_target-6-len(cannons)].start_row+1 and barb.start_col==wizards[barb.barb_target-6-len(cannons)].start_col):
                    if(flag[barb.start_row-1][barb.start_col]):
                        barb.start_row=barb.start_row-1
                    else:
                        barb_wall_attack(barb,walls)
                if(barb.start_row == wizards[barb.barb_target-6-len(cannons)].start_row-1 and barb.start_col >= wizards[barb.barb_target-6-len(cannons)].start_col-1):
                     wizards[barb.barb_target-6-len(cannons)].wiz_health-=barb.barb_damage
                     if(wizards[barb.barb_target-6-len(cannons)].wiz_health<=0):
                        wizards[barb.barb_target-6-len(cannons)].wiz_livestat=0
                        barb.barb_target=-1
                elif(barb.start_row == wizards[barb.barb_target-6-len(cannons)].start_row+1 and barb.start_col >= wizards[barb.barb_target-6-len(cannons)].start_col-1):
                      wizards[barb.barb_target-6-len(cannons)].wiz_health-=barb.barb_damage
                      if(wizards[barb.barb_target-6-len(cannons)].wiz_health<=0):
                         wizards[barb.barb_target-6-len(cannons)].wiz_livestat=0
                         barb.barb_target=-1
                elif(barb.start_col == wizards[barb.barb_target-6-len(cannons)].start_col-1 and barb.start_row > wizards[barb.barb_target-6-len(cannons)].start_row-1):
                    wizards[barb.barb_target-6-len(cannons)].wiz_health-=barb.barb_damage
                    if(wizards[barb.barb_target-6-len(cannons)].wiz_health<=0):
                       wizards[barb.barb_target-6-len(cannons)].wiz_livestat=0
                       barb.barb_target=-1
                elif(barb.start_col == wizards[barb.barb_target-6-len(cannons)].start_col+1 and barb.start_row > wizards[barb.barb_target-6-len(cannons)].start_row-1):
                    wizards[barb.barb_target-6-len(cannons)].wiz_health-=barb.barb_damage
                    if(wizards[barb.barb_target-6-len(cannons)].wiz_health<=0):
                      wizards[barb.barb_target-6-len(cannons)].wiz_livestat=0  
                      barb.barb_target=-1                        


                          


                     




                                       
                    







