from turtle import Turtle
import random




class Bar:
    def __init__(self):
        self.all_bars = []





    def create(self):
        number = random.randint(1,6)
        if number == 6:
            def change_color(self):
                R = random.random()
                B = random.random()
                G = random.random()

                self.color(R, G, B)
        
            n = Turtle("square")
            n.shapesize(1,2)
            change_color(n)
            n.penup()
            number = random.randint(-240,270)
            n.goto(300,number)
            self.all_bars.append(n)
    
    def moving(self):
        for bb in self.all_bars:
            bb.backward(10)



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(25,265)
        self.write(f"Score: {self.score}",align="center", font=("Arial",20,"normal"))

    def increase(self):
        self.score+=1
        self.update_scoreboard()

    def drrr(self):
        self.score = 0
        self.update_scoreboard()