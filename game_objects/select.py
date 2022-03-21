from game_objects.game_object import GameObject
from singletones import window
from constants import Colors
from collider import Rectangle
from pygame import draw, mouse
import pygame as pg


class Select(GameObject):
    def __init__(self, start_coordinates=(0, 0), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.collider = Rectangle(start_coordinates, start_coordinates + start_coordinates)
        self.ui = True
        self.coords = start_coordinates + (0, 0)

    def draw(self):
        self.coords = self.coords[0:2] + mouse.get_pos()
        self.collider.rect[:] = self.coords
        draw.lines(window, Colors.SELECT, True, (
            self.coords[0:2], (self.coords[0], self.coords[3]), self.coords[2:4], (self.coords[2], self.coords[1])
        ), width=1)
        pg.display.flip()


