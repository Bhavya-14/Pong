from turtle import Turtle
import time


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x_move = 4
        self.y_move = 4

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def reset_pos(self):
        time.sleep(0.3)
        self.goto(x=0, y=0)
        self.bounce_x()

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def increase_speed(self):
        self.x_move += 1

    def reset_speed(self):
        self.x_move = 3
