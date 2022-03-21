from singletones import window, camera
import pygame as pg


class GameObject:
    def __init__(self, coords=(0, 0), dimensions=(0, 0), *args, **kwargs):
        self.rect = pg.Rect(*(coords + dimensions))
        self.ui = False
        pass

    def draw(self):
        pass





