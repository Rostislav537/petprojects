import pygame as pg
import  ppp as p
import  random
clock = pg.time.Clock()
f=p.draw_tochka()
cpos={"x":160,
      "y":120}
pg.init()
width = 640
height = 480
display = pg.display.set_mode((width, height))
pg.display.update()
game_end = False
f1 = pg.font.Font(None, 24)
score=0



pg.draw.rect(display, [0, 255, 0], [cpos["x"], cpos["y"], 40, 40])
while not game_end:
    # game loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game_end = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                f.one_left(colour=[255, 0, 0], display=display, speed=40)
            elif event.key == pg.K_RIGHT:
                f.one_right(colour=[255, 0, 0],display=display, speed=40 )
            elif event.key == pg.K_UP:
                f.one_up(colour=[255, 0, 0],display=display, speed=40 )
            elif event.key == pg.K_DOWN:
                f.one_down(colour=[255, 0, 0],display=display, speed=40 )

        if f.pos["x"] == cpos["x"] and f.pos["y"] == cpos["y"]:
            cpos["x"] = round(random.randrange(0, 640 - 40) / 40) * 40
            cpos["y"] = round(random.randrange(0, 480 - 40) / 40) * 40
            score+=1
        pg.draw.rect(display, [0, 255, 0], [cpos["x"], cpos["y"], 40, 40])
    text = f1.render(str(score), True, (0, 180, 0))
    display.blit(text, (40, 40))
    pg.display.update()
    clock.tick(30)
pg.quit()
quit()