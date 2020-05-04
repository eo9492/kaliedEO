"""
Final Project: I like your robo sneakers.
EO Rafelson
4/27/2020


Pseudocode:
Import modules
create screen
create class that inititilizes a robot object with a method that draws robot on the screen 
create attibutes for robot parts that can move separatley with reference to center position
create functions that move different parts of robo and moves robo as a whole
modify Dr Z's amplitude class for my song 
use amplitude to create new animations that respond to loudness of the music, 
changing color of the background various shades of red and white and fancy robo sneakers shades of grey
in game loop separate instances of time since starting using pygame.time.get_ticks()- a start time variable to maximize pprecision timing 
make robot dance across screen using my functions for certain amounts of time! 


Parts of Code modified from Dr Z's Anim, and make robot, and Timing sound an animations,
as well as snipits from my previous PC's. All is cited respectively, of course.

 
Description:
This script will create a robot that dances to Opuio's song Sneakers

unfortunately this song too large for Github. Here is a link to download the song: 
https://drive.google.com/file/d/1NL2w5WVNgZapZMXacvZkXg-q9tPOYra1/view?usp=sharing


Song: Opuio - Sneakers 
I do not own the rights to this song.
For entertainment purposes only. 
Please don't be mad Mr. Opuio. 

*** WARNING ***
*** STROBE LIGHTS *** 


Note: you must restart kernel everytime you watch due to time settings. Enjoy!
"""


#imports modules 
import pygame
from random import *
from time import *
import numpy as np
from pydub import AudioSegment
from pydub.playback import play
import pdb

pygame.init() #initialize all the pygame functions.

#creates screen 
xsize = 1250
ysize = 850
screen = pygame.display.set_mode((xsize,ysize))




Run = True #for game loop

#variable for circPath functions 
theta = np.linspace(0,6*np.pi, 200)


#robot colors
#modified signifigantly from Dr. Z's example robot script 
#https://cdn.inst-fs-iad-prod.inscloudgate.net/c49397e8-d940-418c-b465-55634e4b09af/Robot.py?token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6ImNkbiJ9.eyJyZXNvdXJjZSI6Ii9jNDkzOTdlOC1kOTQwLTQxOGMtYjQ2NS01NTYzNGU0YjA5YWYvUm9ib3QucHkiLCJ0ZW5hbnQiOiJjYW52YXMiLCJ1c2VyX2lkIjoiMTA3NzIwMDAwMDAwMzQwNDA2IiwiaWF0IjoxNTg3OTk5MjY2LCJleHAiOjE1ODgwODU2NjZ9.RfPfgLvUkP2ftdl5fIqS3RFqwmE4VaN8WxPiemGef6l6vll9HKFRpevvupraU8agHwHj--i71suMN1FknJnuiQ&content_type=text%2Fx-python-script
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



x1 = xsize/2 #center positions for  robot parts
y1 = ysize/2
y1-= 200 #offset to move robot up a bit



#variables for Circpath functions to give each part its own contiunous circle movement when called 
a = 0
b = 0
c = 0
d = 0
e = 0




