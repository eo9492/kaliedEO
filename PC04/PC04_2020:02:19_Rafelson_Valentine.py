"""
PC04- Jump till you levitate
E.O. Rafelson, Gabriel Valentine
02/19/20
This code creates 2 robots and stairs for them to play on in pygame. 


PSEUDOCODE
Create another robot by using in class example, changing all x to x1 and y to y1. 
Modify both robots.
create movement for robots using asdw for left spawn and arrow keys for right spawning robot. As well as J and K keys
for 'jump' to combat gravity. 
Create Stairs using draw rect function 
create gravity that pulls robots down until they hit stair using if statements 
create barriers on stairs that dont allow robots to move into them while standing on them using if statements
create fun interaction when both robots are at same location. 
create inverse black and white if statement. 




Code modified from in class example 
Link: https://cdn.inst-fs-iad-prod.inscloudgate.net/c49397e8-d940-418c-b465-55634e4b09af/Robot.py?token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6ImNkbiJ9.eyJyZXNvdXJjZSI6Ii9jNDkzOTdlOC1kOTQwLTQxOGMtYjQ2NS01NTYzNGU0YjA5YWYvUm9ib3QucHkiLCJ0ZW5hbnQiOiJjYW52YXMiLCJ1c2VyX2lkIjoiMTA3NzIwMDAwMDAwMzQwNDA2IiwiaWF0IjoxNTg4NTU0MTM0LCJleHAiOjE1ODg2NDA1MzR9.-PjGJVediMI22wwulb3PTq_8YfdXzCCyqPsLiNFv5gn8PLt8i1sswQDeosjE6TDcAwbUyxpAkM1cD5p5axYUtg&content_type=text%2Fx-python-script
After working on code for a while we found slight bug where robot can enter into a stair if they are in the air next 
to it, but not if they are standing on it. We decided to keep this as an easter egg.

Try to get the robots in the same location! See what happens. 

"""


import pygame
from random import *

#set up colors for robot
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

#create screen and game variables
xsize = 1200
ysize = 800
screen = pygame.display.set_mode((xsize,ysize)) #create 500 x500 pixel screen

run = True
x = xsize/2 #center positions for low robot parts
y = ysize/2
scale = 1 #variable to adjust when keys are pressed to change size of robot
speed = 10
eye_r = 2


x1 = xsize/2 #center positions for high robot parts
y1 = ysize/2


#starting points for low and high robots
x -= 520
y += 300

x1 -= -450
y1 += -300

#Robo features
blink = [GREEN, BLUE, RED, LT_BLUE]
color = choice(blink) #assign a value to color
colorL = choice(blink) #assign a value to color
colorR = choice(blink) #assign a value to color

def stairs():
    pygame.draw.rect(screen, BLACK, [150,700,150,100])
    pygame.draw.rect(screen, BLACK, [300,600,150,200])
    pygame.draw.rect(screen, BLACK, [450,500,150,300])
    pygame.draw.rect(screen, BLACK, [600,400,150,400])
    pygame.draw.rect(screen, BLACK, [750,300,150,500])
    pygame.draw.rect(screen, BLACK, [900,200,150,600])
    pygame.draw.rect(screen, BLACK, [1050,200,150,700])



#Game loop
while run:
    # create exit-on click detection:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            
     
    screen.fill(WHITE)
    stairs()
