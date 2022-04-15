import random
from time import sleep,time
import math
from colorama import Fore, Back, Style 

def wiz_attack(king,barbarians,archers,balloons,wizards,num):
    if(wizards[num].wiz_target==0):
        king.king_health-=wizards[num].wiz_damage
        if(king.king_health<=0):
            king.king_livestat=0
            wizards[num].wiz_target=-1

        for barb in barbarians:
            if(barb.barb_livestat==1): 
                if(barb.start_row>=king.start_row-1 and barb.start_row<=king.start_row+1 and barb.start_col>=king.start_col-1 and barb.start_col<=king.start_col+1):
                    barb.barb_health-=king.king_damage
                    if(barb.barb_health<=0):
                        barb.barb_livestat=0  

        for arch in archers:
            if(arch.arch_livestat==1):
                if(arch.start_row>=king.start_row-1 and arch.start_row<=king.start_row+1 and arch.start_col>=king.start_col-1 and arch.start_col<=king.start_col+1):
                    arch.arch_health-=king.king_damage
                    if(arch.arch_health<=0):
                        arch.arch_livestat=0

        for ball in balloons:
            if(ball.ball_livestat==1):
                if(ball.start_row>=king.start_row-1 and ball.start_row<=king.start_row+1 and ball.start_col>=king.start_col-1 and ball.start_col<=king.start_col+1):
                    ball.ball_health-=king.king_damage
                    if(ball.ball_health<=0):
                        ball.ball_livestat=0                



    if(wizards[num].wiz_target>0 and wizards[num].wiz_target<=len(barbarians)):
        
        for i in range(0,len(barbarians)):
            if(barbarians[i].barb_livestat==1 and i!=wizards[num].wiz_target-1): 
                if(barbarians[i].start_row>=barbarians[wizards[num].wiz_target-1].start_row-1 and barbarians[i].start_row<=barbarians[wizards[num].wiz_target-1].start_row+1 and barbarians[i].start_col>=barbarians[wizards[num].wiz_target-1].start_col-1 and barbarians[i].start_col<=barbarians[wizards[num].wiz_target-1].start_col+1):
                    barbarians[i].barb_health-=barbarians[wizards[num].wiz_target-1].barb_damage
                    if(barbarians[i].barb_health<=0):
                        barbarians[i].barb_livestat=0  

        if(king.king_livestat==1 and king.king_status==1):
            if(king.start_row>=barbarians[wizards[num].wiz_target-1].start_row-1 and king.start_row<=barbarians[wizards[num].wiz_target-1].start_row+1 and king.start_col>=barbarians[wizards[num].wiz_target-1].start_col-1 and king.start_col<=barbarians[wizards[num].wiz_target-1].start_col+1):
                king.king_health-=barbarians[wizards[num].wiz_target-1].barb_damage
                if(king.king_health<=0):
                    king.king_livestat=0

        for arch in archers:
            if(arch.arch_livestat==1):
                if(arch.start_row>=barbarians[wizards[num].wiz_target-1].start_row-1 and arch.start_row<=barbarians[wizards[num].wiz_target-1].start_row+1 and arch.start_col>=barbarians[wizards[num].wiz_target-1].start_col-1 and arch.start_col<=barbarians[wizards[num].wiz_target-1].start_col+1):
                    arch.arch_health-=barbarians[wizards[num].wiz_target-1].barb_damage
                    if(arch.arch_health<=0):
                        arch.arch_livestat=0  

        for ball in balloons:
            if(ball.ball_livestat==1):
                if(ball.start_row>=barbarians[wizards[num].wiz_target-1].start_row-1 and ball.start_row<=barbarians[wizards[num].wiz_target-1].start_row+1 and ball.start_col>=barbarians[wizards[num].wiz_target-1].start_col-1 and ball.start_col<=barbarians[wizards[num].wiz_target-1].start_col+1):
                    ball.ball_health-=barbarians[wizards[num].wiz_target-1].barb_damage
                    if(ball.ball_health<=0):
                        ball.ball_livestat=0       

        barbarians[wizards[num].wiz_target-1].barb_health-=wizards[num].wiz_damage
        if(barbarians[wizards[num].wiz_target-1].barb_health<=0):
            barbarians[wizards[num].wiz_target-1].barb_livestat=0
            wizards[num].wiz_target=-1                           

    if(wizards[num].wiz_target>len(barbarians) and wizards[num].wiz_target<=len(barbarians)+len(archers)):
        
        for i in range(0,len(archers)):
            if(archers[i].arch_livestat==1 and i!=wizards[num].wiz_target-len(barbarians)-1): 
                if(archers[i].start_row>=archers[wizards[num].wiz_target-len(barbarians)-1].start_row-1 and archers[i].start_row<=archers[wizards[num].wiz_target-len(barbarians)-1].start_row+1 and archers[i].start_col>=archers[wizards[num].wiz_target-len(barbarians)-1].start_col-1 and archers[i].start_col<=archers[wizards[num].wiz_target-len(barbarians)-1].start_col+1):
                    archers[i].arch_health-=archers[wizards[num].wiz_target-len(barbarians)-1].arch_damage
                    if(archers[i].arch_health<=0):
                        archers[i].arch_livestat=0

        if(king.king_livestat==1 and king.king_status==1):
            if(king.start_row>=archers[wizards[num].wiz_target-len(barbarians)-1].start_row-1 and king.start_row<=archers[wizards[num].wiz_target-len(barbarians)-1].start_row+1 and king.start_col>=archers[wizards[num].wiz_target-len(barbarians)-1].start_col-1 and king.start_col<=archers[wizards[num].wiz_target-len(barbarians)-1].start_col+1):
                king.king_health-=archers[wizards[num].wiz_target-len(barbarians)-1].arch_damage
                if(king.king_health<=0):
                    king.king_livestat=0

        for barb in barbarians:
            if(barb.barb_livestat==1):
                if(barb.start_row>=archers[wizards[num].wiz_target-len(barbarians)-1].start_row-1 and barb.start_row<=archers[wizards[num].wiz_target-len(barbarians)-1].start_row+1 and barb.start_col>=archers[wizards[num].wiz_target-len(barbarians)-1].start_col-1 and barb.start_col<=archers[wizards[num].wiz_target-len(barbarians)-1].start_col+1):
                    barb.barb_health-=archers[wizards[num].wiz_target-len(barbarians)-1].arch_damage
                    if(barb.barb_health<=0):
                        barb.barb_livestat=0

        for ball in balloons:
            if(ball.ball_livestat==1):
                if(ball.start_row>=archers[wizards[num].wiz_target-len(barbarians)-1].start_row-1 and ball.start_row<=archers[wizards[num].wiz_target-len(barbarians)-1].start_row+1 and ball.start_col>=archers[wizards[num].wiz_target-len(barbarians)-1].start_col-1 and ball.start_col<=archers[wizards[num].wiz_target-len(barbarians)-1].start_col+1):
                    ball.ball_health-=archers[wizards[num].wiz_target-len(barbarians)-1].arch_damage
                    if(ball.ball_health<=0):
                        ball.ball_livestat=0

        archers[wizards[num].wiz_target-len(barbarians)-1].arch_health-=wizards[num].wiz_damage
        if(archers[wizards[num].wiz_target-len(barbarians)-1].arch_health<=0):
            archers[wizards[num].wiz_target-len(barbarians)-1].arch_livestat=0
            wizards[num].wiz_target=-1                

    if(wizards[num].wiz_target>len(barbarians)+len(archers) and wizards[num].wiz_target<=len(barbarians)+len(archers)+len(balloons)):
    
        for i in range(0,len(balloons)):
            if(balloons[i].ball_livestat==1 and i!=wizards[num].wiz_target-len(barbarians)-len(archers)-1): 
                if(balloons[i].start_row>=balloons[wizards[num].wiz_target-len(barbarians)-len(archers)-1].start_row-1 and balloons[i].start_row<=balloons[wizards[num].wiz_target-len(barbarians)-len(archers)-1].start_row+1 and balloons[i].start_col>=balloons[wizards[num].wiz_target-len(barbarians)-len(archers)-1].start_col-1 and balloons[i].start_col<=balloons[wizards[num].wiz_target-len(barbarians)-len(archers)-1].start_col+1):
                    balloons[i].ball_health-=balloons[wizards[num].wiz_target-len(barbarians)-len(archers)-1].ball_damage
                    if(balloons[i].ball_health<=0):
                        balloons[i].ball_livestat=0

        if(king.king_livestat==1):
            if(king.start_row>=balloons[wizards[num].wiz_target-len(barbarians)-len(archers)-1].start_row-1 and king.start_row<=balloons[wizards[num].wiz_target-len(barbarians)-len(archers)-1].start_row+1 and king.start_col>=balloons[wizards[num].wiz_target-len(barbarians)-len(archers)-1].start_col-1 and king.start_col<=balloons[wizards[num].wiz_target-len(barbarians)-len(archers)-1].start_col+1):
                king.king_health-=balloons[wizards[num].wiz_target-len(barbarians)-len(archers)-1].ball_damage
                if(king.king_health<=0):
                    king.king_livestat=0

        for barb in barbarians:
            if(barb.barb_livestat==1):
                if(barb.start_row>=balloons[wizards[num].wiz_target-len(barbarians)-len(archers)-1].start_row-1 and barb.start_row<=balloons[wizards[num].wiz_target-len(barbarians)-len(archers)-1].start_row+1 and barb.start_col>=balloons[wizards[num].wiz_target-len(barbarians)-len(archers)-1].start_col-1 and barb.start_col<=balloons[wizards[num].wiz_target-len(barbarians)-len(archers)-1].start_col+1):
                    barb.barb_health-=balloons[wizards[num].wiz_target-len(barbarians)-len(archers)-1].ball_damage
                    if(barb.barb_health<=0):
                        barb.barb_livestat=0

        for arch in archers:
            if(arch.arch_livestat==1):
                if(arch.start_row>=balloons[wizards[num].wiz_target-len(barbarians)-len(archers)-1].start_row-1 and arch.start_row<=balloons[wizards[num].wiz_target-len(barbarians)-len(archers)-1].start_row+1 and arch.start_col>=balloons[wizards[num].wiz_target-len(barbarians)-len(archers)-1].start_col-1 and arch.start_col<=balloons[wizards[num].wiz_target-len(barbarians)-len(archers)-1].start_col+1):
                    arch.arch_health-=balloons[wizards[num].wiz_target-len(barbarians)-len(archers)-1].ball_damage
                    if(arch.arch_health<=0):
                        arch.arch_livestat=0    

        balloons[wizards[num].wiz_target-len(barbarians)-len(archers)-1].ball_health-=wizards[num].wiz_damage
        if(balloons[wizards[num].wiz_target-len(barbarians)-len(archers)-1].ball_health<=0):
            balloons[wizards[num].wiz_target-len(barbarians)-len(archers)-1].ball_livestat=0
            wizards[num].wiz_target=-1                                        

                    
        