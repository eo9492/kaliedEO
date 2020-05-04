"""
PC05 Dance robot dance!
E.O. Rafelson, Gabriel Valentine
3/08/2020


Pseudocode:
Make screen
make robot (use same as modified from PC04) in the top right corner
make random amount of balls in random places using randint function
make collision detector with robot and balls that causes robot to move after first hit and pops balls from RectList to make them disappear
make functions that move robot left and right 
make robot switch directions with each ball added by using said functions
make function that quits pygame if robot goes off screen

   
Description:
This script will create a random number of circles in random locations.
Drag the circles to the robot and they will vanish and the robot will try to juke you out. Better be quick... 


Code modified from Dr. Z in class scripts for PC05 and PC04 
Links:
https://cdn.inst-fs-iad-prod.inscloudgate.net/c49397e8-d940-418c-b465-55634e4b09af/Robot.py?token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6ImNkbiJ9.eyJyZXNvdXJjZSI6Ii9jNDkzOTdlOC1kOTQwLTQxOGMtYjQ2NS01NTYzNGU0YjA5YWYvUm9ib3QucHkiLCJ0ZW5hbnQiOiJjYW52YXMiLCJ1c2VyX2lkIjoiMTA3NzIwMDAwMDAwMzQwNDA2IiwiaWF0IjoxNTg4NTU0MTM0LCJleHAiOjE1ODg2NDA1MzR9.-PjGJVediMI22wwulb3PTq_8YfdXzCCyqPsLiNFv5gn8PLt8i1sswQDeosjE6TDcAwbUyxpAkM1cD5p5axYUtg&content_type=text%2Fx-python-script
https://cdn.inst-fs-iad-prod.inscloudgate.net/fef24c56-8b39-4fe5-bd2e-9da829c4f1f1/pygameDragIC.py?token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6ImNkbiJ9.eyJyZXNvdXJjZSI6Ii9mZWYyNGM1Ni04YjM5LTRmZTUtYmQyZS05ZGE4MjljNGYxZjEvcHlnYW1lRHJhZ0lDLnB5IiwidGVuYW50IjoiY2FudmFzIiwidXNlcl9pZCI6IjEwNzcyMDAwMDAwMDM0MDQwNiIsImlhdCI6MTU4ODUzNTQ1MywiZXhwIjoxNTg4NjIxODUzfQ.aV7mpOLLNcS4W_hf0Ha-AZy0mWSa5GRjSz0q0t-Ih-aP04F-NzOm7BIXeAqmmJmM7ZW8eUnMq9pKbSK-zrShYQ&content_type=text%2Fx-python-script   
"""



import pygame
from random import *
pygame.init() #initialize all the pygame functions so it actually DOES stuff.

#create screen 
xsize = 1200
ysize = 800
screen = pygame.display.set_mode((xsize,ysize))
Run = True #for game loop
drag = False #boolean that determines if dragging happens

#screen color
blue = (135,206,250)

#robot colors
BLACK = (0,0,0)
BLACK1 = (0,0,0)
RED = (255,0,0)
PINK = (170,0,50)
GREEN = (0,255,0)
BLUE = (0,0,255)
LT_BLUE = (0, 100, 255)
WHITE = (255,255,255)
WHITE1 = (255,255,255)
GRAY = (127,127,127)
DK_GRAY = (100,100,100)

#robot light colors
blink = [GREEN, BLUE, RED, LT_BLUE]
color = choice(blink) #assign a value to color
colorL = choice(blink) #assign a value to color
colorR = choice(blink)

x1 = xsize/2 #center positions for  robot parts
y1 = ysize/2

#offset to move robot to top right
x1 -= -450
y1 += -300


speed = 10 #speed of balls
eye_r = 2 #robot size adjust




#random coordinates for balls to spawn
xvalues = (400,100,200,300,500,450,350)
yvalues = (400,100,200,300,500,450,350)

x=xvalues[randint(0,6)]
y=yvalues[randint(0,6)]
r = 20 #how big we want things to be
step = 10


#creates Rect for our circles for collide function 
rect = pygame.Rect(x,y,r*2,r*2)
#the r is the circle  RADIUS, but we want the rect with to be equal to DIAMETER, so:
#diameter = radius * 2

numbers= (2,3,4,5,6) #possible number of balls
numCirc = (numbers[randint(1,4)])
rectList =[] #empty list to start Rectlist
for i in range(numCirc): #gets balls ready for game 
    rectList.append(pygame.Rect(xvalues[randint(0,6)],(yvalues[randint(0,6)]),r*2,r*2))




