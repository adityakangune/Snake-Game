#Creating A window
import turtle
import time
import random
delay=0.1 #seconds

#Score
score = 0
high_score = 0


#Set up the Screen
wn = turtle.Screen()
wn.title("Snake Game by Adi")
wn.bgcolor("blue")
wn.setup(width=600, height=600) #Pixels
wn.tracer(0) #turns off the animation on screen/turns off the screen object

#Creating a snake head and moving it
head = turtle.Turtle()
head.speed(0) #Animation speed of the turtle module and maximum speed is zero
head.shape("square")
head .color("yellow")
head.penup() #Turtle module is used to draw,We did this so that it does not draw anything
head.goto(0,0) #so that it starts at centre
head.direction = "stop" #so that when it starts it will sit there in the middle with head up

#Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food .color("red")
food.penup()
food.goto(0,100)

# increasing the snake body
segments = []

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score = 0  Highscore  = 0" , align="center",font=("Courier",24,"normal"))



#Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "down":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"
def move():
    if head.direction == "up":
        y=head.ycor()
        head.sety(y + 20) #So if head is up then it will move 20 coordinates up

    if head.direction == "down":
        y=head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x=head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x=head.xcor()
        head.setx(x + 20)

#Keyboard Bindings

wn.listen()
wn.onkeypress(go_up , "w")
wn.onkeypress(go_down , "s")
wn.onkeypress(go_left , "a")
wn.onkeypress(go_right , "d")
#Main Game loop
while True:
    wn.update() #so everytime the screen gets updated

    #Check for a collision of head with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1) #Pause the game for a second
        head.goto(0, 0)
        head.direction = "stop"
        #Hide the segments due to collision
        for segment in segments:
            segment.goto(1000, 1000) #We are just sending the segments away from screen
        #Clear the segments
        segments = []

        #Reset the Score
        score = 0
        pen.clear()
        pen.write("Score= {}  Highscore= {}".format(score, high_score), align="center",font=("Courier",24,"normal"))

#Check for a collision with the food
    if head.distance(food) < 20:
        #move the food to a random spot on the screen
        x=random.randint(-290, 290)#Because sccreen is divided in 300 half of the x and y diretion i.i. 600/2
        y = random.randint(-290, 290)
        food.goto(x, y)
        #Add a segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("pink")
        new_segment.penup()
        segments.append(new_segment)

        #Increase the Score
        score+=10
        if score>high_score:
            high_score=score
        pen.clear()
        pen.write("Score= {}  Highscore= {}".format(score, high_score), align="center",font=("Courier",24,"normal"))

    #Move the end segments first in reverse order
    for index in range(len(segments)-1,0,-1):#will work only when there more then 1 segments
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x, y)

    #Move the segment zero to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)


    move()

    #Check for head collisions with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            #Hide the segments due to collision
            for segment in segments:
                segment.goto(1000, 1000) #We are just sending the segments away from screen
            #Clear the segments
            segments = []



    time.sleep(delay) #stops the program by 0.1 seconds


wn.mainloop()