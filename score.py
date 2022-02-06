from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.pensize(5)

        self.hideturtle()
        self.left_score = 0
        self.right_score = 0





    def update_scoreboard(self):
        self.clear()
        self.goto(0, -300)
        while self.ycor() < 300:
            self.pendown()
            self.goto(0, self.ycor()+10)
            self.penup()
            self.goto(0, self.ycor() + 20)

        self.goto(-100, 180)
        self.write(self.left_score, move=False, align='center', font=('Courier', 88, 'normal'))
        self.goto(100, 180)
        self.write(self.right_score, move=False, align='center', font=('Courier', 88, 'normal'))


    def left_scored(self):
        # self.clear()
        self.left_score += 1
        # self.goto(100, 250)
        # self.write(self.left_score, move=False, align='left', font=('Arial', 32, 'normal'))




    def right_scored(self):
        # self.clear()
        self.right_score += 1
        # self.goto(-100, 250)
        # self.write(self.right_score, move=False, align='left', font=('Arial', 32, 'normal'))