#following class taken and slightly modifed from Dr. Z's Timing sound an animations example script
#https://cdn.inst-fs-iad-prod.inscloudgate.net/c3ad6698-ff1d-4b90-8901-e1a3c200ced7/soundSync.py?token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6ImNkbiJ9.eyJyZXNvdXJjZSI6Ii9jM2FkNjY5OC1mZjFkLTRiOTAtODkwMS1lMWEzYzIwMGNlZDcvc291bmRTeW5jLnB5IiwidGVuYW50IjoiY2FudmFzIiwidXNlcl9pZCI6IjEwNzcyMDAwMDAwMDM0MDQwNiIsImlhdCI6MTU4Nzk5NDQzNCwiZXhwIjoxNTg4MDgwODM0fQ.NNuU87qiir6TfQqS0RonMfot9_IVtDKkCS2FL69s_AkGn3lU5tW4h9BbmdsrVjqzBF4c7avElA2gggxaaIB6rw&content_type=text%2Fx-python-script
class soundCtrlr:
    def __init__(self,filename='sneakers.wav',channel=0):
        self.sound = AudioSegment.from_file(filename) #replace string with YOUR filename with extension (works with wav and mp3)
        self.pySound = pygame.mixer.Sound(filename) #for playing sounds
        self.samples = self.sound.get_array_of_samples() #puts the sound file into a numpy array, for manipulation
        self.bitrate = 1/(self.sound.duration_seconds/len(self.samples)) # samplerate (bitrate) of pydub sound, in Hz
        self.channel=channel
        self.start()
        
    def start(self):
        '''Plays corresponding sound. To play multiple sounds from multiple objects,
        change the channel index. The default number of pygame sound channels is 16.
        You can continually play 16 sounds at once.'''
        
        pygame.mixer.Channel(self.channel).play(self.pySound)
        self.start_time = pygame.time.get_ticks() #updates starttime, makes timenow
   
    def getCurrAmp(self):
        '''Gets the amount of time that has passed since the song started playing
        amount of time that has lapsed from start of play, in ms. Then calculates 
        the sample index from to grab data. Returns the amplitude of the sound
        at the current time, and the index of the samples list'''
        
        self.timenow = (pygame.time.get_ticks() - self.start_time)/1000
        idx = int(self.timenow * self.bitrate) 
        if idx>len(self.samples):
            idx = -1
        amp = int(np.abs(self.samples[idx])) #radius changes with amplitude try 1000
        return amp, idx









class Robot:
    def __init__(self, x1=x1, y1=y1):
        self.x1 = x1 #center x position
        self.y1 = y1 #center y position
        self.LR = 20 #left wheel radius
        self.RR = 20 #Right wheel radius
        self.LX = 40 #left wheel x position offset
        self.LY = 63 #left wheel y position offset
        self.RX = 40 #right wheel x position offset
        self.RY = 63 #right wheel y position offset
        self.HX = 37 #Head x offset 
        self.HY = 78 #Head y offset 
        self.EX = 15 #eye offset 
        self.EY = 70 #eye right offset
        self.eye_r = 8 #eye radius
        self.C1 = 30  #corner 1 x position of body 
        self.C2 = -30 #corner 1 y position of body 
        self.C3 = 55 #corner 2 x position of body 
        self.C4 = 25 #corner 2 y position of body 
        self.C5 = -45 #corner 3 x position of body 
        self.C6 =  35 #corner 3 y position of body 
        self.C7 = -15 #corner 4 x position of body 
        self.C8 = -25 #corner 4 y position of body 
        
        
        
        
        
        

 
        


    def makeBot(self):
        """Creates Robot"""
        #modified signifigantly from Dr. Z's example robot
        #https://cdn.inst-fs-iad-prod.inscloudgate.net/c49397e8-d940-418c-b465-55634e4b09af/Robot.py?token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6ImNkbiJ9.eyJyZXNvdXJjZSI6Ii9jNDkzOTdlOC1kOTQwLTQxOGMtYjQ2NS01NTYzNGU0YjA5YWYvUm9ib3QucHkiLCJ0ZW5hbnQiOiJjYW52YXMiLCJ1c2VyX2lkIjoiMTA3NzIwMDAwMDAwMzQwNDA2IiwiaWF0IjoxNTg3OTk5MjY2LCJleHAiOjE1ODgwODU2NjZ9.RfPfgLvUkP2ftdl5fIqS3RFqwmE4VaN8WxPiemGef6l6vll9HKFRpevvupraU8agHwHj--i71suMN1FknJnuiQ&content_type=text%2Fx-python-script
        
        
        Head1 = pygame.draw.rect(screen,WHITE,(self.x1-self.HX,self.y1-self.HY,75,15))
        Body1 = pygame.draw.polygon(screen, PINK, [(self.x1+30, self.y1-30),(self.x1+55,self.y1+25), (self.x1-45,self.y1+35),(self.x1-15, self.y1-25)])
        L_eye1 = pygame.draw.circle(screen, BLACK1, (int(self.x1-self.EX), int(self.y1-self.EY)),self.eye_r)
        R_eye1 = pygame.draw.circle(screen, BLACK1, (int(self.x1-self.EX+30), int(self.y1-self.EY)),self.eye_r)
        Glasses1 = pygame.draw.rect(screen,BLACK1,(self.x1-self.HX,self.y1-self.HY+5,75,3))
        Body1 = pygame.draw.polygon(screen, PINK, [(self.x1+self.C1, self.y1+self.C2),(self.x1+self.C3, self.y1+self.C4), (self.x1+self.C5,self.y1+self.C6),(self.x1+self.C7, self.y1+self.C8)])
        panelLights11 = pygame.draw.circle(screen, GREEN, (int(self.x1+20), int(self.y1-5)),3)
        panelLights21 = pygame.draw.circle(screen, GREEN, (int(self.x1), int(self.y1-5)),3)
        panelLights31 = pygame.draw.circle(screen, GREEN, (int(self.x1-20), int(self.y1-5)),3)
    
        L_wheel1 = pygame.draw.circle(screen, BLACK, (int(self.x1-self.LX), int(self.y1+self.LY)), self.LR)
        R_wheel1 = pygame.draw.circle(screen, BLACK, (int(self.x1+self.RX), int(self.y1+self.RY)), self.RR)
        L_hub1 = pygame.draw.circle(screen, PINK, (int(self.x1-self.LX), int(self.y1+self.LY)),10)
        R_hub1 = pygame.draw.circle(screen, PINK, (int(self.x1+self.RX), int(self.y1+self.RY)),10)
    
    
    
