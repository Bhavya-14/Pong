from turtle import Turtle

FONT = ('Courier', 60, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.p1_score = 0
        self.p2_score = 0
        self.color('white')
        self.refresh()

    def increase_score_p1(self):
        self.p1_score += 1
        self.refresh()

    def increase_score_p2(self):
        self.p2_score += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.setpos(-100, 230)
        self.write(self.p1_score, align='center', font=FONT)
        self.setpos(100, 230)
        self.write(self.p2_score, align='center', font=FONT)
