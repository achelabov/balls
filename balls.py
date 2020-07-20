import tkinter as tk
from random import randint as rnd

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self):
        self.route_x = rnd(-3, 4)
        self.route_y = rnd(-3, 4)
        self.x = rnd(100, 700)
        self.y = rnd(100, 500)
        self.r = rnd(30, 50)
        self.ball_color = self.painting_ball()
        self.ball = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                                     fill=self.ball_color[rnd(0, len(self.ball_color) - 1)])

    def painting_ball(self):
        self.colors = ['red', 'orange', 'yellow', 'green', 'blue']
        return self.colors

    def move_ball(self):
        self.x += self.route_x
        self.y += self.route_y
        canv.move(self.ball, self.route_x, self.route_y)

    def bounce_ball(self):
        if self.x - self.r <= 0:
            if self.route_x != 0:
                self.route_x = -self.route_x
        if self.x + self.r >= WIDTH:
            if self.route_x != 0:
                self.route_x = -self.route_x
        if self.y + self.r >= HEIGHT:
            if self.route_y != 0:
                self.route_y = -self.route_y
        if self.y - self.r <= 0:
            if self.route_y != 0:
                self.route_y = -self.route_y


def add_balls():
    for ball in balls:
        ball.move_ball()
        ball.bounce_ball()
    root.after(50, add_balls)


def main():
    global root, canv, balls
    root = tk.Tk()
    root.geometry('{}x{}'.format(WIDTH, HEIGHT))
    canv = tk.Canvas(root, bg='white')

    ball_count = 6

    balls = [Ball() for ball in range(ball_count)]

    add_balls()
    canv.pack(fill=tk.BOTH, expand=1)
    root.mainloop()


if __name__ == '__main__':
    main()
