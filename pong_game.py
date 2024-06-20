from turtle import Screen
from paddle import Paddle, Ball, Scoreboard
import time    

scr = Screen()
scr.setup(width=900, height=600)
scr.bgcolor("black")
scr.title("PONG GAME")
scr.tracer(0)

first_bar = Paddle((430, 0))
second_bar = Paddle((-430, 0))
ball = Ball()

scoreboard = Scoreboard()

scr.listen()
scr.onkeypress(first_bar.uppp, "Up")
scr.onkeypress(first_bar.downnnn, "Down")
scr.onkeypress(second_bar.uppp, "w")
scr.onkeypress(second_bar.downnnn, "s")

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    scr.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 450:
        scoreboard.increase_score_left()
        ball.reset_position()

    if ball.xcor() < -450: 
        scoreboard.increase_score_right()
        ball.reset_position()

    if (ball.distance(first_bar) < 50 and ball.xcor() > 320) or (ball.distance(second_bar) < 50 and ball.xcor() < -320):
        ball.bounce_x()

scr.mainloop()
