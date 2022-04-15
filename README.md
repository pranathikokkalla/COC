This game is a mini version of Clash of Clans.

To start the game we have to run the game.py file. All the necessary files are inside the src folder. village.py file contains a class village which has all the important functions and properties.

In game.py we run an infinite loop which calls render() function every time unless the game ends.

I used all the OOPS concepts like inheritance,encapsulation,abstraction and polymorphism in this assignment.

I took a 2D array called village which displays the village base using ASCII characters and gave colors accordingly using colorama.

The dimensions of king, barbarians, huts, walls and cannons are 1 X 1. 

King is spawned on pressing the button 'b' and barbarians are spawned at 3 places on pressing the buttons 'i', 'j' and 'k'. Once the king is spawned it's health bar will be displayed on the side and the length of the health bar would vary according to the king's health.  The movement of barbarians is automtated. They move towards the closest non wall building and attack it. If any wall comes in its path then it would first destroy that wall and then attack the building.  Initially I have taken the time stamp of barbarians to be 1 sec and the speed of the king as 1 tile per render.

Cannons check for the buildings that are within the radius of 6 tiles and attack them. Time stamp for cannons is taken as 0.5 secs i.e cannon checks for the target and attacks it for every 0.5 secs. The color of the cannons is changed to RED whenever they start firing. 

The color of all the non wall buildings vary according to their health. I have also implemented 2 types of spells. Rage spell gets activated when the key 'r' is pressed and it will be active for 5 secs. During this period, the background color of the board changes to CYAN and speed of the kings gets doubled and time stamp of the barbarians will be halved and the damage of all the troops and king will be doubled. Heal spell get activated on pressing the key 'h'. This spell increases the health of all the troops and king to 150% of their current health. I have taken that both the spells can be executed exactly once. 

I will also check for the live status of all the troops, king and building every time and if the livestat of king and troops is 0 i.e all the troops and king are dead then the game ends and it prints 'DEFEAT' and the time taken. If all the buildings are dead then I printed 'VICTORY' and the time taken.

I have also implemented the replay function. On running the replay.py file, we are supposed to enter the game number which we want to view and the file with the corresponding number opens and all its contents will be displayed.

Levaithan axe feature will be activated when the key 'l' is pressed. Here the king attacks all the buildings that are in the range of 5 tiles to it.

