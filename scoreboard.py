from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 18, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 270)
        self.screen_score()

    def screen_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.screen_score()

    #def end_game(self):
    #   self.goto(0,0)
    #    self.write("GAME OVER 😥", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.screen_score()
