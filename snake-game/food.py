from random import randint
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize()
        self.color("tan")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(x=randint(-280, 280), y=randint(-280, 280))
