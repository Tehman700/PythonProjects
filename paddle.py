from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=8, stretch_len=1)
        self.penup()
        self.goto(position)

    def uppp(self):
        y = self.ycor()
        if y < 250:  
            self.sety(y + 20)

    def downnnn(self):
        y = self.ycor()
        if y > -240: 
            self.sety(y - 20)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()  
        
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 260)
        self.write(f"Player 1: {self.score_left}", align="center", font=("Courier", 24, "normal"))
        self.goto(100, 260)
        self.write(f"Player 2: {self.score_right}", align="center", font=("Courier", 24, "normal"))

    def increase_score_left(self):
        self.score_left += 1
        self.update_scoreboard()

    def increase_score_right(self):
        self.score_right += 1
        self.update_scoreboard()
