from turtle import Screen, Turtle
import random

# Create a screen object and add the car1.gif shape
scr = Screen()
scr.addshape('car1.gif')
scr.addshape('car2.gif')
scr.addshape('car3.gif')
scr.addshape('car4.gif')


class Car:
    def __init__(self):
        self.all_cars = []

    def create(self):
        number = random.randint(1,700)
        if number == 6:
            new_car = Turtle('car1.gif')  # Assuming you have 'car1.gif' as your car image
            new_car.penup()
            new_car.goto(-70,-300)  # Randomize x, start from top of screen (y=300)
            self.all_cars.append(new_car)

    def moving(self, speed):
        for car in self.all_cars:
            car.sety(car.ycor() + speed)
              # Move the car downwards