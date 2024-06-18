import pygame as pg
import random
class draw_tochka:
    def __init__(self):
        self.pos={"x":320,
                  "y":240}
        self.cpos={"x":160,
                  "y":120}
    def coin(self, display):
        pg.draw.circle(display, [0, 255, 0], [self.cpos["x"], self.cpos["y"]], 40.0)
        if self.pos["x"]==self.cpos["x"] and self.pos["y"]==self.cpos["y"]:
            self.cpos["x"] = round(random.randrange(0, 640 - 40) / 40) * 40
            self.cpos["y"] = round(random.randrange(0, 480 - 40) / 40) * 40
    def one_left(self, display, colour, speed):
        if self.pos["x"]==0:
            pass
        else:
            display.fill((0, 0, 0))
            self.pos["x"]-=speed
            pg.draw.rect(display, colour, [self.pos["x"], self.pos["y"], 40, 40])

    def one_right(self, display, colour, speed):
        if self.pos["x"]==600:
            pass
        else:
            display.fill((0, 0, 0))
            self.pos["x"]+=speed
            pg.draw.rect(display, colour, [self.pos["x"], self.pos["y"], 40, 40])
    def one_down(self, display, colour, speed):
        if self.pos["y"]>400:
            pass
        else:
            display.fill((0, 0, 0))
            self.pos["y"]+=speed
            pg.draw.rect(display, colour, [self.pos["x"], self.pos["y"], 40, 40])
    def one_up(self, display, colour, speed):
        if self.pos["y"]==0:
            pass
        else:
            display.fill((0, 0, 0))
            self.pos["y"]-=speed
            pg.draw.rect(display, colour, [self.pos["x"], self.pos["y"], 40, 40])