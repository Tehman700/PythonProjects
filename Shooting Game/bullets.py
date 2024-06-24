import turtle
import time
scr = turtle.Screen()
scr.addshape('user_shooter.gif')
scr.addshape('computer_shooter.gif')
scr.addshape('bullet.gif')



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

