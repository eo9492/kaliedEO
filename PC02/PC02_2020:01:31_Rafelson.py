"""
PC02- Tails Chasing Tail Trails...
E.O Rafelson
02/05/2020
Code animates a turtle dance using python




#works cited

#this is the website where I got all of the color names from
#https://ecsdtech.com/8-pages/121-python-turtle-colors source of colors
#this is where I got my backround image
#https://wallpaperaccess.com/beautiful-lake


"""
from turtle import * #gets my turlte stuff
from time import sleep

#Cool color lists used to create 'boy turtle'
boyColors=('midnight blue', 'Medium Blue', 'Blue', 'Dodger Blue', 'Deep Sky Blue', 'Cyan', 
'Dark Turquoise',	 'Medium Turquoise', 'Turquoise', 'Medium Aquamarine',	 
'Aquamarine', 'Dark Sea Green', 'Sea Green',	 'Medium Sea Green', 'Light Sea Green',	 
'Pale Green',	 'Spring Green', 'Lawn Green')

#Cool color lists used to create 'girl turtle'
girlColors=['Dark Salmon', 'Salmon', 'Light Salmon','Orange','Dark Orange','Coral','Light Coral' ,'Tomato',
'Orange Red','Red','Hot Pink','Deep Pink' ,'Pink','Light Pink',
'Pale Violet Red' ,'Maroon','Medium Violet Red','Violet Red']

#Color lists used to create 'baby turtle at end'
babyColors= ['red','pink','magenta','violet','blue','light blue','cyan',
'aquamarine','green','light green','yellow','orange','white']

fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,] #fibinacci sequence used in exit spiral 

#imports image for screen 
lake = Screen()
lake.bgpic('lake.gif')
lake.update

boy = Turtle()
boy.shape('turtle')

girl = Turtle()
girl.shape('turtle')

baby = Turtle()
baby.shape('turtle')
baby.up()
baby.left(90)
baby.goto(0,600)


boy.up()
boy.shapesize(.2)
boy.goto(250,-150)
boy.color('blue')
boy.left(180 )

girl.up()
girl.shapesize(.2)
girl.goto(-250,-150)
girl.color('pink')

boy.speed(0)
girl.speed(0)
baby.speed(0)



 #creates loop that allowed me to make alterations to turtle's path's every 10 frames.
 #procedes to make hypnotizing trails as turtles move, stamp, and loop.
 #features a fibonacci sequence spiral at the end. 
 #best enjoyed listening to psychedelic music of your choice, I'd recomend some deep house, pink floyd, or downtempo tipper :)
 
 
