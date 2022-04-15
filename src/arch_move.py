import random
from time import sleep,time
import math
from colorama import Fore, Back, Style 

def arch_wall_attack(arch,walls):
    for wall in walls:
        if(arch.start_row == wall.start_row-1 and arch.start_col >= wall.start_col-1 and arch.start_col <= wall.end_col+1):
            if(wall.live_stat==1):
               wall.health-=arch.arch_damage
               if(wall.health<=0):
                 wall.live_stat=0  
               break       
        elif(arch.start_row == wall.end_row+1 and arch.start_col >= wall.start_col-1 and arch.start_col <= wall.end_col+1):
           if(wall.live_stat==1):
              wall.health-=arch.arch_damage
              if(wall.health<=0):
                 wall.live_stat=0   
              break    
        elif(arch.start_col == wall.start_col-1 and arch.start_row >= wall.start_row-1 and arch.start_row <= wall.end_row+1):
           if(wall.live_stat==1):
              wall.health-=arch.arch_damage
              if(wall.health<=0):
                wall.live_stat=0  
              break   
        elif(arch.start_col == wall.end_col+1 and arch.start_row >= wall.start_row-1 and arch.start_row <= wall.end_row+1):
           if(wall.live_stat==1):
              wall.health-=arch.arch_damage
              if(wall.health<=0):
                wall.live_stat=0     
              break    

