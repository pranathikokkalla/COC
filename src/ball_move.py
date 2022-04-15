import random
from time import sleep,time
import math
from colorama import Fore, Back, Style 

def ball_movement(balloons,townhall,walls,huts,cannons,wizards,flag):
    for ball in balloons:
        if(ball.ball_livestat==0):
            continue

        if(ball.ball_target<len(cannons) and ball.ball_target>-1):
               if(cannons[ball.ball_target].cannon_livestat==0):
                ball.ball_target=-1
        if(ball.ball_target>=len(cannons) and ball.ball_target<len(cannons)+len(wizards)):
                if(wizards[ball.ball_target-len(cannons)].wiz_livestat==0):
                     ball.ball_target=-1        
        if(ball.ball_target>=len(cannons)+len(wizards) and ball.ball_target<len(cannons)+len(wizards)+5):
            if(huts[ball.ball_target-len(cannons)-len(wizards)].hut_livestat==0):
                ball.ball_target=-1
        if(ball.ball_target==len(cannons)+len(wizards)+5):
            if(townhall.townhall_livestat==0):
                ball.ball_target=-1

        if(ball.ball_target==-1):
            mindist=100000
            dist = 0
            for i in range(0,len(cannons)):
                dist=math.sqrt((ball.start_row-cannons[i].start_row)**2+(ball.start_col-cannons[i].start_col)**2)
                if(cannons[i].cannon_livestat==1 and dist<=mindist):
                   mindist=dist
                   ball.ball_target=i
            for i in range(0,len(wizards)):
                dist=math.sqrt((ball.start_row-wizards[i].start_row)**2+(ball.start_col-wizards[i].start_col)**2)
                if(wizards[i].wiz_livestat==1 and dist<=mindist):
                    mindist=dist
                    ball.ball_target=i+len(cannons)       
            if(ball.ball_target==-1):
                for i in range(0,len(huts)):
                    dist=math.sqrt((ball.start_row-huts[i].start_row)**2+(ball.start_col-huts[i].start_col)**2)
                    if(huts[i].hut_livestat==1 and dist<=mindist):
                       mindist=dist
                       ball.ball_target=i+len(cannons)+len(wizards)
                if(townhall.townhall_livestat==1):            
                    for i in range(0, townhall.rows) :
                        for j in range(0, townhall.cols) : 
                            dist=math.sqrt((i+townhall.start_row-ball.start_row)**2+(j+townhall.start_col-ball.start_col)**2) 
                            if(dist<=mindist):
                               mindist=dist
                               ball.ball_target=len(cannons)+len(wizards)+5
                               break  

        if(ball.ball_target<len(cannons) and ball.ball_target>-1):
            dist=math.sqrt((ball.start_row-cannons[ball.ball_target].start_row)**2+(ball.start_col-cannons[ball.ball_target].start_col)**2)
            if(dist<=0):
                cannons[ball.ball_target].cannon_health-=ball.ball_damage
                if(cannons[ball.ball_target].cannon_health<=0):
                    cannons[ball.ball_target].cannon_livestat=0
                    ball.ball_target=-1
                continue 

            if(ball.start_row>cannons[ball.ball_target].start_row and ball.start_col<cannons[ball.ball_target].start_col):
                    ball.start_row=ball.start_row-1
                    ball.start_col=ball.start_col+1
            if(ball.start_row<cannons[ball.ball_target].start_row and ball.start_col<cannons[ball.ball_target].start_col):
                    ball.start_row=ball.start_row+1
                    ball.start_col=ball.start_col+1
            if(ball.start_row<cannons[ball.ball_target].start_row and ball.start_col>cannons[ball.ball_target].start_col):
                    ball.start_row=ball.start_row+1
                    ball.start_col=ball.start_col-1
            if(ball.start_row>cannons[ball.ball_target].start_row and ball.start_col>cannons[ball.ball_target].start_col):
                    ball.start_row=ball.start_row-1
                    ball.start_col=ball.start_col-1
            if(ball.start_row==cannons[ball.ball_target].start_row and ball.start_col<cannons[ball.ball_target].start_col):
                    ball.start_col=ball.start_col+1
            if(ball.start_row==cannons[ball.ball_target].start_row and ball.start_col>cannons[ball.ball_target].start_col):
                    ball.start_col=ball.start_col-1
            if(ball.start_row<cannons[ball.ball_target].start_row and ball.start_col==cannons[ball.ball_target].start_col):
                    ball.start_row=ball.start_row+1
            if(ball.start_row>cannons[ball.ball_target].start_row and ball.start_col==cannons[ball.ball_target].start_col):
                    ball.start_row=ball.start_row-1

        if(ball.ball_target>=len(cannons) and ball.ball_target<len(cannons)+len(wizards)):
            dist=math.sqrt((ball.start_row-wizards[ball.ball_target-len(cannons)].start_row)**2+(ball.start_col-wizards[ball.ball_target-len(cannons)].start_col)**2)
            if(dist<=0):
                wizards[ball.ball_target-len(cannons)].wiz_health-=ball.ball_damage
                if(wizards[ball.ball_target-len(cannons)].wiz_health<=0):
                    wizards[ball.ball_target-len(cannons)].wiz_livestat=0
                    ball.ball_target=-1
                continue 

            if(ball.start_row>wizards[ball.ball_target-len(cannons)].start_row and ball.start_col<wizards[ball.ball_target-len(cannons)].start_col):
                    ball.start_row=ball.start_row-1
                    ball.start_col=ball.start_col+1
            if(ball.start_row<wizards[ball.ball_target-len(cannons)].start_row and ball.start_col<wizards[ball.ball_target-len(cannons)].start_col):
                    ball.start_row=ball.start_row+1
                    ball.start_col=ball.start_col+1
            if(ball.start_row<wizards[ball.ball_target-len(cannons)].start_row and ball.start_col>wizards[ball.ball_target-len(cannons)].start_col):
                    ball.start_row=ball.start_row+1
                    ball.start_col=ball.start_col-1
            if(ball.start_row>wizards[ball.ball_target-len(cannons)].start_row and ball.start_col>wizards[ball.ball_target-len(cannons)].start_col):
                    ball.start_row=ball.start_row-1
                    ball.start_col=ball.start_col-1
            if(ball.start_row==wizards[ball.ball_target-len(cannons)].start_row and ball.start_col<wizards[ball.ball_target-len(cannons)].start_col):
                    ball.start_col=ball.start_col+1
            if(ball.start_row==wizards[ball.ball_target-len(cannons)].start_row and ball.start_col>wizards[ball.ball_target-len(cannons)].start_col):
                    ball.start_col=ball.start_col-1
            if(ball.start_row<wizards[ball.ball_target-len(cannons)].start_row and ball.start_col==wizards[ball.ball_target-len(cannons)].start_col):
                    ball.start_row=ball.start_row+1
            if(ball.start_row>wizards[ball.ball_target-len(cannons)].start_row and ball.start_col==wizards[ball.ball_target-len(cannons)].start_col):
                    ball.start_row=ball.start_row-1            
        
        if(ball.ball_target>=len(cannons)+len(wizards) and ball.ball_target<len(cannons)+len(wizards)+5):
            dist=math.sqrt((ball.start_row-huts[ball.ball_target-len(cannons)-len(wizards)].start_row)**2+(ball.start_col-huts[ball.ball_target-len(cannons)-len(wizards)].start_col)**2)
            if(dist<=0):
                huts[ball.ball_target-len(cannons)-len(wizards)].hut_health-=ball.ball_damage
                if(huts[ball.ball_target-len(cannons)-len(wizards)].hut_health<=0):
                    huts[ball.ball_target-len(cannons)-len(wizards)].hut_livestat=0
                    ball.ball_target=-1
                continue

            if(ball.start_row>huts[ball.ball_target-len(cannons)-len(wizards)].start_row and ball.start_col<huts[ball.ball_target-len(cannons)-len(wizards)].start_col):
                    ball.start_row=ball.start_row-1
                    ball.start_col=ball.start_col+1
            if(ball.start_row<huts[ball.ball_target-len(cannons)-len(wizards)].start_row and ball.start_col<huts[ball.ball_target-len(cannons)-len(wizards)].start_col):
                    ball.start_row=ball.start_row+1
                    ball.start_col=ball.start_col+1
            if(ball.start_row<huts[ball.ball_target-len(cannons)-len(wizards)].start_row and ball.start_col>huts[ball.ball_target-len(cannons)-len(wizards)].start_col):
                    ball.start_row=ball.start_row+1
                    ball.start_col=ball.start_col-1
            if(ball.start_row>huts[ball.ball_target-len(cannons)-len(wizards)].start_row+1 and ball.start_col>huts[ball.ball_target-len(cannons)-len(wizards)].start_col):
                    ball.start_row=ball.start_row-1
                    ball.start_col=ball.start_col-1
            if(ball.start_row==huts[ball.ball_target-len(cannons)-len(wizards)].start_row and ball.start_col<huts[ball.ball_target-len(cannons)-len(wizards)].start_col):
                    ball.start_col=ball.start_col+1
            if(ball.start_row==huts[ball.ball_target-len(cannons)-len(wizards)].start_row and ball.start_col>huts[ball.ball_target-len(cannons)-len(wizards)].start_col):
                    ball.start_col=ball.start_col-1
            if(ball.start_row<huts[ball.ball_target-len(cannons)-len(wizards)].start_row and ball.start_col==huts[ball.ball_target-len(cannons)-len(wizards)].start_col):
                    ball.start_row=ball.start_row+1
            if(ball.start_row>huts[ball.ball_target-len(cannons)-len(wizards)].start_row and ball.start_col==huts[ball.ball_target-len(cannons)-len(wizards)].start_col):
                    ball.start_row=ball.start_row-1

        if(ball.ball_target==len(cannons)+len(wizards)+5): 
            mindist=100000
            for i in range(0, townhall.rows) :
                for j in range(0, townhall.cols) : 
                  dist=math.sqrt((i+townhall.start_row-ball.start_row)**2+(j+townhall.start_col-ball.start_col)**2) 
                  if(dist<=mindist):
                    mindist=dist
            if(mindist<=0):
                townhall.townhall_health-=ball.ball_damage
                if(townhall.townhall_health<=0):
                    townhall.townhall_livestat=0
                    ball.ball_target=-1
                continue
            if(ball.start_row<townhall.start_row and ball.start_row<townhall.end_row and ball.start_col>townhall.end_col):
                ball.start_row=ball.start_row+1
                ball.start_col=ball.start_col-1
            if(ball.start_row>townhall.start_row and ball.start_row>townhall.end_row and ball.start_col>townhall.end_col):
                ball.start_row=ball.start_row-1
                ball.start_col=ball.start_col-1
            if(ball.start_row>townhall.start_row and ball.start_row>townhall.end_row and ball.start_col<townhall.start_col):
                ball.start_row=ball.start_row-1
                ball.start_col=ball.start_col+1
            if(ball.start_row<townhall.start_row and ball.start_row<townhall.end_row and ball.start_col<townhall.start_col):
                ball.start_row=ball.start_row+1
                ball.start_col=ball.start_col+1
            if(ball.start_row>=townhall.start_row and ball.start_row<=townhall.end_row and ball.start_col<townhall.start_col):
                ball.start_col=ball.start_col+1
            if(ball.start_row>=townhall.start_row and ball.start_row<=townhall.end_row and ball.start_col>townhall.end_col):
                ball.start_col=ball.start_col-1
            if(ball.start_row<townhall.start_row and ball.start_col>=townhall.start_col and ball.start_col<=townhall.end_col):
                ball.start_row=ball.start_row+1
            if(ball.start_row>townhall.end_row and ball.start_col>=townhall.start_col and ball.start_col<=townhall.end_col):
                ball.start_row=ball.start_row-1            
 

























