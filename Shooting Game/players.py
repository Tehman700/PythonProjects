import turtle
import random
import time
scr = turtle.Screen()
scr.addshape('user_shooter.gif')
scr.addshape('computer_shooter.gif')
scr.addshape('bullet.gif')
scr.addshape('car3.gif')

class Player:
    def __init__(self, shape, edges):
        self.player = turtle.Turtle()
        self.player.shape(shape)
        self.player.penup()
        self.player.goto(edges)

    def up(self):
        y = self.player.ycor()
        if y < 250:
            self.player.sety(y+20)

    def down(self):
        y = self.player.ycor()
        if y > -250:
            self.player.sety(y-20)

    def left(self):
        x = self.player.xcor()
        if x > 250:
            self.player.setx(x-20)

    def right(self):
        x = self.player.xcor()
        if x < 390:
            self.player.setx(x+20)

    def comp_right(self):
        x = self.player.xcor()
        if x < -250:
            self.player.setx(x+20)


    def comp_left(self):
        x = self.player.xcor()
        if x > -390:
            self.player.setx(x-20)


class Bullet:
    def __init__(self, position, dx, dy):
        self.bullet = turtle.Turtle()
        self.bullet.shape('bullet.gif')
        self.bullet.color("red")
        self.bullet.penup()
        self.bullet.speed(0)
        self.bullet.goto(position)
        self.dx = dx
        self.dy = dy

    def bullet_moving(self):
        x = self.bullet.xcor() + self.dx
        y = self.bullet.ycor() + self.dy
        self.bullet.goto(x, y)









class Points:
    def __init__(self):
        super().__init__()
        self.p = turtle.Turtle()

        self.p.score_computer = 0
        self.p.score_user = 0
        self.p.color("white")
        self.p.penup()
        self.p.hideturtle()
        self.update_points()
    
    def update_points(self):
        self.p.clear()
        self.p.goto(-80,250)
        self.p.write(f"Shayan:{self.p.score_computer}", align="center", font=("Courier", 22, "normal"))
        self.p.goto(80, 250)
        self.p.write(f"Tehman:{self.p.score_user}", align="center", font=("Courier", 22, "normal"))        
        self.writing_to_file()
    
    def increase_comp_score(self):
        self.p.score_computer +=1
        self.update_points()
    
    def increase_user_score(self):
        self.p.score_user +=1
        self.update_points()
    
    def decrease_comp_score(self):
        self.p.score_computer -=1
        self.update_points()
    
    def decrease_user_score(self):
        self.p.score_user -=1
        self.update_points()
    
    def writing_to_file(self):
        with open("points.txt", "w") as f:
            f.write(f"{self.p.score_computer}\n{self.p.score_user}")


    
class Timer:
    def __init__(self):
        self.t = turtle.Turtle()
        self.start_time = time.time()  # Initialize start time when Timer object is created

    def display_timer(self):
        current_time = int(time.time() - self.start_time)
        remaining = max(0, 5 - current_time)

        self.t.clear()
        self.t.penup()
        self.t.goto(0, 230)
        self.t.write(f"Time left: {remaining} seconds", align="center", font=("Arial", 24, "normal"))
        self.t.pendown()
        self.t.hideturtle()

        if current_time < 5:
            turtle.ontimer(self.display_timer, 1000)