def arch_movement(archers,townhall,walls,huts,cannons,wizards,flag):
    for arch in archers:
        if(arch.arch_livestat==0):
            continue

        if(arch.arch_target<len(huts) and arch.arch_target>-1):
               if(huts[arch.arch_target].hut_livestat==0):
                arch.arch_target=-1
        if(arch.arch_target==5):
            if(townhall.townhall_livestat==0):
                arch.arch_target=-1        
        if(arch.arch_target>5 and arch.arch_target<len(cannons)+6):
            if(cannons[arch.arch_target-6].cannon_livestat==0):
                arch.arch_target=-1
        if(arch.arch_target>len(cannons)+5):
            if(wizards[arch.arch_target-len(cannons)-6].wiz_livestat==0):
                arch.arch_target=-1        

        if(arch.arch_target==-1):
            mindist=100000
            dist = 0
            for i in range(0,len(huts)):
                dist=math.sqrt((arch.start_row-huts[i].start_row)**2+(arch.start_col-huts[i].start_col)**2)
                if(huts[i].hut_livestat==1 and dist<=mindist):
                    mindist=dist
                    arch.arch_target=i
            if(townhall.townhall_livestat==1):            
                for i in range(0, townhall.rows) :
                    for j in range(0, townhall.cols) : 
                      dist=math.sqrt((i+townhall.start_row-arch.start_row)**2+(j+townhall.start_col-arch.start_col)**2) 
                      if(dist<=mindist):
                        mindist=dist
                        arch.arch_target=5
                        break 
            for i in range(0,len(cannons)):
                dist=math.sqrt((arch.start_row-cannons[i].start_row)**2+(arch.start_col-cannons[i].start_col)**2)
                if(cannons[i].cannon_livestat==1 and dist<=mindist):
                    mindist=dist
                    arch.arch_target=i+6
            for i in range(0,len(wizards)):
                dist=math.sqrt((arch.start_row-wizards[i].start_row)**2+(arch.start_col-wizards[i].start_col)**2)
                if(wizards[i].wiz_livestat==1 and dist<=mindist):
                    mindist=dist
                    arch.arch_target=i+len(cannons)+6        

        if(arch.arch_target<len(huts) and arch.arch_target>-1):
            dist=math.sqrt((arch.start_row-huts[arch.arch_target].start_row)**2+(arch.start_col-huts[arch.arch_target].start_col)**2)
            if(dist<=arch.arch_range):
                huts[arch.arch_target].hut_health-=arch.arch_damage
                if(huts[arch.arch_target].hut_health<=0):
                    huts[arch.arch_target].hut_livestat=0
                    arch.arch_target=-1
                continue

            if(arch.start_row>huts[arch.arch_target].start_row and arch.start_col<huts[arch.arch_target].start_col):
                if(flag[arch.start_row-1][arch.start_col+1]):
                    arch.start_row=arch.start_row-1
                    arch.start_col=arch.start_col+1
                else:
                    arch_wall_attack(arch,walls)
            if(arch.start_row<huts[arch.arch_target].start_row and arch.start_col<huts[arch.arch_target].start_col):
                if(flag[arch.start_row+1][arch.start_col+1]):
                    arch.start_row=arch.start_row+1
                    arch.start_col=arch.start_col+1
                else:
                    arch_wall_attack(arch,walls)
            if(arch.start_row<huts[arch.arch_target].start_row and arch.start_col>huts[arch.arch_target].start_col):
                if(flag[arch.start_row+1][arch.start_col-1]):
                    arch.start_row=arch.start_row+1
                    arch.start_col=arch.start_col-1
                else:
                    arch_wall_attack(arch,walls)
            if(arch.start_row>huts[arch.arch_target].start_row and arch.start_col>huts[arch.arch_target].start_col):
                if(flag[arch.start_row-1][arch.start_col-1]):
                    arch.start_row=arch.start_row-1
                    arch.start_col=arch.start_col-1
                else:
                    arch_wall_attack(arch,walls)
            if(arch.start_row==huts[arch.arch_target].start_row and arch.start_col<huts[arch.arch_target].start_col-1):
                if(flag[arch.start_row][arch.start_col+1]):
                    arch.start_col=arch.start_col+1
                else:
                    arch_wall_attack(arch,walls)
            if(arch.start_row==huts[arch.arch_target].start_row and arch.start_col>huts[arch.arch_target].start_col+1):
                if(flag[arch.start_row][arch.start_col-1]):
                    arch.start_col=arch.start_col-1
                else:
                    arch_wall_attack(arch,walls)
            if(arch.start_row<huts[arch.arch_target].start_row-1 and arch.start_col==huts[arch.arch_target].start_col):
                if(flag[arch.start_row+1][arch.start_col]):
                    arch.start_row=arch.start_row+1
                else:
                    arch_wall_attack(arch,walls)
            if(arch.start_row>huts[arch.arch_target].start_row+1 and arch.start_col==huts[arch.arch_target].start_col):
                if(flag[arch.start_row-1][arch.start_col]):
                    arch.start_row=arch.start_row-1
                else:
                    arch_wall_attack(arch,walls)      

        if(arch.arch_target==5): 
            mindist=100000
            for i in range(0, townhall.rows) :
                for j in range(0, townhall.cols) : 
                  dist=math.sqrt((i+townhall.start_row-arch.start_row)**2+(j+townhall.start_col-arch.start_col)**2) 
                  if(dist<=mindist):
                    mindist=dist
            if(mindist<=arch.arch_range):
                townhall.townhall_health-=arch.arch_damage
                if(townhall.townhall_health<=0):
                    townhall.townhall_livestat=0
                    arch.arch_target=-1
                continue
            if(arch.start_row<townhall.start_row and arch.start_row<townhall.end_row and arch.start_col>townhall.end_col):
                if(flag[arch.start_row+1][arch.start_col-1]==0):
                    arch_wall_attack(arch,walls) 
                else:    
                    arch.start_row=arch.start_row+1
                    arch.start_col=arch.start_col-1
            if(arch.start_row>townhall.start_row and arch.start_row>townhall.end_row and arch.start_col>townhall.end_col):
                if(flag[arch.start_row-1][arch.start_col-1]==0):
                    arch_wall_attack(arch,walls)
                else:
                    arch.start_row=arch.start_row-1
                    arch.start_col=arch.start_col-1
            if(arch.start_row>townhall.start_row and arch.start_row>townhall.end_row and arch.start_col<townhall.start_col):
                if(flag[arch.start_row-1][arch.start_col+1]==0):
                    arch_wall_attack(arch,walls)
                else:
                    arch.start_row=arch.start_row-1
                    arch.start_col=arch.start_col+1
            if(arch.start_row<townhall.start_row and arch.start_row<townhall.end_row and arch.start_col<townhall.start_col):
                if(flag[arch.start_row+1][arch.start_col+1]==0):
                    arch_wall_attack(arch,walls)
                else:
                    arch.start_row=arch.start_row+1
                    arch.start_col=arch.start_col+1
            if(arch.start_row>=townhall.start_row and arch.start_row<=townhall.end_row and arch.start_col<townhall.start_col-1):
                if(flag[arch.start_row][arch.start_col+1]==0):
                    arch_wall_attack(arch,walls)
                else:
                   arch.start_col=arch.start_col+1
            if(arch.start_row>=townhall.start_row and arch.start_row<=townhall.end_row and arch.start_col>townhall.end_col+1):
                if(flag[arch.start_row][arch.start_col-1]==0):
                    arch_wall_attack(arch,walls)
                else:
                   arch.start_col=arch.start_col-1
            if(arch.start_row<townhall.start_row-1 and arch.start_col>=townhall.start_col and arch.start_col<=townhall.end_col):
                if(flag[arch.start_row+1][arch.start_col]==0):
                    arch_wall_attack(arch,walls)
                else:
                    arch.start_row=arch.start_row+1
            if(arch.start_row>townhall.end_row+1 and arch.start_col>=townhall.start_col and arch.start_col<=townhall.end_col):
                if(flag[arch.start_row-1][arch.start_col]==0):
                    arch_wall_attack(arch,walls)
                else:
                   arch.start_row=arch.start_row-1

        if(arch.arch_target>5 and arch.arch_target<len(cannons)+6):
            dist=math.sqrt((arch.start_row-cannons[arch.arch_target-6].start_row)**2+(arch.start_col-cannons[arch.arch_target-6].start_col)**2)
            if(dist<=arch.arch_range):
                cannons[arch.arch_target-6].cannon_health-=arch.arch_damage
                if(cannons[arch.arch_target-6].cannon_health<=0):
                    cannons[arch.arch_target-6].cannon_livestat=0
                    arch.arch_target=-1
                continue
            if(arch.start_row>cannons[arch.arch_target-6].start_row and arch.start_col<cannons[arch.arch_target-6].start_col):
                if(flag[arch.start_row-1][arch.start_col+1]):
                    arch.start_row=arch.start_row-1
                    arch.start_col=arch.start_col+1
                else:
                    arch_wall_attack(arch,walls)
            if(arch.start_row<cannons[arch.arch_target-6].start_row and arch.start_col<cannons[arch.arch_target-6].start_col):
                if(flag[arch.start_row+1][arch.start_col+1]):
                    arch.start_row=arch.start_row+1
                    arch.start_col=arch.start_col+1
                else:
                    arch_wall_attack(arch,walls)
            if(arch.start_row<cannons[arch.arch_target-6].start_row and arch.start_col>cannons[arch.arch_target-6].start_col):
                if(flag[arch.start_row+1][arch.start_col-1]):
                    arch.start_row=arch.start_row+1
                    arch.start_col=arch.start_col-1
                else:
                    arch_wall_attack(arch,walls)
            if(arch.start_row>cannons[arch.arch_target-6].start_row and arch.start_col>cannons[arch.arch_target-6].start_col):
                if(flag[arch.start_row-1][arch.start_col-1]):
                    arch.start_row=arch.start_row-1
                    arch.start_col=arch.start_col-1
                else:
                    arch_wall_attack(arch,walls)
            if(arch.start_row==cannons[arch.arch_target-6].start_row and arch.start_col<cannons[arch.arch_target-6].start_col-1):
                if(flag[arch.start_row][arch.start_col+1]):
                    arch.start_col=arch.start_col+1
                else:
                    arch_wall_attack(arch,walls)
            if(arch.start_row==cannons[arch.arch_target-6].start_row and arch.start_col>cannons[arch.arch_target-6].start_col+1):
                if(flag[arch.start_row][arch.start_col-1]):
                    arch.start_col=arch.start_col-1
                else:
                    arch_wall_attack(arch,walls)
            if(arch.start_row<cannons[arch.arch_target-6].start_row-1 and arch.start_col==cannons[arch.arch_target-6].start_col):
                if(flag[arch.start_row+1][arch.start_col]):
                    arch.start_row=arch.start_row+1
                else:
                    arch_wall_attack(arch,walls)
            if(arch.start_row>cannons[arch.arch_target-6].start_row+1 and arch.start_col==cannons[arch.arch_target-6].start_col):
                if(flag[arch.start_row-1][arch.start_col]):
                    arch.start_row=arch.start_row-1
                else:
                    arch_wall_attack(arch,walls)   

        if(arch.arch_target>len(cannons)+5):
            dist=math.sqrt((arch.start_row-wizards[arch.arch_target-6-len(cannons)].start_row)**2+(arch.start_col-wizards[arch.arch_target-6-len(cannons)].start_col)**2)
            if(dist<=arch.arch_range):
                wizards[arch.arch_target-6-len(cannons)].wiz_health-=arch.arch_damage
                if(wizards[arch.arch_target-6-len(cannons)].wiz_health<=0):
                    wizards[arch.arch_target-6-len(cannons)].wiz_livestat=0
                    arch.arch_target=-1
                continue
            if(arch.start_row>wizards[arch.arch_target-6-len(cannons)].start_row and arch.start_col<wizards[arch.arch_target-6-len(cannons)].start_col):
                if(flag[arch.start_row-1][arch.start_col+1]):
                    arch.start_row=arch.start_row-1
                    arch.start_col=arch.start_col+1
                else:
                    arch_wall_attack(arch,walls)
            if(arch.start_row<wizards[arch.arch_target-6-len(cannons)].start_row and arch.start_col<wizards[arch.arch_target-6-len(cannons)].start_col):
                if(flag[arch.start_row+1][arch.start_col+1]):
                    arch.start_row=arch.start_row+1
                    arch.start_col=arch.start_col+1
                else:
                    arch_wall_attack(arch,walls)
            if(arch.start_row<wizards[arch.arch_target-6-len(cannons)].start_row and arch.start_col>wizards[arch.arch_target-6-len(cannons)].start_col):
                if(flag[arch.start_row+1][arch.start_col-1]):
                    arch.start_row=arch.start_row+1
                    arch.start_col=arch.start_col-1
                else:
                    arch_wall_attack(arch,walls)
            if(arch.start_row>wizards[arch.arch_target-6-len(cannons)].start_row and arch.start_col>wizards[arch.arch_target-6-len(cannons)].start_col):
                if(flag[arch.start_row-1][arch.start_col-1]):
                    arch.start_row=arch.start_row-1
                    arch.start_col=arch.start_col-1
                else:
                    arch_wall_attack(arch,walls)
            if(arch.start_row==wizards[arch.arch_target-6-len(cannons)].start_row and arch.start_col<wizards[arch.arch_target-6-len(cannons)].start_col-1):
                if(flag[arch.start_row][arch.start_col+1]):
                    arch.start_col=arch.start_col+1
                else:
                    arch_wall_attack(arch,walls)
            if(arch.start_row==wizards[arch.arch_target-6-len(cannons)].start_row and arch.start_col>wizards[arch.arch_target-6-len(cannons)].start_col+1):
                if(flag[arch.start_row][arch.start_col-1]):
                    arch.start_col=arch.start_col-1
                else:
                    arch_wall_attack(arch,walls)
            if(arch.start_row<wizards[arch.arch_target-6-len(cannons)].start_row-1 and arch.start_col==wizards[arch.arch_target-6-len(cannons)].start_col):
                if(flag[arch.start_row+1][arch.start_col]):
                    arch.start_row=arch.start_row+1
                else:
                    arch_wall_attack(arch,walls)
            if(arch.start_row>wizards[arch.arch_target-6-len(cannons)].start_row+1 and arch.start_col==wizards[arch.arch_target-6-len(cannons)].start_col):
                if(flag[arch.start_row-1][arch.start_col]):
                    arch.start_row=arch.start_row-1
                else:
                    arch_wall_attack(arch,walls)               
                    
        

                            
            