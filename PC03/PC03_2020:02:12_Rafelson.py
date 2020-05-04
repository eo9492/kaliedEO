
"""
PC03- Flower children 
E.O. Rafelson
02/12/2020
Code draws 7 random spirograph flowers 


# spirograph code modified from in-class script created by Dr. Z, 2/6/2020
Link: https://cdn.inst-fs-iad-prod.inscloudgate.net/ca471bdf-f2ca-4d74-8c2b-32ea8e59a91b/spirograph.py?token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6ImNkbiJ9.eyJyZXNvdXJjZSI6Ii9jYTQ3MWJkZi1mMmNhLTRkNzQtOGMyYi0zMmVhOGU1OWE5MWIvc3Bpcm9ncmFwaC5weSIsInRlbmFudCI6ImNhbnZhcyIsInVzZXJfaWQiOiIxMDc3MjAwMDAwMDAzNDA0MDYiLCJpYXQiOjE1ODg1NTc4MTMsImV4cCI6MTU4ODY0NDIxM30.OacimKCOHtTeMv1hKlBPtmsMLDtRA5JOkLthJTe1qUJwDgM6B2KXj8h6bFn15N8y_SiFP0yhm2YuTzMwxYnYyA&content_type=text%2Fx-python-script
# animation may take a while, so please be patient! ha. 
#not all flowers are created equal, so dont judge the less pretty ones... they have feelings too.

"""

#imports librarys 


from turtle import * 
import numpy as np
from random import *



#recaman sequence used in roots of each flower list taken from wikipedia https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence
rec=[0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22, 10, 23, 9, 24, 8, 25, 43, 62, 42, 63, 41, 18, 42, 17, 43, 16, 44, 15, 45, 14, 46, 79,]
reclength = len(rec)
bg = Screen()
bg.screensize(1000,1000) #makes big screen! please expand or you wont be able to see it all! 
bg.clear()
bg.bgcolor('black')


#creates turtle 
pen= Turtle(visible=False)
pen.width(3)
pen.speed(0)
pen.right(90)
pen.up()





#used for spirograph 
circNum= 22 
theta = np.linspace(0, circNum*2*np.pi, 1000) 


warmColors=['Dark Salmon', 'Salmon', 'Light Salmon','Orange','Dark Orange','Coral','Light Coral' ,'Tomato',
'Orange Red','Red','Hot Pink','Deep Pink' ,'Pink','Light Pink',
'Pale Violet Red' ,'Maroon','Medium Violet Red','Violet Red']


coolColors=('midnight blue', 'Medium Blue', 'Blue', 'Dodger Blue', 'Deep Sky Blue', 'Cyan', 
'Dark Turquoise',	 'Medium Turquoise', 'Turquoise', 'Medium Aquamarine',	 
'Aquamarine', 'Dark Sea Green', 'Sea Green',	 'Medium Sea Green', 'Light Sea Green',	 
'Pale Green',	 'Spring Green', 'Lawn Green')

even = (0,2,4,6) #used to help alternate color paterns 


for loop in range(7):   #main loop that contains all my code 
    if loop == 0:     #starting position 
        pen.width(3)
        R = randint(100, 150)  #   notice that R, r, and d are contained in loop so they switch for every new spiro graph
        r = randint(50, 100)
        d = randint(60, 100)
        off_x= -450
        off_y= -250
        pen.up()
        xs= off_x+ (R-r)*np.cos(theta[0]) + d*np.cos(((R-r)/r)*theta[0])
        ys= off_y+ (R-r)*np.sin(theta[0]) - d*np.sin(((R-r)/r)*theta[0])
        pen.goto(xs,ys)
        pen.down()
        pen.begin_fill()
    elif loop == 1 or loop == 2 or loop == 3: #same as above, but moves new spirograph up 150 and right 150 
        pen.width(3)
        R = randint(100, 150)
        r = randint(50, 100)
        d = randint(60, 100)
        off_x += 150
        off_y += 150
        pen.up()
        xs= off_x+ (R-r)*np.cos(theta[0]) + d*np.cos(((R-r)/r)*theta[0])
        ys= off_y+ (R-r)*np.sin(theta[0]) - d*np.sin(((R-r)/r)*theta[0])
        pen.goto(xs,ys)
        pen.down()
        pen.begin_fill()
    else:               #same as above, but moves new spirograph *DOWN* 150 and right 150, creating a nice pyramid of spirograph flowers 
        pen.width(3)
        R = randint(100, 150)
        r = randint(50, 100)
        d = randint(60, 100)
        off_x += 150
        off_y -=150
        pen.up()
        xs= off_x+ (R-r)*np.cos(theta[0]) + d*np.cos(((R-r)/r)*theta[0])
        ys= off_y+ (R-r)*np.sin(theta[0]) - d*np.sin(((R-r)/r)*theta[0])
        pen.goto(xs,ys)
        pen.down()
        pen.begin_fill()
        
    if loop in even: #these two loops draw each spirograph, the only difference between them is that they alternate color patterns
        for t in range(len(theta)):  #so that it either outlines in random warm colors and fills in random cool color, or vice versa 
            x= off_x+ (R-r)*np.cos(theta[t]) + d*np.cos(((R-r)/r)*theta[t])
            y=  off_y+ (R-r)*np.sin(theta[t]) - d*np.sin(((R-r)/r)*theta[t])
            pen.color(warmColors[randint(0,17)], coolColors[randint(0,17)])
            pen.goto(x,y)  
    else: 
        for t in range(len(theta)):
            x= off_x+ (R-r)*np.cos(theta[t]) + d*np.cos(((R-r)/r)*theta[t])
            y=  off_y+ (R-r)*np.sin(theta[t]) - d*np.sin(((R-r)/r)*theta[t])
            pen.color(coolColors[randint(0,17)], warmColors[randint(0,17)])
            pen.goto(x,y)  
        
    pen.end_fill()   #draws "flower" stem and roots 
    pen.color('green')
    pen.width(10)
    pen.up()
    pen.goto(off_x, off_y)
    pen.down()
    pen.forward(222)
    for i in range(reclength): #utilizes recaman sequence for lengths of roots, hope this counts lol! 
        pen.width(1)
        branch = rec[i]
        turn = randint(0,60) #random turn for each loop to create different roots every time
        pen.right(turn)
        pen.forward(branch*1.5)
        pen.backward(branch*1.5)
        pen.left(turn*2)
        pen.forward(branch*1.5)
        pen.backward(branch*1.5)
        pen.right(turn)
    pen.backward(222)
        
    
        

