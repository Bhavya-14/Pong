from turtle import Turtle

PADDLE_DISTANCE = 30


class Paddle(Turtle):

    def __init__(self, x_pos):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.setpos(x_pos, 0)

    def up(self):
        self.fd(PADDLE_DISTANCE)

    def down(self):
        self.bk(PADDLE_DISTANCE)
