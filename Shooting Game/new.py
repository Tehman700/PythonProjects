from turtle import Turtle, Screen
import random
import time
from new_class import Car, Scoreboard

scr = Screen()
scr.setup(width=900, height=600)
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
barrr = Car()

is_ggg = True

speed_increase = 0.1

while is_ggg:
    time.sleep(speed_increase)
    scr.update()
    barrr.create()
    barrr.moving(10)  #


    # if tim.ycor() > 280:
    #     tim.setposition(0,-280)
    #     speed_increase -=0.01
    #     time.sleep(speed_increase)
        

    # for eacg in barrr.all_cars:
    #     if eacg.distance(tim) < 20:
    #         tim.setposition(0,-280)
    #         speed_increase = 0.1
    #         time.sleep(speed_increase)
        
        
    

scr.exitonclick()