def moveBot(x, y, Dir,speed):
    """moves whole robot in any direction at a given speed. To move diagonal use 2 at the same time ex up and right"""
    if Dir == 'left':
        x -= speed
    elif Dir == 'right':
        x += speed 
    elif Dir == 'up':
        y -= speed 
    else: 
        y+= speed
    return x, y
    

    
def wheelSize(wheel, grow):
    """Causes a given wheel on the robot to grow or shrink"""
    if grow == 'grow':
        step =.3
    else:
        step=-.3
    if wheel == 'left':
        Bot1.LR += step
    else:
        Bot1.RR +=step
    

    
def circPath(part,r,theta):  
    '''Creates the circular path for robot and or wheel/ head modified from in class anim.py'''
    #https://canvas.colorado.edu/courses/59943/files/15509321?module_item_id=1872226
    if part == 'bot':
        Bot1.x1 = r * -np.cos(theta) + Bot1.x1 
        Bot1.y1 = r * -np.sin(theta) + Bot1.y1
    elif part == 'left wheel':
        Bot1.LX = r * np.cos(theta) + Bot1.LX 
        Bot1.LY = r * np.sin(theta) + Bot1.LY
    elif part == 'head':
        Bot1.HX = r * np.cos(theta) + Bot1.HX 
        Bot1.HY = r * np.sin(theta) + Bot1.HY
        Bot1.EX = r * np.cos(theta) + Bot1.EX
        Bot1.EY = r * np.sin(theta) + Bot1.EY
    elif part == 'corner 1':
        Bot1.C1 = r * np.cos(theta) + Bot1.C1
        Bot1.C2 = r * np.sin(theta) + Bot1.C2
    else:
        Bot1.RX = r * np.cos(theta) + Bot1.RX 
        Bot1.RY = r * np.sin(theta) + Bot1.RY





    
