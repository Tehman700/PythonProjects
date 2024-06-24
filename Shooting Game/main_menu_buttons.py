import turtle

class Button:
    def __init__(self,position,letter_poss,letter, letter_size =23):
        super().__init__()
        self = turtle.Turtle()
        self.hideturtle()

        self.penup()
        self.goto(position)

        self.pendown()

        for i in range(2):
            self.forward(170)
            self.left(90)
            self.forward(50)
            self.left(90)

        self.penup()
        self.goto(letter_poss)
        self.write(letter, font = ("Arial", letter_size, 'normal'))



