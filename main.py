from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

HEIGHT = 600
WIDTH = 850

screen = Screen()
screen.title('pong')
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('black')
screen.tracer(0)

p1 = Paddle(-400)
p2 = Paddle(390)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(p1.up, 'w')
screen.onkeypress(p1.down, 's')
screen.onkeypress(p2.up, 'Up')
screen.onkeypress(p2.down, 'Down')

is_game_on = True

while is_game_on:
    ball.move()
    screen.update()
    # detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if p2.distance(ball) < 50 and ball.xcor() > 370 or p1.distance(ball) < 50 and ball.xcor() < -380:
        ball.bounce_x()
        ball.increase_speed()

    # detect if the ball goes out of bounds
    if ball.xcor() > 400:
        ball.reset_pos()
        ball.reset_speed()
        scoreboard.increase_score_p1()
        screen.update()
        time.sleep(0.5)

    if ball.xcor() < - 410:
        ball.reset_pos()
        ball.reset_speed()
        scoreboard.increase_score_p2()
        screen.update()
        time.sleep(0.5)

screen.exitonclick()