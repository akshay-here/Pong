from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.penup()
        self.color("White")
        self.update_score()

    def update_score(self):
        self.clear()        #so that score doesn't get overwritten on top every time
        self.goto(x=100, y=250)
        self.color("Red")       #When blue misses red gets a point
        self.write(f"{self.r_score}", align='center', font=('Arial', 30, 'normal'))
        self.goto(-100, 250)
        self.color("Blue")      #When red misses blue gets a point
        self.write(f"{self.l_score}", align='center', font=('Arial', 30, 'normal'))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