for i in range (250):   
    if 10> i >= 0 :        
        boy.speed(6)
        girl.speed(6)
        boy.color(boyColors[0])
        girl.color(girlColors[0])
        boy.shapesize(1) 
        girl.shapesize(1)
        boy.forward(5)
        girl.forward(5)
        boy.right(2)
        girl.left(2)
        boy.stamp()
        girl.stamp()
    elif 20> i >= 10:
        boy.speed(9)
        girl.speed(9)
        boy.color(boyColors[1])
        girl.color(girlColors[1])
        boy.shapesize(1.5)
        girl.shapesize(1.5)
        boy.forward(7)
        girl.forward(7)
        boy.right(5)
        girl.left(5)
        boy.stamp()
        girl.stamp()
    elif 30> i >= 20:
        boy.speed(0)
        girl.speed(0)
        boy.color(boyColors[2])
        girl.color(girlColors[2])
        boy.shapesize(2)
        girl.shapesize(2)
        boy.forward(10)
        girl.forward(10)
        boy.right(8)
        girl.left(8)
        boy.stamp()
        girl.stamp()
    elif 40> i >= 30:
        boy.color(boyColors[3])
        girl.color(girlColors[3])
        boy.shapesize(2.5)
        girl.shapesize(2.5)
        boy.forward(10)
        girl.forward(10)
        boy.left(10)
        girl.right(10)
        boy.stamp()
        girl.stamp()
    elif 50> i >= 40:
        boy.color(boyColors[4])
        girl.color(girlColors[4])
        boy.shapesize(2.5)
        girl.shapesize(2.5)
        boy.forward(15)
        girl.forward(15)
        boy.right(36)
        girl.left(36)
        boy.stamp()
        girl.stamp()
    elif 60> i >= 50:
        boy.color(boyColors[5])
        girl.color(girlColors[5])
        boy.shapesize(3)
        girl.shapesize(3)
        boy.forward(10)
        girl.forward(10)
        boy.left(10)
        girl.right(10)
        boy.stamp()
        girl.stamp()
    elif 70> i >= 60:
        boy.color(boyColors[6])
        girl.color(girlColors[6])
        boy.shapesize(3.2)
        girl.shapesize(3.2)
        boy.forward(10)
        girl.forward(10)
        boy.left(4)
        girl.right(4)
        boy.stamp()
        girl.stamp()
    elif 80> i >= 70:
        boy.color(boyColors[7])
        girl.color(girlColors[7])
        boy.shapesize(3.5)
        girl.shapesize(3.5)
        boy.forward(10)
        girl.forward(10)
        boy.right(10)
        girl.left(10)
        boy.stamp()
        girl.stamp()
    elif 90> i >= 80:
        boy.color(boyColors[8])
        girl.color(girlColors[8])
        boy.shapesize(4)
        girl.shapesize(4)
        boy.forward(fib[4])
        girl.forward(fib[4])
        boy.left(18)
        girl.left(18)
        boy.stamp()
        girl.stamp()
        sleep(.1)
    elif 100> i >= 90:
        boy.color(boyColors[9])
        girl.color(girlColors[9])
        boy.shapesize(4)
        girl.shapesize(4)
        boy.forward(fib[5])
        girl.forward(fib[5])
        boy.left(18)
        girl.left(18)
        boy.stamp()
        girl.stamp()
        sleep(.05)
    elif 110> i >= 100:
        boy.color(boyColors[10])
        girl.color(girlColors[-10])
        boy.shapesize(4)
        girl.shapesize(4)
        boy.forward(fib[6])
        girl.forward(fib[6])
        boy.left(18)
        girl.left(18)
        boy.stamp()
        girl.stamp()
    elif 120> i >= 110:
        boy.color(boyColors[11])
        girl.color(girlColors[11])
        boy.shapesize(4)
        girl.shapesize(4)
        boy.forward(fib[7])
        girl.forward(fib[7])
        boy.left(18)
        girl.left(18)
        boy.stamp()
        girl.stamp()
        baby.left(18)
        baby.goto(0,-60)
        baby.shapesize(.5)
        baby.color(babyColors[0])
    elif 130> i >= 120:
        boy.color(boyColors[12])
        girl.color(girlColors[12])
        boy.shapesize(4)
        girl.shapesize(4)
        boy.forward(fib[8])
        girl.forward(fib[8])
        boy.left(18)
        girl.left(18)
        boy.stamp()
        girl.stamp()
        baby.left(18)
        baby.shapesize(1)
        baby.color(babyColors[1])
    elif 140> i >= 130:
        boy.color(boyColors[13])
        girl.color(girlColors[13])
        boy.shapesize(4)
        girl.shapesize(4)
        boy.forward(fib[9])
        girl.forward(fib[9])
        boy.left(18)
        girl.left(18)
        boy.stamp()
        girl.stamp()
        baby.left(18)
        baby.shapesize(1.5)
        baby.color(babyColors[2])
    elif 150> i >= 140:
        boy.color(boyColors[14])
        girl.color(girlColors[14])
        boy.shapesize(4)
        girl.shapesize(4)
        boy.forward(fib[10])
        girl.forward(fib[10])
        boy.left(18)
        girl.left(18)
        boy.stamp()
        girl.stamp()
        baby.left(18)
        baby.shapesize(2)
        baby.color(babyColors[3])
    elif 160> i >= 150:
        boy.color(boyColors[15])
        girl.color(girlColors[15])
        boy.shapesize(4)
        girl.shapesize(4)
        boy.forward(fib[11])
        girl.forward(fib[11])
        boy.left(18)
        girl.left(18)
        boy.stamp()
        girl.stamp()
        baby.left(18)
        baby.shapesize(2.5)
        baby.color(babyColors[4])
    elif 170> i >= 160:
        boy.color(boyColors[16])
        girl.color(girlColors[16])
        boy.shapesize(4)
        girl.shapesize(4)
        boy.forward(fib[12])
        girl.forward(fib[12])
        boy.left(18)
        girl.left(18)
        boy.stamp()
        girl.stamp()
        baby.left(18)
        baby.shapesize(3)
        baby.color(babyColors[5])
    elif 180> i >= 170:
        baby.left(18)
        baby.shapesize(3.5)
        baby.color(babyColors[6])
    elif 190> i >= 180:
        baby.left(18)
        baby.shapesize(4)
        baby.color(babyColors[7])
    elif 200> i >= 190:
        baby.left(18)
        baby.shapesize(4.5)
        baby.color(babyColors[8])
    elif 210> i >= 200:
        baby.left(18)
        baby.shapesize(5)
        baby.color(babyColors[9])
    elif 220> i >= 210:
        baby.left(18)
        baby.shapesize(7)
        baby.color(babyColors[10])
    elif 230> i >= 220:
        baby.left(18)
        baby.shapesize(9)
        baby.color(babyColors[11])
    elif 240> i >= 230:
        baby.left(18)
        baby.shapesize(10)
        baby.color(babyColors[12])
        sleep(.2)
     
        
    

done()





