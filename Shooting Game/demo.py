from turtle import Screen, Turtle
import random

scr = Screen()
scr.addshape('car1.gif')
scr.addshape('car2.gif')
scr.addshape('car3.gif')
scr.addshape('car4.gif')


class Car:
    def __init__(self):
        self.all_cars = []

    def create(self,model,position):
        number = random.randint(1,700)
        if number == 6:
            new_car = Turtle(model) 
            new_car.penup()
            new_car.goto(position)  
            self.all_cars.append(new_car)

    def moving(self, speed):
        for car in self.all_cars:
            car.sety(car.ycor() + speed)





class Down:
    def __init__(self):
        self.all_down = []

    def create_down(self,model,position):
        number = random.randint(1,900)
        if number == 6:
            new_car = Turtle(model)  
            new_car.penup()
            new_car.goto(position) 
            self.all_down.append(new_car)

    def moving_down(self, speed):
        for car in self.all_down:
            car.sety(car.ycor() - speed)


