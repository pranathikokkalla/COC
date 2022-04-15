import random
from colorama import Fore, Back, Style 
from os import system
from time import sleep,time
import math
from src.input import *
from src.building import *
from src.king import *
from src.spawn import *
from src.barb import *
from src.archer import *
from src.attack import *
from src.balloon import *
from src.arch_move import *
from src.ball_move import *
from src.wiz_attack import *

class Village():

    def __init__(self):

        self.cols = 150
        self.rows = 50
        self.last_cols = 50
        self.last_rows = 25
        self.bg_pixel = Back.BLACK+' '+Style.RESET_ALL
        self.last_bg_pixel = Back.WHITE+' '+Style.RESET_ALL
        self.fg_pixel = Fore.WHITE+' '+Style.RESET_ALL
        self.title = "Clash Of Clans"
        self.game_over = "Game Over"
        self.king = King()
        self.barb = Barb()
        self.archer=Archer()
        self.balloon = Balloon()
        self.townhall= Townhall()
        self.huts = []
        self.cannons = []
        self.wizards = []
        self.barbarians = []
        self.archers = []
        self.balloons = []
        self.walls = []
        self.rage = 0
        self.rage_count=0        
        self.rage_start = 0
        self.heal_count=0         
        self.th_health = self.townhall.townhall_health
        self.c_health=0
        self.h_health=0
        self.w_health=0
        self.king_spawn_count=0     
        self.queen_spawn_count=0     
        self.final_text = ""
        self.start_time=time()
        self.barb_time=-0.5
        self.arch_time=-0.25
        self.queen_time=-1.5
        self.ball_time=-0.25
        self.health_bar = "Health Bar"
        self.health_bar_len=0
        self.prev_key = ' ' 
        self.eagle_key = ' '
        self.level=1
        self.queen_row=0
        self.queen_col=0
        self.eagle_bool=0

    def get_input(self):
        
        key = input_to()

        if(key ==  'b' and self.king_spawn_count == 0 and self.queen_spawn_count == 0):
          self.king = king_spawn()
          self.king_spawn_count=1

        if(key=='v' and self.queen_spawn_count == 0 and self.king_spawn_count == 0):
            self.king = king_spawn()
            self.king.bg_pixel = Back.BLUE+'Q'+Style.RESET_ALL
            self.king.king_damage=25
            self.queen_spawn_count=1  

        if(key == 'i'):
          self.barb = barb_spawn1()
          if(len(self.barbarians) < 6):
                self.barbarians.append(self.barb)

        if(key == 'j'):
            self.barb = barb_spawn2()
            if(len(self.barbarians) < 6):
                self.barbarians.append(self.barb)

        if(key == 'k'):
            self.barb = barb_spawn3()   
            if(len(self.barbarians) < 6):
                self.barbarians.append(self.barb)   

        if(key == 'x'):
            self.archer = archer_spawn1()
            if(len(self.archers) < 6):
                self.archers.append(self.archer)

        if(key == 'y'):
            self.archer = archer_spawn2()
            if(len(self.archers) < 6):
                self.archers.append(self.archer)

        if(key == 'z'):
            self.archer = archer_spawn3()
            if(len(self.archers) < 6):
                self.archers.append(self.archer) 

        if(key == 'e'):
            self.balloon = balloon_spawn1()  
            if(len(self.balloons) < 3):
                self.balloons.append(self.balloon)  

        if(key == 'f'):
            self.balloon = balloon_spawn2()  
            if(len(self.balloons) < 3):
                self.balloons.append(self.balloon)  

        if(key == 'g'):
            self.balloon = balloon_spawn3()  
            if(len(self.balloons) < 3):
                self.balloons.append(self.balloon)                   


        if((key == 'w' or key == 's' or key == 'a' or key == 'd') and self.king.king_livestat==1):
          self.prev_key=key  
          self.king = self.king.king_move(key,self.flag,self.king)

        if(key == ' ' and self.king.king_livestat==1 and self.king_spawn_count == 1):
          self.flag = king_attack(self.king,self.flag,self.walls,self.townhall,self.cannons,self.huts,self.wizards)

        if(key == ' ' and self.king.king_livestat==1 and self.queen_spawn_count == 1 and self.prev_key!=' '):  
          queen_attack(self.king,self.flag,self.walls,self.townhall,self.cannons,self.huts,self.wizards,self.prev_key)  

        if(key=='p' and self.king.king_livestat==1 and self.queen_spawn_count == 1):
          self.queen_time=time()
          self.eagle_key=self.prev_key
          self.queen_row=self.king.start_row
          self.queen_col=self.king.start_col
          self.eagle_bool=1

        if(time()-self.queen_time>=1 and self.eagle_bool==1 ):
            self.queen_time=time() 
            eagle_attack(self.king,self.flag,self.walls,self.townhall,self.cannons,self.huts,self.wizards,self.queen_row,self.queen_col,self.eagle_key) 
            self.eagle_bool=0
          
        if(key == 'h' and self.heal_count == 0):
           self.heal_count=1
           if(self.king.king_livestat==1):
                self.king.king_health= 3/2*self.king.king_health
           for barb in self.barbarians:
                if(barb.barb_livestat==1):
                    barb.barb_health= 3/2*barb.barb_health   
           for arch in self.archers:
                if(arch.arch_livestat==1):
                    arch.arch_health= 3/2*arch.arch_health
           for balloon in self.balloons:
                   if(balloon.ball_livestat==1):
                        balloon.ball_health= 3/2*balloon.ball_health         

        if(key == 'l' and self.king.king_livestat==1 and self.king_spawn_count == 1):
            self.leviathan_axe()              

        if(key == 'r' and self.rage_count == 0):  

           self.rage_count+=1
           self.rage=1
           self.bg_pixel = Back.CYAN+' '+Style.RESET_ALL
           
           if(self.king.king_livestat == 1):
             self.king.king_speed = 2
             self.king.king_damage = self.king.king_damage*2

           for barb in self.barbarians:
               if(barb.barb_livestat == 1):
                 barb.barb_damage = barb.barb_damage*2  

           for arch in self.archers:
                if(arch.arch_livestat == 1):
                    arch.arch_speed = 4
                    arch.arch_damage = arch.arch_damage*2

           for balloon in self.balloons:
               if(balloon.ball_livestat == 1):
                    balloon.ball_damage = balloon.ball_damage*2 

           self.rage_start = time()  

        if(self.rage == 1 and time()-self.rage_start > 5):
               self.rage=0
               self.bg_pixel = Back.BLACK+' '+Style.RESET_ALL
               if(self.king.king_livestat == 1):
                  self.king.king_speed = 1
                  self.king.king_damage = self.king.king_damage/2

               for barb in self.barbarians:
                    if(barb.barb_livestat == 1):
                      barb.barb_damage = barb.barb_damage/2 
               for arch in self.archers:
                    if(arch.arch_livestat == 1):
                      arch.arch_damage = arch.arch_damage/2  
               for balloon in self.balloons:
                    if(balloon.ball_livestat == 1):
                      balloon.ball_damage = balloon.ball_damage/2             

        return key

    def leviathan_axe(self):
        dist=0
        for wall in self.walls:
            dist = math.sqrt((wall.start_row-self.king.start_row)**2+(wall.start_col-self.king.start_col)**2)
            if(wall.live_stat == 1 and dist <= 5):
                wall.health-=self.king.king_damage
                if(wall.health <= 0):
                    wall.live_stat = 0
        for hut in self.huts:
            dist = math.sqrt((hut.start_row-self.king.start_row)**2+(hut.start_col-self.king.start_col)**2)
            if(hut.hut_livestat == 1 and dist <= 5):
                hut.hut_health-=self.king.king_damage
                if(hut.hut_health <= 0):
                    hut.hut_livestat = 0
        for cannon in self.cannons:
            dist = math.sqrt((cannon.start_row-self.king.start_row)**2+(cannon.start_col-self.king.start_col)**2)
            if(cannon.cannon_livestat == 1 and dist <= 5):
                cannon.cannon_health-=self.king.king_damage
                if(cannon.cannon_health <= 0):
                    cannon.cannon_livestat = 0
        if(self.townhall.townhall_livestat==1):            
            for i in range(0, self.townhall.rows) :
                for j in range(0, self.townhall.cols) : 
                  dist=math.sqrt((i+self.townhall.start_row-self.king.start_row)**2+(j+self.townhall.start_col-self.king.start_col)**2) 
                  if(dist<=5):
                    self.townhall.townhall_health-=self.king.king_damage
                    if(self.townhall.townhall_health <= 0):
                        self.townhall.townhall_livestat = 0
                    break    



    
    def hut_build(self):

        for i in range(0 , 5):
        
            hut = Hut()
            self.h_health=hut.hut_health
            if(i == 0):
                hut.start_row = 2
                hut.end_row=2
                hut.start_col = 0
                hut.end_col = 0

            elif(i == 1):
                hut.start_row = 2
                hut.end_row=2
                hut.start_col = 99
                hut.end_col = 99

            elif(i == 2):
                hut.start_row = 49
                hut.end_row=49
                hut.start_col = 0
                hut.end_col = 0
               
            elif(i == 3):
                hut.start_row = 49
                hut.end_row=49
                hut.start_col = 99
                hut.end_col = 99
                
            elif(i == 4):
                hut.start_row = 49
                hut.end_row=49
                hut.start_col = 50
                hut.end_col = 50

            self.huts.append(hut) 

    def cannon_build(self):

        for i in range(0 , 2):
            cannon = Cannon()
            self.c_health=cannon.cannon_health
            if(i == 0):
                cannon.start_row = 20
                cannon.end_row = 20
                cannon.start_col = 30
                cannon.end_col = 30
        
            elif(i == 1):
                cannon.start_row = 40
                cannon.end_row = 40
                cannon.start_col = 60
                cannon.end_col = 60

            self.cannons.append(cannon)   

    def cannon_build_levels(self):

        if(self.level==2):
            cannon = Cannon()
            cannon.start_row = 20
            cannon.end_row = 20
            cannon.start_col = 60
            cannon.end_col = 60
            self.cannons.append(cannon)  

        if(self.level==3):
            cannon = Cannon()
            cannon.start_row = 40
            cannon.end_row = 40
            cannon.start_col = 30
            cannon.end_col = 30
            self.cannons.append(cannon)
                 

    def wizard_build(self):

        for i in range(0 , 2):
            wizard = Wizard()
            self.w_health=wizard.wiz_health
            if(i == 0):
                wizard.start_row = 10
                wizard.start_col = 40
        
            elif(i == 1):
                wizard.start_row = 40
                wizard.start_col = 80

            self.wizards.append(wizard) 

    def wizard_build_levels(self):
            
            if(self.level==2):
                wizard = Wizard()
                wizard.start_row = 10
                wizard.start_col = 80
                self.wizards.append(wizard)  
    
            if(self.level==3):
                wizard = Wizard()
                wizard.start_row = 40
                wizard.start_col = 40
                self.wizards.append(wizard)                
    
    def wall_build(self):
        
       for i in range(0,5):
    
            self.wall= Wall()
            self.wall.start_row=self.townhall.start_row-1
            self.wall.end_row=self.wall.start_row
            self.wall.start_col=i+self.townhall.start_col-1
            self.wall.end_col=self.wall.start_col
            self.walls.append(self.wall)

       for i in range(0,5):
             
            self.wall= Wall()
            self.wall.start_row=self.townhall.end_row+1
            self.wall.end_row=self.wall.start_row
            self.wall.start_col=i+self.townhall.start_col-1
            self.wall.end_col=self.wall.start_col
            self.walls.append(self.wall)

       for i in range(0,4):

            self.wall= Wall()
            self.wall.start_row=self.townhall.start_row+i
            self.wall.end_row=self.wall.start_row
            self.wall.start_col=self.townhall.start_col-1
            self.wall.end_col=self.wall.start_col
            self.walls.append(self.wall)

       for i in range(0,4):

            self.wall= Wall()
            self.wall.start_row=self.townhall.start_row+i
            self.wall.end_row=self.wall.start_row
            self.wall.start_col=self.townhall.end_col+1
            self.wall.end_col=self.wall.start_col
            self.walls.append(self.wall)


    def cannon_attack(self,cannons,num):
        distance = 0
        dummy=0
        if(cannons[num].cannon_livestat==1):
            if(self.cannons[num].cannon_target==0):
                if(self.king.king_status==1):
                    distance=math.sqrt((cannons[num].start_row-self.king.start_row)**2+(cannons[num].start_col-self.king.start_col)**2)
                    if(distance<=cannons[num].cannon_range and self.king.king_livestat==1):
                        self.king.king_health=self.king.king_health-cannons[num].cannon_damage
                        cannons[num].bg_pixel = Back.RED+' '+Style.RESET_ALL
                        if(self.king.king_health<=0):  
                          self.king.king_livestat=0
                          self.cannons[num].cannon_target=-1
                    else:
                        self.cannons[num].cannon_target=-1           


            if(self.cannons[num].cannon_target>0 and self.cannons[num].cannon_target<=len(self.barbarians)):
                distance=math.sqrt((cannons[num].start_row-self.barbarians[self.cannons[num].cannon_target-1].start_row)**2+(cannons[num].start_col-self.barbarians[self.cannons[num].cannon_target-1].start_col)**2)
                if(distance<=cannons[num].cannon_range and self.barbarians[self.cannons[num].cannon_target-1].barb_livestat==1):
                    self.barbarians[self.cannons[num].cannon_target-1].barb_health=self.barbarians[self.cannons[num].cannon_target-1].barb_health-cannons[num].cannon_damage
                    cannons[num].bg_pixel= Back.RED+' '+Style.RESET_ALL
                    if(self.barbarians[self.cannons[num].cannon_target-1].barb_health<=0):
                        self.barbarians[self.cannons[num].cannon_target-1].barb_livestat=0
                        self.cannons[num].cannon_target=-1
                else:
                    self.cannons[num].cannon_target=-1      

            if(self.cannons[num].cannon_target>len(self.barbarians) and self.cannons[num].cannon_target<=len(self.barbarians)+len(self.archers)):
                distance=math.sqrt((cannons[num].start_row-self.archers[self.cannons[num].cannon_target-len(self.barbarians)-1].start_row)**2+(cannons[num].start_col-self.archers[self.cannons[num].cannon_target-len(self.barbarians)-1].start_col)**2)
                if(distance<=cannons[num].cannon_range and self.archers[self.cannons[num].cannon_target-len(self.barbarians)-1].arch_livestat==1):
                    self.archers[self.cannons[num].cannon_target-len(self.barbarians)-1].arch_health=self.archers[self.cannons[num].cannon_target-len(self.barbarians)-1].arch_health-cannons[num].cannon_damage
                    cannons[num].bg_pixel= Back.RED+' '+Style.RESET_ALL
                    if(self.archers[self.cannons[num].cannon_target-len(self.barbarians)-1].arch_health<=0):
                        self.archers[self.cannons[num].cannon_target-len(self.barbarians)-1].arch_livestat=0
                        self.cannons[num].cannon_target=-1
                else:
                    self.cannons[num].cannon_target=-1                   

            if(self.cannons[num].cannon_target==-1):
                if(self.king.king_livestat==1):
                  distance=math.sqrt((cannons[num].start_row-self.king.start_row)**2+(cannons[num].start_col-self.king.start_col)**2)
                  if(distance<=cannons[num].cannon_range):
                     self.king.king_health=self.king.king_health-cannons[num].cannon_damage
                     self.cannons[num].cannon_target=0
                     if(self.king.king_health<=0):
                         self.king.king_livestat=0
                         self.cannons[num].cannon_target=-1
                if(self.king.king_livestat==0 or distance>cannons[num].cannon_range):
                    for i in range(0,len(self.barbarians)):
                        if(self.barbarians[i].barb_livestat==1):
                            distance=math.sqrt((cannons[num].start_row-self.barbarians[i].start_row)**2+(cannons[num].start_col-self.barbarians[i].start_col)**2)
                            if(distance<=cannons[num].cannon_range):
                                self.barbarians[i].barb_health=self.barbarians[i].barb_health-cannons[num].cannon_damage
                                self.cannons[num].cannon_target=i+1
                                if(self.barbarians[i].barb_health<=0):
                                    self.barbarians[i].barb_livestat=0
                                    self.cannons[num].cannon_target=-1
                                break 
                        dummy=i     
                    if(dummy==len(self.barbarians)):
                        for i in range(0,len(self.archers)):
                            if(self.archers[i].arch_livestat==1):
                                distance=math.sqrt((cannons[num].start_row-self.archers[i].start_row)**2+(cannons[num].start_col-self.archers[i].start_col)**2)
                                if(distance<=cannons[num].cannon_range):
                                   self.archers[i].arch_health=self.archers[i].arch_health-cannons[num].cannon_damage
                                   self.cannons[num].cannon_target=i+1+len(self.barbarians)
                                   if(self.archers[i].arch_health<=0):
                                      self.archers[i].arch_livestat=0
                                      self.cannons[num].cannon_target=-1
                                   break 

                       

    def wizard_attack(self,num):
        distance = 0
        dummy1=0
        dummy2=0
        if(self.wizards[num].wiz_livestat==1):
            if(self.wizards[num].wiz_target==0):
                    distance=math.sqrt((self.wizards[num].start_row-self.king.start_row)**2+(self.wizards[num].start_col-self.king.start_col)**2)
                    if(distance<=self.wizards[num].wiz_range and self.king.king_livestat==1):
                        wiz_attack(self.king,self.barbarians,self.archers,self.balloons,self.wizards,num)
                    else:
                        self.wizards[num].wiz_target=-1

            if(self.wizards[num].wiz_target>0 and self.wizards[num].wiz_target<=len(self.barbarians)):
                distance=math.sqrt((self.wizards[num].start_row-self.barbarians[self.wizards[num].wiz_target-1].start_row)**2+(self.wizards[num].start_col-self.barbarians[self.wizards[num].wiz_target-1].start_col)**2)
                if(distance<=self.wizards[num].wiz_range and self.barbarians[self.wizards[num].wiz_target-1].barb_livestat==1):
                    wiz_attack(self.king,self.barbarians,self.archers,self.balloons,self.wizards,num)
                else:
                    self.wizards[num].wiz_target=-1 
            if(self.wizards[num].wiz_target>len(self.barbarians) and self.wizards[num].wiz_target<=len(self.barbarians)+len(self.archers)):
                distance=math.sqrt((self.wizards[num].start_row-self.archers[self.wizards[num].wiz_target-len(self.barbarians)-1].start_row)**2+(self.wizards[num].start_col-self.archers[self.wizards[num].wiz_target-len(self.barbarians)-1].start_col)**2)
                if(distance<=self.wizards[num].wiz_range and self.archers[self.wizards[num].wiz_target-len(self.barbarians)-1].arch_livestat==1):
                    wiz_attack(self.king,self.barbarians,self.archers,self.balloons,self.wizards,num)
                else:
                    self.wizards[num].wiz_target=-1  
            if(self.wizards[num].wiz_target>len(self.barbarians)+len(self.archers) and self.wizards[num].wiz_target<=len(self.barbarians)+len(self.archers)+len(self.balloons)):
                distance=math.sqrt((self.wizards[num].start_row-self.balloons[self.wizards[num].wiz_target-len(self.barbarians)-len(self.archers)-1].start_row)**2+(self.wizards[num].start_col-self.balloons[self.wizards[num].wiz_target-len(self.barbarians)-len(self.archers)-1].start_col)**2)
                if(distance<=self.wizards[num].wiz_range and self.balloons[self.wizards[num].wiz_target-len(self.barbarians)-len(self.archers)-1].ball_livestat==1):
                    wiz_attack(self.king,self.barbarians,self.archers,self.balloons,self.wizards,num)
                else:
                    self.wizards[num].wiz_target=-1       

            if(self.wizards[num].wiz_target==-1):
                if(self.king.king_livestat==1 and (self.king_spawn_count==1 or self.queen_spawn_count==1)):
                  distance=math.sqrt((self.wizards[num].start_row-self.king.start_row)**2+(self.wizards[num].start_col-self.king.start_col)**2)
                  if(distance<=self.wizards[num].wiz_range):
                     self.wizards[num].wiz_target=0
                     wiz_attack(self.king,self.barbarians,self.archers,self.balloons,self.wizards,num)

                if(self.king.king_livestat==0 or distance>self.wizards[num].wiz_range or (self.king_spawn_count==0 and self.queen_spawn_count==0)):
                    for i in range(0,len(self.barbarians)):
                        if(self.barbarians[i].barb_livestat==1):
                            distance=math.sqrt((self.wizards[num].start_row-self.barbarians[i].start_row)**2+(self.wizards[num].start_col-self.barbarians[i].start_col)**2)
                            if(distance<=self.wizards[num].wiz_range):
                                self.wizards[num].wiz_target=i+1
                                wiz_attack(self.king,self.barbarians,self.archers,self.balloons,self.wizards,num)
                                break  
                        dummy1=i    
                    if(dummy1==len(self.barbarians)):
                        for i in range(0,len(self.archers)):
                            if(self.archers[i].arch_livestat==1):
                                distance=math.sqrt((self.wizards[num].start_row-self.archers[i].start_row)**2+(self.wizards[num].start_col-self.archers[i].start_col)**2)
                                if(distance<=self.wizards[num].wiz_range):
                                    self.wizards[num].wiz_target=i+1+len(self.barbarians)
                                    wiz_attack(self.king,self.barbarians,self.archers,self.balloons,self.wizards,num)
                                    break   
                            dummy2=i       
                    if(dummy2==len(self.archers)):
                        for i in range(0,len(self.balloons)):
                            if(self.balloons[i].ball_livestat==1):
                                distance=math.sqrt((self.wizards[num].start_row-self.balloons[i].start_row)**2+(self.wizards[num].start_col-self.balloons[i].start_col)**2)
                                if(distance<=self.wizards[num].wiz_range):
                                    self.wizards[num].wiz_target=i+1+len(self.barbarians)+len(self.archers)
                                    wiz_attack(self.king,self.barbarians,self.archers,self.balloons,self.wizards,num)
                                    break                 

    def level_up(self,king,barbarians,archers,balloons,cannons,townhall,huts,wizards,walls):

        #king reset
        self.king_spawn_count=0 
        self.queen_spawn_count=0
        king.start_row=3
        king.end_row = 3
        king.start_col = 49
        king.end_col = 49
        king.king_status = 0
        king.king_damage = 30
        king.king_health = 120.0
        king.king_speed = 1
        king.king_livestat = 1

        #barb reset
        barbarians.clear()

        #archer reset
        archers.clear()

        #balloon reset
        balloons.clear()

        #cannon reset
        for i in range(0,len(cannons)):
            cannons[i].cannon_health = 100
            cannons[i].cannon_livestat=1
            cannons[i].cannon_target=-1
            cannons[i].bg_pixel = Back.GREEN+'C'+Style.RESET_ALL

        self.cannon_build_levels()

        #townhall reset
        townhall.townhall_health = 150
        townhall.townhall_livestat=1
        townhall.bg_pixel = Back.GREEN+' '+Style.RESET_ALL

        #huts reset
        for i in range(0,len(huts)):
            huts[i].hut_health = 50
            huts[i].hut_livestat=1
            huts[i].bg_pixel = Back.GREEN+' '+Style.RESET_ALL

        #wizards reset
        for i in range(0,len(wizards)):
            wizards[i].wiz_health = 100
            wizards[i].wiz_livestat=1
            wizards[i].wiz_target=-1
            wizards[i].bg_pixel = Back.GREEN+'W'+Style.RESET_ALL  

        self.wizard_build_levels()     

        #walls reset
        for i in range(0,len(walls)):
           walls[i].health = 35
           walls[i].live_stat = 1        

        #variables reset
        self.rage_count=0 
        self.heal_count=0
        self.prev_key = ' '



        
    def render(self,file):

        system('clear')
        for tower in self.wizards:
            print(tower.wiz_health)

        count1=0
        count2=0
        count3=0
        count4=0
        count5=0
        count6=0

        self.village = [[self.bg_pixel for i in range(self.cols)] for j in range(self.rows)]
        self.flag = [[1 for i in range(self.cols)] for j in range(self.rows)]

        if(self.townhall.townhall_health <= self.th_health/2 and self.townhall.townhall_health>self.th_health/5):
            self.townhall.bg_pixel = Back.YELLOW+' '+Style.RESET_ALL
        if(self.townhall.townhall_health <= self.th_health/5 and self.townhall.townhall_health>0):
            self.townhall.bg_pixel = Back.RED+' '+Style.RESET_ALL

        for hut in self.huts:
            if(hut.hut_health <= self.h_health/2 and hut.hut_health>self.h_health/5):
                hut.bg_pixel = Back.YELLOW+' '+Style.RESET_ALL
            if(hut.hut_health <= self.h_health/5 and self.h_health>0):
                hut.bg_pixel = Back.RED+' '+Style.RESET_ALL

        for cannon in self.cannons:
            if(cannon.cannon_health <= self.c_health/2 and cannon.cannon_health>self.c_health/5):
                cannon.bg_pixel = Back.YELLOW+'C'+Style.RESET_ALL
            if(cannon.cannon_health <= self.c_health/5 and self.c_health>0):
                cannon.bg_pixel = Back.RED+'C'+Style.RESET_ALL    

        for wiz in self.wizards:
            if(wiz.wiz_health <= self.w_health/2 and wiz.wiz_health>self.w_health/5):
                wiz.bg_pixel = Back.YELLOW+'W'+Style.RESET_ALL
            if(wiz.wiz_health <= self.w_health/5 and self.w_health>0):
                wiz.bg_pixel = Back.RED+'W'+Style.RESET_ALL                   

        title_offset = (100-len(self.title)) // 2
        for j in range(0, len(self.title)):
            self.village[1][title_offset+j] = Back.WHITE+Fore.BLUE+self.title[j]+Style.RESET_ALL
            self.flag[1][title_offset+j] = 0

        if(self.townhall.townhall_livestat==1):
            for i in range(0, self.townhall.rows) :
               for j in range(0, self.townhall.cols) :
                  self.village[i+self.townhall.start_row][j+self.townhall.start_col] = self.townhall.bg_pixel 
                  self.flag[i+self.townhall.start_row][j+self.townhall.start_col] = 0

        for hut in self.huts:
            if(hut.hut_livestat==1):
                for i in range(0, hut.rows) :
                   for j in range(0, hut.cols) :
                      self.village[i+hut.start_row][j+hut.start_col] = hut.bg_pixel 
                      self.flag[i+hut.start_row][j+hut.start_col] = 0

        for cannon in self.cannons:
            if(cannon.cannon_livestat==1):
                for i in range(0, cannon.rows) :
                    for j in range(0, cannon.cols) :
                      self.village[i+cannon.start_row][j+cannon.start_col] = cannon.bg_pixel 
                      self.flag[i+cannon.start_row][j+cannon.start_col] = 0    

        for wiz in self.wizards:
            if(wiz.wiz_livestat==1):
                self.village[wiz.start_row][wiz.start_col] = wiz.bg_pixel 
                self.flag[wiz.start_row][wiz.start_col] = 0              

        if(self.king.king_status == 1):
            self.village[self.king.start_row][self.king.start_col] = self.king.bg_pixel 
    

        # barbarians spawn       
        for i in range(0, len(self.barbarians)):
            if(self.barbarians[i].barb_livestat==1):
               self.village[self.barbarians[i].start_row][self.barbarians[i].start_col] = self.barbarians[i].bg_pixel 

        # archers spawn
        for i in range(0, len(self.archers)):
            if(self.archers[i].arch_livestat==1):
                   self.village[self.archers[i].start_row][self.archers[i].start_col] = self.archers[i].bg_pixel                    

        #wall
        for wall in self.walls:
            if(wall.live_stat == 1):
               self.village[wall.start_row][wall.start_col] = wall.bg_pixel
               self.flag[wall.start_row][wall.start_col] = 0


        #balloons spawn
        for i in range(0, len(self.balloons)):
            if(self.balloons[i].ball_livestat==1):
                   self.village[self.balloons[i].start_row][self.balloons[i].start_col] = self.balloons[i].bg_pixel        
        
        #cannon attack
        for i in range(0, len(self.cannons)):
            if(time()-self.cannons[i].cannon_time>=1):
                self.cannon_attack(self.cannons,i)    
                self.cannons[i].cannon_time=time()  
                if(self.cannons[i].cannon_target>-1):
                    self.cannons[i].bg_pixel = Back.RED+' '+Style.RESET_ALL
                else:
                    self.cannons[i].bg_pixel = Back.GREEN+' '+Style.RESET_ALL   


        #wizard attack
        for i in range(0, len(self.wizards)):
            if(time()-self.wizards[i].wiz_time>=1):
                self.wizard_attack(i)
                self.wizards[i].wiz_time=time()

        #Side Board    
        for i in range(0, self.rows):
            for j in range(100,150):
                self.village[i][j] = Back.BLUE+' '+Style.RESET_ALL
                self.flag[i][j] = 0

        for i in range(0,len(self.health_bar)):
            self.village[10][120+i] = Back.WHITE+Fore.BLACK+self.health_bar[i]+Style.RESET_ALL
        self.health_bar_len = math.floor(1/12*self.king.king_health) 
        if(self.king.king_status==1):
          for i in range(0, self.health_bar_len):
            self.village[12][120+i] = Back.RED+' '+Style.RESET_ALL 

        #barbarian attack
        if(time()-self.barb_time>=0.5 and self.rage==1):
           barb_attack(self.barbarians,self.townhall,self.walls,self.huts,self.cannons,self.wizards,self.flag)  
           self.barb_time=time()  
        if(time()-self.barb_time>=1 and self.rage==0):
            barb_attack(self.barbarians,self.townhall,self.walls,self.huts,self.cannons,self.wizards,self.flag)  
            self.barb_time=time()  
 

        #archer movement
        if(time()-self.arch_time>=0.25 and self.rage==1):
            arch_movement(self.archers,self.townhall,self.walls,self.huts,self.cannons,self.wizards,self.flag)  
            self.arch_time=time()
        if(time()-self.arch_time>=0.5 and self.rage==0):    
            arch_movement(self.archers,self.townhall,self.walls,self.huts,self.cannons,self.wizards,self.flag)  
            self.arch_time=time()

        #balloon movement
        if(time()-self.ball_time>=0.25 and self.rage==1):
            ball_movement(self.balloons,self.townhall,self.walls,self.huts,self.cannons,self.wizards,self.flag)  
            self.ball_time=time()
        if(time()-self.ball_time>=0.5 and self.rage==0):
            ball_movement(self.balloons,self.townhall,self.walls,self.huts,self.cannons,self.wizards,self.flag)  
            self.ball_time=time()            

        #Game over
        if(self.townhall.townhall_livestat==0):
            for cannon in self.cannons:
                if(cannon.cannon_livestat == 0):
                    count1+=1
            for hut in self.huts:
                if(hut.hut_livestat == 0):
                    count2+=1   
            for wiz in self.wizards:
                if(wiz.wiz_livestat == 0):
                    count3+=1        
            if(count1==len(self.cannons) and count2==len(self.huts) and count3==len(self.wizards)):
                if(self.level==1):
                    self.level=2
                    self.level_up(self.king,self.barbarians,self.archers,self.balloons,self.cannons,self.townhall,self.huts,self.wizards,self.walls)
            if(self.level==2 and count1==len(self.cannons) and count2==len(self.huts) and count3==len(self.wizards)):
                    self.level=3
                    self.level_up(self.king,self.barbarians,self.archers,self.balloons,self.cannons,self.townhall,self.huts,self.wizards,self.walls)
            if(self.level==3 and count1==len(self.cannons) and count2==len(self.huts) and count3==len(self.wizards)):    
                   self.game_over="VICTORY" 
                   for i in range(17,42):
                       for j in range(25,75):
                           self.village[i][j] = Back.WHITE+' '+Style.RESET_ALL
                   for i in range(0,len(self.game_over)):
                       self.village[20][45+i] = Back.WHITE+Fore.BLACK+self.game_over[i]+Style.RESET_ALL
                   self.final_text="Time Taken : "+str(math.floor(time()-self.start_time))+" seconds"    
                   for i in range(0,len(self.final_text)):
                       self.village[30][37+i] = Back.WHITE+Fore.BLACK+self.final_text[i]+Style.RESET_ALL

                   print("\n".join(["".join(row) for row in self.village]))    
                   return 1

        if(count1!=len(self.cannons) or count2!=len(self.huts) or count3!=len(self.wizards) or self.townhall.townhall_livestat==1):
            for barb in self.barbarians:
                if(barb.barb_livestat==0):
                    count4+=1
            for arch in self.archers:
                if(arch.arch_livestat==0):
                    count5+=1
            for ball in self.balloons:
                if(ball.ball_livestat==0):
                    count6+=1                
            if(count4==len(self.barbarians) and count5==len(self.archers) and count6==len(self.balloons) and self.king.king_livestat == 0):
                self.game_over="DEFEAT"
                for i in range(17,42):
                       for j in range(25,75):
                           self.village[i][j] = Back.WHITE+' '+Style.RESET_ALL
                for i in range(0,len(self.game_over)):
                       self.village[20][45+i] = Back.WHITE+Fore.BLACK+self.game_over[i]+Style.RESET_ALL
                self.final_text="Time Taken : "+str(math.floor(time()-self.start_time))+" seconds" 
                for i in range(0,len(self.final_text)):
                       self.village[30][37+i] = Back.WHITE+Fore.BLACK+self.final_text[i]+Style.RESET_ALL
                print("\n".join(["".join(row) for row in self.village]))
                return 1               
                                     
        print("\n".join(["".join(row) for row in self.village]))
        file_name=open(file,"a")
        file_name.write("\n".join(["".join(row) for row in self.village]))
        file_name.write("\n")
        file_name.close()

        return 0


