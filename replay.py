import os
import sys


num=input("Enter the game number you want to view: ")
file="./replay/game"+num+".txt"

def Replay(file):
    with open(file,'r') as f:
        array=[]
        rows=0
        for line in f.readlines():
            array.append(line)
            rows = rows+1
            if(rows%50==0):
                os.system('clear')
                print(''.join(array))
                os.system('sleep 0.2')
                array=[]

Replay(file)                
