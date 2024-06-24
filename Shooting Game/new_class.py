from turtle import Screen, Turtle
import random

# Create a screen object and add the car1.gif shape
scr = Screen()
scr.addshape('car1.gif')


class Car:
    def __init__(self):
        self.all_cars = []

    def create(self):
        number = random.randint(1, 25)
        if number == 6:
            new_car = Turtle('car1.gif')  # Assuming you have 'car1.gif' as your car image
            new_car.penup()
            new_car.goto(0, 300)  # Randomize x, start from top of screen (y=300)
            self.all_cars.append(new_car)

    def moving(self, speed):
        for car in self.all_cars:
            car.sety(car.ycor() - speed)  # Move the car downwards

    

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.load_highscore()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(25, 265)
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Arial", 20, "normal"))
    
    def increase(self):
        self.score += 1
        self.update_scoreboard()
    
    def reset_score(self):
        self.score = 0
        self.update_scoreboard()
    
    def load_highscore(self):
        try:
            with open("texting.txt", mode="r") as file:
                highscore = int(file.readline().strip())
        except (FileNotFoundError, ValueError):
            highscore = 0
        return highscore
    
    def save_highscore(self, highscore):
        with open("texting.txt", mode="w") as file:
            file.write(f"{highscore}\n")
    
    def check_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore(self.highscore)
        self.update_scoreboard()



