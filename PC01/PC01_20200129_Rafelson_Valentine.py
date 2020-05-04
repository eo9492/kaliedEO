
"""
PC01-turtleSwag
E.O. Rafelson, Gabriel Valentine
01/24/2020
Code Draws a sexy boi a nice mom tat and heart eye emoji Xtreme in turtle

#image taken from website https://www.menshealth.com/uk/building-muscle/a755394/10-quick-steps-how-to-get-big-biceps-fast/
"""
from turtle import * #gets my turlte library


#creates backround
bicep = Screen() 
bicep.bgpic("Bicep.gif") 
bicep.update() 

#creates turtle
needle = Turtle()



#draws red heart on arm
needle.up()
needle.goto(-20,-150)
needle.down()
needle.color("black", "red")
needle.begin_fill()
needle.left(45)
needle.forward(150)
needle.left(20)
needle.circle(31,180)
needle.right(170)
needle.circle(31,180)
needle.left(20)
needle.forward(150)
needle.end_fill()
needle.up()

#letter M
needle.goto(20,20)
needle.down()
needle.left(90)
needle.color('black')
needle.up()
needle.right(125)
needle.forward(85)
needle.left(90)
needle.forward(3)
needle.right(97)


needle.down()
needle.right(180)
needle.forward(35)
needle.right(165)
needle.forward(20)
needle.left(165)
needle.forward(20)
needle.right(165)
needle.forward(35)
needle.up()

needle.left(90)
needle.forward(18)

#Letter O
needle.down()
needle.circle(15)

needle.up()
needle.forward(17)
needle.right(100)
#Letter M
needle.down()
needle.right(180)
needle.forward(35)
needle.right(165)
needle.forward(20)
needle.left(165)
needle.forward(20)
needle.right(165)
needle.forward(35)
needle.up()





#arrow
needle.goto(0,0)
needle.left(115)
needle.up()
needle.right(135)
needle.forward(70)
needle.down()
needle.left(90)

needle.backward(15)

needle.right(20)
needle.backward(10)
needle.forward(10)
needle.left(40)
needle.backward(10)
needle.forward(10)
needle.right(20)
needle.forward(7)
needle.right(20)
needle.backward(15)
needle.forward(15)
needle.left(40)
needle.backward(15)
needle.forward(15)
needle.right(20)
needle.forward(7)
needle.right(20)
needle.backward(15)
needle.forward(15)
needle.left(40)
needle.backward(15)
needle.forward(15)
needle.right(20)
needle.forward(7)
needle.right(20)
needle.backward(15)
needle.forward(15)
needle.left(40)
needle.backward(15)
needle.forward(15)
needle.right(20)
needle.forward(7)
needle.right(20)
needle.backward(15)
needle.forward(15)
needle.left(40)
needle.backward(15)
needle.forward(15)
needle.right(20)
needle.forward(27)

needle.up()
needle.forward(44)
needle.down()
needle.forward(25)
needle.right(160)
needle.forward(15)
needle.backward(15)
needle.left(320)
needle.forward(15)
needle.backward(15)
needle.left(60)

#head

needle.up()
needle.goto(-8,158)
needle.right(93)
needle.down()
needle.begin_fill()
needle.forward(40)
needle.circle(61,180)
needle.forward(40)
needle.left(90)
needle.forward(122)
needle.end_fill()

#heart eye emoji #Xtrme 

needle.up()
needle.goto(-42,188)
needle.down()
needle.color('black','red')
needle.begin_fill()
needle.left(65)
needle.forward(40)
needle.left(20)
needle.circle(9,180)
needle.right(170)
needle.circle(9,180)
needle.left(20)
needle.forward(40)
needle.end_fill()


needle.up()
needle.goto(-95,188)
needle.left(65)
needle.down()
needle.color('black','red')
needle.begin_fill()
needle.left(65)
needle.forward(40)
needle.left(20)
needle.circle(9,180)
needle.right(170)
needle.circle(9,180)
needle.left(20)
needle.forward(40)
needle.end_fill()


needle.up()
needle.goto(-42,193)
needle.left(65)
needle.down()
needle.color('red','black')
needle.begin_fill()
needle.left(65)
needle.forward(30)
needle.left(20)
needle.circle(6,180)
needle.right(170)
needle.circle(6,180)
needle.left(20)
needle.forward(30)
needle.end_fill()

needle.up()
needle.goto(-95,193)
needle.left(65)
needle.down()
needle.color('red','black')
needle.begin_fill()
needle.left(65)
needle.forward(30)
needle.left(20)
needle.circle(6,180)
needle.right(170)
needle.circle(6,180)
needle.left(20)
needle.forward(30)
needle.end_fill()

needle.up()
needle.goto(-40,202)
needle.left(65)
needle.down()
needle.color('black','red')
needle.begin_fill()
needle.left(65)
needle.forward(15)
needle.left(20)
needle.circle(3,180)
needle.right(170)
needle.circle(3,180)
needle.left(20)
needle.forward(15)
needle.end_fill()

needle.up()
needle.goto(-94,202)
needle.left(65)
needle.down()
needle.color('black','red')
needle.begin_fill()
needle.left(65)
needle.forward(15)
needle.left(20)
needle.circle(3,180)
needle.right(170)
needle.circle(3,180)
needle.left(20)
needle.forward(15)
needle.end_fill()



#Gets rid of obnoxious needle on my dudes tat

needle.up()
needle.goto(1000,1000)

done()












