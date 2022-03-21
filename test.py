import pygame as pg
from time import time


pg.display.set_caption('RTShapes')
window = pg.display.set_mode((900, 500))
circle_sprite = pg.image.load('circle.png')
pg.font.init()
my_font = pg.font.SysFont('Comic Sans MS', 30)


def main():
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                break
        window.fill((200, 200, 200))
        cf = pg.Surface((20, 20), pg.SRCALPHA)

        pg.draw.circle(cf, (100, 100, 100, 100), (10, 10), 10)
        window.blit(cf, pg.mouse.get_pos())
        pg.display.flip()
    pg.quit()


if __name__ == '__main__':
    main()

