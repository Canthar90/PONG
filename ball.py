from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.k=10
        self.l=10
        # self.ball_move(self.k, self.l)


    def ball_move(self, k, l):
        x = self.xcor()
        y = self.ycor()
        self.goto(x+k, y+l)
        # self.ball_move(self.k, self.l)

    def ball_reset(self):
        self.goto(0, 0)