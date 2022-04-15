from src.village import *
import os.path

village = Village()
village.hut_build()
village.cannon_build()
village.wall_build()
village.wizard_build()

val=1
if not os.path.exists('./replay'):
    os.makedirs('./replay')
    
file="./replay/game"
while(True):
    if(os.path.exists(file+str(val)+".txt")):
        val+=1
    else:
        break
num=str(val)
file=file+num+".txt"    


while(True):
    key = village.get_input()
    if(key == 'q'):
        break
    else:
      val=village.render(file)
      if(val==1):
          break
     