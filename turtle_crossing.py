from turtle import Turtle, Screen
import random
from bars import Bar,Scoreboard
import time

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("white")
scr.title("TURTLE CROSSING GAME")
scr.tracer(0)

tim = Turtle()
tim.shape("turtle")
tim.color("black")
tim.penup()
tim.left(90)
tim.goto(0,-280)


scoreboard = Scoreboard()

def uppp():
    tim.forward(10)


scr.listen()
scr.onkeypress(uppp, "Up")
barrr = Bar()

is_ggg = True

speed_increase = 0.1

while is_ggg:
    time.sleep(speed_increase)
    scr.update()
    barrr.create()
    barrr.moving()


    if tim.ycor() > 280:
        scoreboard.increase()
        tim.setposition(0,-280)
        speed_increase -=0.01
        time.sleep(speed_increase)
        

    for eacg in barrr.all_bars:
        if eacg.distance(tim) < 20:
            tim.setposition(0,-280)
            scoreboard.drrr()
            speed_increase = 0.1
            time.sleep(speed_increase)
            

scr.exitonclick()