def  moveHead(H,E,Dir,speed):
    """Moves robot head separate from robot"""
    if Dir == 'left' or Dir == 'up':
        step = speed
    else:
        step = -speed 
        
    H += step
    E += step
    return H, E
        
def bodyGrow(speed):
    """causes the body of the robot to grow at a given speed"""
    Bot1.C1 += speed
    Bot1.C2 -= speed
    Bot1.C3 += speed
    Bot1.C4 += speed
    Bot1.C5 -= speed
    Bot1.C6 += speed
    Bot1.C7 -= speed
    Bot1.C8 -= speed
        
            


Bot1 = Robot()   #instatiates my robot object

Sauce = soundCtrlr() #instatiates sound controller so animations can respond to amplitutde 


#RGB color values that change with amplitude

R=0     
B=0
G=0



start_time = pygame.time.get_ticks() #gets time taken since pygame.init() was called

while Run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            Run = False
            pygame.mixer.music.pause()
   #sets time = to miliseconds passed since start of while loop so I can have robo do certian moves at certain times, +250 for slight correction           
    time =    pygame.time.get_ticks() - start_time +250  
    
            
    A ,idx = Sauce.getCurrAmp()  #fetches Amplitude and index of song also modified from Dr. Z's sound controller cited with class above 
    amp = abs(A) #makes all amplitudes positve for animations sake 
    
    
    
    #causes brightness of red background to change with amplitude, switches to a mellow grey if really loud to create flash effect 
    #also causes brightness of grey robo sneakers to change with amplitude
    if amp< 20000:       
       R = amp/100
       G = 0
       B = 0
    else:
       R = 150
       G = 150
       B = 150
       
    BLACK = (R,R,R) #makes 'BLACK' robo sneakers, grey, brighter with louder parts of song 
    BG = (R,G,B)  #Background color 
    screen.fill(BG) #fills screen with RGB values


    

    #causes animations at given times after pressing play using functions above
    if 4000 < time <= 6000:
        Bot1.HX, Bot1.EX = moveHead(Bot1.HX, Bot1.EX, 'left',1)        
    elif 6000  < time <= 6500:
        Bot1.HX, Bot1.EX = moveHead(Bot1.HX, Bot1.EX, 'right',1)
        Bot1.HY, Bot1.EY = moveHead(Bot1.HY, Bot1.EY, 'up',1)      
    elif 6500  < time <= 7000:
        Bot1.HX, Bot1.EX = moveHead(Bot1.HX, Bot1.EX, 'right',1)
        Bot1.HY, Bot1.EY = moveHead(Bot1.HY, Bot1.EY, 'down',1)
    elif 7000  < time <= 7500:
        Bot1.HX, Bot1.EX = moveHead(Bot1.HX, Bot1.EX, 'right',1)
        Bot1.HY, Bot1.EY = moveHead(Bot1.HY, Bot1.EY, 'up',1)
    elif 7500  < time <= 8000:
        Bot1.HX, Bot1.EX = moveHead(Bot1.HX, Bot1.EX, 'right',1)
        Bot1.HY, Bot1.EY = moveHead(Bot1.HY, Bot1.EY, 'down',1)
    elif 8000  < time <= 8500:
        Bot1.HX, Bot1.EX = moveHead(Bot1.HX, Bot1.EX, 'right',1)
        Bot1.HY, Bot1.EY = moveHead(Bot1.HY, Bot1.EY, 'up',1)
    elif 8500  < time <= 8750:
        Bot1.HX, Bot1.EX = moveHead(Bot1.HX, Bot1.EX, 'right',1)
        Bot1.HY, Bot1.EY = moveHead(Bot1.HY, Bot1.EY, 'down',1)
    elif 8750  < time <= 9000:
        Bot1.HX, Bot1.EX = moveHead(Bot1.HX, Bot1.EX, 'right',1)
        Bot1.HY, Bot1.EY = moveHead(Bot1.HY, Bot1.EY, 'up',1)   
    elif 9000  < time <= 9250:
        Bot1.HX, Bot1.EX = moveHead(Bot1.HX, Bot1.EX, 'right',1)
        Bot1.HY, Bot1.EY = moveHead(Bot1.HY, Bot1.EY, 'down',1)
    elif 9250  < time <= 9500:
        Bot1.HX, Bot1.EX = moveHead(Bot1.HX, Bot1.EX, 'right',1)
        Bot1.HY, Bot1.EY = moveHead(Bot1.HY, Bot1.EY, 'up',1) 
    elif 9500  < time <= 10000:
        Bot1.HX, Bot1.EX = moveHead(Bot1.HX, Bot1.EX, 'right',1)
        Bot1.HY, Bot1.EY = moveHead(Bot1.HY, Bot1.EY, 'down',1)
    elif 10000  < time <= 10250:
        Bot1.HX, Bot1.EX = moveHead(Bot1.HX, Bot1.EX, 'left',1)
        Bot1.HY, Bot1.EY = moveHead(Bot1.HY, Bot1.EY, 'up',1)
    elif 10250  < time <= 10500:
        Bot1.HX, Bot1.EX = moveHead(Bot1.HX, Bot1.EX, 'left',1)
        Bot1.HY, Bot1.EY = moveHead(Bot1.HY, Bot1.EY, 'down',1)
    elif 10500  < time <= 10750:
        Bot1.HX, Bot1.EX = moveHead(Bot1.HX, Bot1.EX, 'left',1)
        Bot1.HY, Bot1.EY = moveHead(Bot1.HY, Bot1.EY, 'up',1)
    elif 10750  < time <= 11000:
        Bot1.HX, Bot1.EX = moveHead(Bot1.HX, Bot1.EX, 'left',1)
        Bot1.HY, Bot1.EY = moveHead(Bot1.HY, Bot1.EY, 'down',1)
    elif 11000  < time <= 11250:
        Bot1.HX, Bot1.EX = moveHead(Bot1.HX, Bot1.EX, 'left',1)
        Bot1.HY, Bot1.EY = moveHead(Bot1.HY, Bot1.EY, 'up',1)
    elif 11250  < time <= 11500:
        Bot1.HX, Bot1.EX = moveHead(Bot1.HX, Bot1.EX, 'left',1)
        Bot1.HY, Bot1.EY = moveHead(Bot1.HY, Bot1.EY, 'down',1)
    elif 11500  < time <= 11750:
        Bot1.HX, Bot1.EX = moveHead(Bot1.HX, Bot1.EX, 'left',1)
        Bot1.HY, Bot1.EY = moveHead(Bot1.HY, Bot1.EY, 'up',1)
    elif 11750  < time <= 12000:
        Bot1.HX, Bot1.EX = moveHead(Bot1.HX, Bot1.EX, 'left',1)
        Bot1.HY, Bot1.EY = moveHead(Bot1.HY, Bot1.EY, 'down',1)
    elif 12000 < time <= 14000:
        Bot1.HY, Bot1.EY = moveHead(Bot1.HY, Bot1.EY, 'up',1)
    elif 14000 < time <= 16000:
        Bot1.HY, Bot1.EY = moveHead(Bot1.HY, Bot1.EY, 'down',1)
    elif 16000 < time <= 18000:
        Bot1.x1, Bot1.y1 = moveBot(Bot1.x1, Bot1.y1, 'down',3)
    elif 18000 < time <= 20000:
        Bot1.x1, Bot1.y1 = moveBot(Bot1.x1, Bot1.y1, 'left',3)
        Bot1.HX, Bot1.EX = moveHead(Bot1.HX, Bot1.EX, 'left',1)
    elif 20000 < time <= 22000:
        Bot1.x1, Bot1.y1 = moveBot(Bot1.x1, Bot1.y1, 'right',3)
        Bot1.HX, Bot1.EX = moveHead(Bot1.HX, Bot1.EX, 'right',1)
    elif 22000 < time <= 24000:
        Bot1.x1, Bot1.y1 = moveBot(Bot1.x1, Bot1.y1, 'up',1)
        wheelSize('left', 'grow')
    elif 24000 < time <= 26000:
        wheelSize('left', 'shrink')
        wheelSize('right', 'grow')
    elif 26000 < time <= 28000:
        wheelSize('left', 'grow')
        wheelSize('right', 'shrink')
    elif 28000 < time <= 30000:
        wheelSize('left', 'shrink')
        wheelSize('right', 'grow')
    elif 30000 < time <= 32000:
        wheelSize('right', 'shrink')
        circPath('left wheel',3,theta[a])
        a += 1 
        if a >= len(theta):   
            a = 0  
    elif 32000 < time <= 35000:
        circPath('right wheel',3,theta[b])
        b += 1 
        if b >= len(theta):   
            b = 0  
        circPath('left wheel',3,theta[c])
        c += 1 
        if c >= len(theta):   
            c = 0  
    elif 35000 < time< 40000:
        circPath('bot', 10, theta[d])
        d += 1 
        if d >= len(theta):   
            d = 0       
    elif 40000 < time< 42000:
        Bot1.x1, Bot1.y1 = moveBot(Bot1.x1, Bot1.y1, 'left',2)
        circPath('right wheel',3,theta[b])
        b += 1 
        if b >= len(theta):   
            b = 0  
        circPath('left wheel',3,theta[c])
        c += 1 
        if c >= len(theta):   
            c = 0  
    elif 42000 < time< 45000:
        Bot1.x1, Bot1.y1 = moveBot(Bot1.x1, Bot1.y1, 'right',2)
        circPath('right wheel',3,theta[b])
        b += 1 
        if b >= len(theta):   
            b = 0  
        circPath('left wheel',3,theta[c])
        c += 1 
        if c >= len(theta):   
            c = 0  
    elif 45000 < time< 47750:
        Bot1.x1, Bot1.y1 = moveBot(Bot1.x1, Bot1.y1, 'down',1)
        Bot1.HY, Bot1.EY = moveHead(Bot1.HY, Bot1.EY, 'up',1)
    elif 47750 < time< 50750:
        Bot1.x1, Bot1.y1 = moveBot(Bot1.x1, Bot1.y1, 'up',1)
        Bot1.HY, Bot1.EY = moveHead(Bot1.HY, Bot1.EY, 'down',1)
    elif 52800 < time <55000:
        Bot1.x1, Bot1.y1 = moveBot(Bot1.x1, Bot1.y1, 'left',1)
        Bot1.x1, Bot1.y1 = moveBot(Bot1.x1, Bot1.y1, 'down',1)
        circPath('right wheel',3,theta[b])
        b += 1 
        if b >= len(theta):   
            b = 0  
        circPath('left wheel',3,theta[c])
        c += 1 
        if c >= len(theta):   
            c = 0  
    elif 55000 < time< 56000:
        Bot1.x1, Bot1.y1 = moveBot(Bot1.x1, Bot1.y1, 'left',1)
        Bot1.x1, Bot1.y1 = moveBot(Bot1.x1, Bot1.y1, 'up',1)
        circPath('right wheel',3,theta[b])
        b += 1 
        if b >= len(theta):   
            b = 0  
        circPath('left wheel',3,theta[c])
        c += 1 
        if c >= len(theta):   
            c = 0  
    elif 56000 < time <58000:
        Bot1.x1, Bot1.y1 = moveBot(Bot1.x1, Bot1.y1, 'left',2)
        Bot1.x1, Bot1.y1 = moveBot(Bot1.x1, Bot1.y1, 'down',2)
        circPath('right wheel',3,theta[b])
        b += 1 
        if b >= len(theta):   
            b = 0  
        circPath('left wheel',3,theta[c])
        c += 1 
        if c >= len(theta):   
            c = 0  
    elif 58000 < time < 60000:
        circPath('right wheel',10,theta[b])
        b += 1 
        if b >= len(theta):   
            b = 0  
        circPath('left wheel',10,theta[c])
        c += 1 
        if c >= len(theta):   
            c = 0  
    elif 60000  < time <= 60250:
        circPath('head',9,theta[e])
        e += 1 
        if e >= len(theta):   
            e = 0  
        circPath('right wheel',9,theta[b])
        b += 1 
        if b >= len(theta):   
            b = 0  
        circPath('left wheel',9,theta[c])
        c += 1 
        if c >= len(theta):   
            c = 0  
    elif 60250  < time <= 60500:
        circPath('head',8,theta[e])
        e += 1 
        if e >= len(theta):   
            e = 0  
        circPath('right wheel',8,theta[b])
        b += 1 
        if b >= len(theta):   
            b = 0  
        circPath('left wheel',8,theta[c])
        c += 1 
        if c >= len(theta):   
            c = 0  
    elif 60500  < time <= 60750:
        circPath('head',7,theta[e])
        e += 1 
        if e >= len(theta):   
            e = 0
        circPath('right wheel',7,theta[b])
        b += 1 
        if b >= len(theta):   
            b = 0  
        circPath('left wheel',7,theta[c])
        c += 1 
        if c >= len(theta):   
            c = 0  
    elif 60750  < time <= 61000:
        circPath('head',6,theta[e])
        e += 1 
        if e >= len(theta):   
            e = 0
        circPath('right wheel',6,theta[b])
        b += 1 
        if b >= len(theta):   
            b = 0  
        circPath('left wheel',6,theta[c])
        c += 1 
        if c >= len(theta):   
            c = 0  
    elif 61000  < time <= 61250:
        circPath('head',5,theta[e])
        e += 1 
        if e >= len(theta):   
            e = 0
        circPath('right wheel',5,theta[b])
        b += 1 
        if b >= len(theta):   
            b = 0  
        circPath('left wheel',5,theta[c])
        c += 1 
        if c >= len(theta):   
            c = 0  
    elif 61250  < time <= 61500:
        circPath('head',4,theta[e])
        e += 1 
        if e >= len(theta):   
            e = 0
        circPath('right wheel',4,theta[b])
        b += 1 
        if b >= len(theta):   
            b = 0  
        circPath('left wheel',4,theta[c])
        c += 1 
        if c >= len(theta):   
            c = 0  
    elif 61500  < time <= 61750:
        circPath('head',3,theta[e])
        e += 1 
        if e >= len(theta):   
            e = 0
        circPath('right wheel',3,theta[b])
        b += 1 
        if b >= len(theta):   
            b = 0  
        circPath('left wheel',3,theta[c])
        c += 1 
        if c >= len(theta):   
            c = 0  
    elif 61750  < time <= 62000:
        circPath('head',2,theta[e])
        e += 1 
        if e >= len(theta):   
            e = 0
        circPath('right wheel',2,theta[b])
        b += 1 
        if b >= len(theta):   
            b = 0  
        circPath('left wheel',2,theta[c])
        c += 1 
        if c >= len(theta):   
            c = 0  
    elif 62000 < time <= 64000: 
            bodyGrow(.5)
    elif 64000 < time <= 72000: 
        Bot1.x1, Bot1.y1 = moveBot(Bot1.x1, Bot1.y1, 'right',2.5)
        circPath('right wheel',1,theta[b])
        circPath('left wheel',1,theta[b])
        b += 1 
        if b >= len(theta):   
            b = 0  
    elif time > 72000:
        Run = False



    Bot1.makeBot() #draws bot 

    
    
    pygame.display.update() #updates display 



            

#pauses music and quits once we exit while loop
pygame.mixer.music.pause() 
pygame.quit() 


