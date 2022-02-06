from turtle import Turtle
import heroes

class Palette(Turtle):

    def __init__(self):
        super().__init__()
        self.left_palette()
        self.right_palette()


    def right_palette(self):
        self.right = heroes.gen()
        x = 350
        y = 0
        self.right = Turtle("square")
        self.right.penup()
        self.right.color("white")
        self.right.shapesize(stretch_wid=5, stretch_len=1)
        self.right.setheading(0)
        self.right.setposition(x, y)



    def left_palette(self):
        self.left = heroes.gen()
        x = -350
        y = 0
        self.left = Turtle("square")
        self.left.penup()
        self.left.color("white")
        self.left.shapesize(stretch_wid=5, stretch_len=1)
        self.left.setheading(0)
        self.left.setposition(x, y)

    def left_up(self):
        y = self.left.ycor()
        x = self.left.xcor()
        if y < 250:
            self.left.goto(x, y+20)


    def left_down(self):
        y = self.left.ycor()
        x = self.left.xcor()
        if y > -340:
            self.left.goto(x, y - 20)

    def right_down(self):
        y = self.right.ycor()
        x = self.right.xcor()
        if y > -340:
            self.right.goto(x, y - 20)
            return True


    def right_up(self):
        y = self.right.ycor()
        x = self.right.xcor()
        if y < 340:
            self.right.goto(x, y + 20)
            return True



    # def move(self, name):
        # for n in range(len(self.left) - 1, 0, -1):
        #     positionx = self.left[n-1].xcor()
        #     positiony = self.left[n - 1].ycor()
        #     self.left[n].goto(positionx, positiony)
        # # screen.onkeypress(key="d", fun=snake_names[0].right(90))
        # self.left[0].forward(20)