#creates low robot 
    Head = pygame.draw.rect(screen,RED,(x-38,y-90,75,50)) 
    Body = pygame.draw.polygon(screen, BLUE, [(x+35, y-35),(x+45,y+35), (x-45,y+35),(x-35, y-35)])
    L_eye = pygame.draw.circle(screen, GREEN, (int(x-10), int(y-70)),eye_r)
    R_eye = pygame.draw.circle(screen, GREEN, (int(x+10), int(y-70)),eye_r)
    panelLights1 = pygame.draw.circle(screen, colorR, (int(x+20), int(y-5)),3)
    panelLights2 = pygame.draw.circle(screen, color, (int(x), int(y-5)),3)
    panelLights3 = pygame.draw.circle(screen, colorL, (int(x-20), int(y-5)),3)

    L_wheel = pygame.draw.circle(screen, BLACK, (int(x-40), int(y+63)),20)
    R_wheel = pygame.draw.circle(screen, BLACK, (int(x+40), int(y+63)),20)
    L_hub = pygame.draw.circle(screen, DK_GRAY, (int(x-40), int(y+63)),10)
    R_hub = pygame.draw.circle(screen, DK_GRAY, (int(x+40), int(y+63)),10)
    Track = pygame.draw.ellipse(screen, DK_GRAY, (int(x-65), int(y+33),130,60),2)

#creates high robot 
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
    pygame.display.update() #update all changes to screen

#controls for low start robot
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        x += speed
    if keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_s]:
        y += speed
    if keys[pygame.K_j]:
        y-= speed*10
        
        
 #controls for high start robot       
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x1 += speed
    if keys[pygame.K_LEFT]:
        x1 -= speed
    if keys[pygame.K_UP]:
        y1 -= speed
    if keys[pygame.K_DOWN]:
        y1 += speed
    if keys[pygame.K_k]:
        y1-= speed*10

        
    if keys[pygame.K_SPACE]:
            BLACK = WHITE1
            WHITE = BLACK1
        
        
        
#Gravity for both robots
    if y< 800-93 and 0<x<=85:
        y += speed
    if y< 700-93 and 0<x<=235:
        y += speed 
    if y< 600-93 and 0<x<=385:
        y += speed 
    if y< 500-93 and 0<x<=535:
        y += speed 
    if y< 400-93 and 0<x<=685:
        y += speed 
    if y< 300-93 and 0<x<=835:
        y += speed 
    if y< 200-93 and 0<x<=985:
        y += speed 
    if y< 200-93 and 0<x<=1135:
        y += speed 
    
    if y1< 800-93 and 0<x1<=85:
        y1 += speed
    if y1< 700-93 and 0<x1<=235:
        y1 += speed 
    if y1< 600-93 and 0<x1<=385:
        y1 += speed 
    if y1< 500-93 and 0<x1<=535:
        y1+= speed 
    if y1< 400-93 and 0<x1<=685:
        y1 += speed 
    if y1< 300-93 and 0<x1<=835:
        y1 += speed 
    if y1< 200-93 and 0<x1<=985:
        y1 += speed 
    if y1< 200-93 and 0<x1<=1135:
        y1 += speed 
        
#barriers on stairs for both robots       

    if 800-93<y<= 900-93 and x>85:
        x -= speed
    if 700-93<y<= 800-93 and x>235:
        x -= speed
    if 600-93<y<= 700-93 and  x>385:
        x -= speed
    if 500-93< y<= 600-93 and x>535:
        x -= speed 
    if 400-93< y<= 500-93 and x>685:
        x -= speed
    if 300-93<y<= 400-93 and x>835:
        x -= speed 
    if 200-93<y<= 300-93 and x>1135:
        x -= speed 
    if 0-93<y<= 200-93 and x>1135:
        x -= speed  
        
        
    if 700-93<y1<= 800-93 and x1>235:
        x1 -= speed
    if 600-93<y1<= 700-93 and  x1>385:
        x1 -= speed
    if 500-93< y1<= 600-93 and x1>535:
        x1 -= speed 
    if 400-93< y1<= 500-93 and x1>685:
        x1 -= speed
    if 300-93<y1<= 400-93 and x1>835:
        x1 -= speed 
    if 200-93<y1<= 300-93 and x1>1135:
        x1 -= speed 
    if 0-93<y1<= 200-93 and x1>1135:
        x1 -= speed 


        
#interaction when robots are at same location. 
    if x1 ==x and y1 ==y: 
        y-= speed*3
        y1-= speed*3
        

#stairs

    pygame.display.update()
#Used in class example to start this code