#moves bot left 
def moveBotLeft():
    global x1
    x1 -= 3
    botMoveLeft = True
#moves bot right
def moveBotRight():
    global x1
    x1 += 3
    botMoveRight = True

#detects if robot leaves screen
def offScreen(x):
    if x >1250 or x<-50:
        done = pygame.quit()
        print ("Too slow! The following errors are my (the robot's) way of telling you to F off... #endrobotslavery ")
        return done
        
#counts score
def countScore(ballsLeft, balls):
    score = balls - ballsLeft
    print('your score is '+str(score))

    

while Run: #start the game loop! 
    offScreen(x1)
    for event in pygame.event.get(): #scan all events --things happening outside python (mouse and keyboard actions)
        if event.type == pygame.QUIT:
            pygame.quit() #add a quit function so it stops up background tasks
           
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos() #get our x and y positions of where the click happened
            for i in range(len(rectList)):        
                if rectList[i].collidepoint(pos[0],pos[1]):
                    drag = True #whenever the mouse is down, we can drag our balls
                    selected = i
                    offsetX = rectList[i].x - pos[0] #calculates the difference between where the rectangle is and where the click happened
                    offsetY = rectList[i].y - pos[1]

        elif event.type == pygame.MOUSEMOTION:
            if drag: 
                pos = event.pos #update position as mouse moves around
                #update the position of the shape based on where the mouse motion event is happening (where the cursor is)
                rectList[selected].x = pos[0] + offsetX
                rectList[selected].y = pos[1] + offsetY
               
        elif event.type == pygame.MOUSEBUTTONUP: #ok, now we're done dragging, so we want to detect when the mouse button is released.
            pop = event.pos
            if Body1.collidepoint(pos[0],pos[1]) and drag: #from Dr. Z, detects if ball collides with robot 
                rectList.pop(selected)
                balls = numCirc
                ballsLeft = len(rectList)
                countScore(ballsLeft, balls)
            drag = False
            
    #Switches direction of bot movement with each ball added and stops once all done 
    if len(rectList) == numCirc - 1:
        moveBotLeft()
    elif len(rectList) == numCirc - 2:
        moveBotRight()
    elif len(rectList) == numCirc - 3:
        moveBotLeft()
    elif len(rectList) == numCirc - 4:
        moveBotRight()
    elif len(rectList) == numCirc - 5:
        moveBotLeft()
    elif len(rectList) == numCirc - 6:
        moveBotRight()
    elif len(rectList) == numCirc - 7:
        moveBotLeft()
    if len(rectList) == 0 :
        print('and you filled me up!')
        Run = False
    
        
        
    
    speed = [randint(-step,step),randint(-step,step)] #random displacement to add fun wiggles to our circle.
   
    screen.fill(blue) #draw/redraw the screen to "erase" previous drawings
   
    #draws the circle object on top of our Rectangle
    for i in range(len(rectList)):
       
        pygame.draw.circle(screen, (0,0,0), (rectList[i].x + speed[0], rectList[i].y+speed[1]), r) #(x+randint(-3,3), y+randint(-3,3) ), 15)
 

   
    Head1 = pygame.draw.rect(screen,GRAY,(x1-37,y1-78,75,15))
    Body1 = pygame.draw.polygon(screen, PINK, [(x1+30, y1-30),(x1+55,y1+25), (x1-45,y1+35),(x1-15, y1-25)])
    L_eye1 = pygame.draw.circle(screen, GREEN, (int(x1-10), int(y1-70)),eye_r)
    panelLights11 = pygame.draw.circle(screen, colorR, (int(x1+20), int(y1-5)),3)
    panelLights21 = pygame.draw.circle(screen, color, (int(x1), int(y1-5)),3)
    panelLights31 = pygame.draw.circle(screen, colorL, (int(x1-20), int(y1-5)),3)

    L_wheel1 = pygame.draw.circle(screen, BLACK, (int(x1-40), int(y1+63)),20)
    R_wheel1 = pygame.draw.circle(screen, BLACK, (int(x1+40), int(y1+63)),20)
    L_hub1 = pygame.draw.circle(screen, PINK, (int(x1-40), int(y1+63)),10)
    R_hub1 = pygame.draw.circle(screen, PINK, (int(x1+40), int(y1+63)),10)
   
    pygame.time.wait(0)
    pygame.display.update()
   
   
   
   
 
 
    #update our image to our screen
   











