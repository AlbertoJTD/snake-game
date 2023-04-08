from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 18, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_highest_score()
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
            self.set_highest_score(self.high_score)
        self.score = 0
        self.screen_score()

    def get_highest_score(self):
        with open('data.txt') as file:
            return  int(file.read())

    def set_highest_score(self, value):
        with open('data.txt', mode='w') as file:
            file.write(f'{value}')
