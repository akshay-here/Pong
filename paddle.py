from turtle import Turtle

"""
Paddle is subclass
Turtle is super class
"""


class Paddle(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape('square')
        self.hideturtle()
        self.color(color)
        """
        All turtle start off at 20X20 pixels, So to get 20 pixels wide and 100 pixels height, 
        have to stretch width by 1(20*1 = 20), have to stretch height by 5(20*5 = 100)
        """
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)
        self.setheading(90)
        self.showturtle()
        self.paddle_speed = 0.1

    def move_up(self):
        self.fd(30)

    def move_down(self):
        self.bk(30)

