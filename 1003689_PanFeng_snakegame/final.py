# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 00:13:10 2020

@author: Adler
"""

import turtle
import random
import time
import winsound

number_of_player = int(input("1 or 2 player?:"))
delay = 0.1
score = 0
high_score = 0
score2 = 0
screensize_x = 600
screensize_y = 600
x_max = (screensize_x-20)/2
y_max = (screensize_y-20)/2

#setting up the screen of the game
screen = turtle.Screen()
screen.setup(width=screensize_x, height =screensize_y , startx = None, starty = None)
screen.title("SNAKE by Adler")
screen.bgcolor("black")
screen.tracer(0)

class a_dot(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("square")
        self.speed(0)
        self.direction = "stop"
        self.color("white")
        
#give a random coordiante on screen        
def random_coordiante():
    x = random.randint(-(screensize_x-30)/2 , (screensize_x-30)/2)
    y = random.randint(-(screensize_y-30)/2 , (screensize_y-30)/2)
    return x, y

#setting up the snake head
snakehead = a_dot()
snakehead.color("green")
if number_of_player == 2:
    snakehead2 = a_dot()
    snakehead2.color("blue")

#setting up the snake head 
snakehead.goto(0,0)
if number_of_player == 2:
    snakehead.goto(-100,0)
    snakehead2.goto(100,0)

#first snake food 
snakefood = a_dot() 
snakefood.shape("circle")   
snakefood.goto(random_coordiante())

#a list that stores the bodyparts of the snake
body = []
body2 = []

def move_body(snakehead, body):
    #body goes to the position of the body infront of it    
    for i in range(len(body)-1 , 0 ,-1):
        x = body[ i -1].xcor()
        y = body[ i -1].ycor()
        body[i].goto(x, y)
    if len(body) > 0:
        x = snakehead.xcor()
        y = snakehead.ycor()
        body[0].goto(x,y)

#list of color for turtle to change color
listofcolors= ["yellow","gold","orange","red","maroon","violet", "magenta","purple","navy","blue","cyan","lightgreen","green","darkgreen","chocolate"]

#set up a pen that writes the score
pen = a_dot()
pen.goto(0, (screensize_y/2)-40 )
pen.hideturtle()

#update score
def score_update():
    global high_score
    if number_of_player ==1:
        pen.clear()    #clear off the text on the screen
        if score>high_score:  #update high score variable
            high_score = score
        pen.write("Score:{:4}   High Score:{:4}".format(score,high_score), align="center", font=("Arial", 24, "normal")) 
    else:
        pen.clear()
        if score > high_score :
            high_score = score
        elif score2 > high_score:
            high_score = score2
        pen.write("P1:{:4}  P2:{:4}  High Score:{:4}".format(score,score2,high_score), align="center", font=("Arial", 24, "normal")) 

#change the direction of the snake
def move_up():
    if snakehead.direction != "down":
        snakehead.direction = "up"

def move_down():
    if snakehead.direction != "up":
        snakehead.direction = "down"

def move_left():
    if snakehead.direction != "right":
        snakehead.direction = "left"

def move_right():
    if snakehead.direction != "left":
        snakehead.direction = "right"

def move_up2():
    if snakehead2.direction != "down":
        snakehead2.direction = "up"

def move_down2():
    if snakehead2.direction != "up":
        snakehead2.direction = "down"

def move_left2():
    if snakehead2.direction != "right":
        snakehead2.direction = "left"

def move_right2():
    if snakehead2.direction != "left":
        snakehead2.direction = "right"        
        


#change color of snake body to that of snakehead
def change_color():
    snakehead.color(random.choice(listofcolors))
    for i in body:
        i.color(snakehead.color()[0])

def change_color2():
    snakehead2.color(random.choice(listofcolors))
    for i in body2:
        i.color(snakehead2.color()[0])

#Let the snake move in the given direction
def move(x):
    if x.direction == "up":
        x.sety(x.ycor() + 20)
        
    if x.direction == "down":
        x.sety(x.ycor() - 20)        
        
    if x.direction == "left":
        x.setx(x.xcor() - 20)        
        
    if x.direction == "right":
        x.setx(x.xcor() + 20)    
 
#clear all the bodyparts of the snake
def reset(snakehead,body,snake = 1 ):
    snakehead.goto(0,0)
    snakehead.direction = "stop"
    for i in body:
        i.hideturtle()
    body.clear()
    global delay,score,score2
    if snake == 1:
        score = 0
    if snake == 2:
        score2 = 0
    score_update()
    delay = 0.1

def check_death():
    if number_of_player ==1:
        #check for collision with wall
        if snakehead.xcor() < -x_max or snakehead.xcor() > x_max or snakehead.ycor() < -y_max or snakehead.ycor() > y_max:
            winsound.PlaySound("die.wav", winsound.SND_ASYNC) 
            reset(snakehead,body,snake=1)

        #check for collision with body
        for i in body:
            if i.distance(snakehead)<20:
                winsound.PlaySound("die.wav", winsound.SND_ASYNC) 
                reset(snakehead,body,snake=1)
    else:
        #check for collision with wall
        if snakehead.xcor() < -x_max or snakehead.xcor() > x_max or snakehead.ycor() < -y_max or snakehead.ycor() > y_max:
            winsound.PlaySound("die.wav", winsound.SND_ASYNC) 
            reset(snakehead,body,snake = 1 )
        #check for collision with body
        for i in body:
            if i.distance(snakehead2)<20:
                winsound.PlaySound("die.wav", winsound.SND_ASYNC) 
                reset(snakehead2,body2,snake = 2 )

        #check for collision with wall                
        if snakehead2.xcor() < - x_max or snakehead2.xcor() > x_max or snakehead2.ycor() < -y_max or snakehead2.ycor() > y_max:
            winsound.PlaySound("die.wav", winsound.SND_ASYNC) 
            reset(snakehead2,body2,snake = 2 )
        #check for collision with body
        for i in body2:
            if i.distance(snakehead)<20:
                winsound.PlaySound("die.wav", winsound.SND_ASYNC) 
                reset(snakehead,body,snake = 1 )

#bind keyboard input to function that changes direction    
screen.listen()

screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(change_color, "c")

if number_of_player ==2:
    screen.onkeypress(move_up2, "w")
    screen.onkeypress(move_down2, "s")
    screen.onkeypress(move_left2, "a")
    screen.onkeypress(move_right2, "d")
    screen.onkeypress(change_color2, "v")

winsound.PlaySound("start.wav", winsound.SND_ASYNC )

#main game function        
while True:
    screen.update()
    score_update()
    #head hit the boundary
    check_death()

    if number_of_player == 1:            
        #snakehead eat the food, next snakefood appears.
        if snakehead.distance(snakefood)<20:
            winsound.PlaySound("eatfood.wav", winsound.SND_ASYNC) 
            snakefood.goto(random_coordiante())

            #create a newbody and append it into the list of body
            newbody = a_dot()
            
            newbody.color(snakehead.color()[0])
            body.append(newbody)
            
            #increasing the score
            score +=1
            
            #increase speed of the snake
            if delay >= 0.06:
                delay -= 0.001
            
            #clear the score
            score_update()
            
        move_body(snakehead,body)
        #snake moves        
        move(snakehead)   
        time.sleep(delay)
    else:
        #snakehead eat the food, next snakefood appears.
        if snakehead.distance(snakefood)<20:
            winsound.PlaySound("eatfood.wav", winsound.SND_ASYNC)
            snakefood.goto(random_coordiante())
    
            #create a newbody and append it into the list of body
            newbody = a_dot()
            newbody.shape("circle")
            newbody.color(snakehead.color()[0])
            body.append(newbody)
            
            #increasing the score
            score +=1
            
            #increase speed of the snake
            if delay >= 0.06:
                delay -= 0.001

            #clear the score
            score_update()
            
        #body goes to the position of the body infront of it    
        move_body(snakehead,body)
            
        #snakehead2 eat the food, next snakefood appears.
        if snakehead2.distance(snakefood)<20 :
            winsound.PlaySound("eatfood.wav", winsound.SND_ASYNC)
            snakefood.goto(random_coordiante())
    
            #create a newbody and append it into the list of body
            newbody2 = a_dot()
            newbody2.shape("circle")
            newbody2.color(snakehead2.color()[0])
            body2.append(newbody2)
            
            #increasing the score
            score2 +=1
            
            #increase speed of the snake
            if delay >= 0.06:
                delay -= 0.001

            #clear the score
            score_update()
            
        #body goes to the position of the body infront of it    
        move_body(snakehead2,body2)      
            
        #snake moves        
        move(snakehead)   
        move(snakehead2)
        time.sleep(delay)

screen.mainloop()