from turtle import Turtle
import heroes

class Palette(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setheading(0)
        self.setposition(x, y)


    def move_up(self):
        y = self.ycor()
        x = self.xcor()
        if y < 240:
            self.goto(x, y + 20)


    def move_down(self):
        y = self.ycor()
        x = self.xcor()
        if y > -240:
            self.goto(x, y - 20)
