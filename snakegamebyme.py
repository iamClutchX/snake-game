import turtle   #turtle is pre installed python library that enables user to create picture and shape by providing them in virtual cnavas/screen
import random
import time

delay=0.1 #time k sleep function mai as an argument pass hoga that' produce a gap
score=0
highscore=0

#snakebodies
bodies=[]   #snake k body as a list treat

#getting a screen 

s=turtle.Screen()
s.title("Snake Game")    #title
s.bgcolor("gray")
s.setup(width=600,height=600)  #screen ki size decide

#snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square") #snake shape
head.color("white")  #for border color
head.fillcolor("red")   #snake inner color
head.penup() #so we can move snake without leaving track
head.goto(0,0)
head.direction="stop"

#snake food
food=turtle.Turtle()
food.shape("square")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.ht()  #snake turtle invisible full form- HIDE TURTLE
food.goto(0,200)
food.st()  #show turtle food ye nhi to food nhi dihega after if ht() use

#score board
sb=turtle.Turtle()
sb.shape("circle")
sb.fillcolor("red")
sb.penup()
sb.ht()
sb.goto(-250,-250)
sb.write("score:0 | high score: 0")

def moveup():
   if head.direction!="down":
       head.direction="up"
def movedown():       
   if head.direction!="up":
       head.direction="down"
def moveleft():       
   if head.direction!="right":
    head.direction="left"
def moveright():    
   if head.direction!="left":
       head.direction="right"

def movestop():
    head.direction="stop"
def move():
    if head.direction=="up":
        y=head.ycor()  #ycor=y-coordinate snake ke head coordinate ki postion ko get 
        head.sety(y+20)   #if up arrow chose then increment in y by 20
    
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    

#which operation should perform by which key or EVENT HANDLING- KEY MAPPING

s.listen()
s.onkey(moveup,"Up")
s.onkey(movedown,"Down")
s.onkey(moveleft,"Left")
s.onkey(moveright,"Right")
s.onkey(movestop,"space")

#main loop
while True:
   s.update()
   #this is to update to screen   
#chech collision with border
   if head.xcor()>290:
      head.setx(-290)
   if head.xcor()<-290:
      head.setx(290)
   if head.ycor()>290:
      head.sety(-290)
   if head.ycor()<-290:
      head.sety(290)         


#check collision food
   if head.distance(food)<20:
       #move the food to new random place  
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        #to increase length  of snake
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("circle") 
        body.color("red")
        body.fillcolor("black")
        bodies.append(body)  #append new body or add new item in your list
        #increase the score
        score+=10
        delay-=0.001  #delay decrease it means speed increases
        #update the high score
        if score>highscore:
          highscore=score
        sb.clear()
        sb.write(f"score: {score} high score: {highscore}")  

#move snake bodies (agar ye code nhi likhe to body sath mai na move kr ke kewal centre pe rahege)
   for index in range(len(bodies)-1,0,-1):
    x=bodies[index-1].xcor()
    y=bodies[index-1].ycor()
    bodies[index].goto(x,y)


   if len(bodies)>0:
      x=head.xcor()
      y=head.ycor()
      bodies[0].goto(x,y)
   move()



#check collison with snakebody
   for body  in bodies:
     if body.distance(head)<20:
         time.sleep(0.1)
         head.goto(0,0)
         head.direction="stop"
      #hide bodies
         for body in bodies:
            body.ht()
         bodies.clear()
         score=0
         delay=0.1  
      #update score board
         sb.clear()
         sb.write("Score: {} high score: {}".format(score,highscore))  
   time.sleep(delay)  #itne duration ka gap har bar aaye


s.mainloop() #event hNDILIN WALA har bar call




