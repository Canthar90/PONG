from turtle import Screen
from palettes import Palette
import time
from paddles import Palette
from ball import Ball
import random
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
l_palett = Palette(-350, 0)
r_palett = Palette(350, 0)
ball = Ball()
score = Score()
screen.listen()
screen.tracer()
game_on=True
screen.onkeypress(fun=l_palett.move_up, key="w")
screen.onkeypress(fun=l_palett.move_down, key="s")
screen.onkeypress(fun=r_palett.move_up, key="Up")
screen.onkeypress(fun=r_palett.move_down, key="Down")

right_move_down = False
right_move_up = False
no_wall_on_top = False
no_wall_on_bottom = False
x_move = 10
y_move = 10
score.update_scoreboard()
time_of_sleep = 0.1
while game_on:
    time.sleep(time_of_sleep)

    ball.ball_move(x_move, y_move)
    screen.update()
    # print(ball.ycor())
    # print(l_palett.ycor())
    # print(l_palett.xcor())
    if ball.ycor() > 270 or ball.ycor() < -270:
        y_move *= -1
        # x_move += random.randint(1, 5)
    elif (ball.distance(r_palett) < 50 and ball.xcor() > 325) or (ball.distance(l_palett) < 50 and ball.xcor() < -325):
        y_move +=random.randint(1, 5)
        x_move *= -1
        time_of_sleep *= 0.9
        x_move = x_move*(1 + random.uniform(0, 0.2))
    # elif ball.distance(l_palett) < 50 and ball.xcor() < -325:
    #     y_move += random.randint(1, 5)
    #     x_move *= -1
        # x_move = x_move*(1 + random.uniform(0, 0.5))

    if ball.xcor() > 360:
        ball.ball_reset()
        y_move = 10 * random.randint(-2, 2)
        x_move = 10
        score.left_scored()
        score.update_scoreboard()
        time_of_sleep = 0.1
    elif ball.xcor() < -360:
        ball.ball_reset()
        y_move = 10 * random.randint(-2, 2)
        x_move = -10
        score.right_scored()
        score.update_scoreboard()
        time_of_sleep = 0.1




















screen.exitonclick()