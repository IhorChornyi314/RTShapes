import pygame as pg


class Camera:
    def __init__(self):
        self.rect = pg.Rect(0, 0, 900, 500)
        self.cull_distance = 100
        self.zoom = 1

    def screen_to_world(self, x, y):
        return x + self.rect[0], y + self.rect[1]

    def world_to_screen(self, x, y):
        return x - self.rect[0], y - self.rect[1]

    def translate_distance(self, original):
        return original * self.zoom

    def cull_objects(self, objects):
        result = []
        for o in objects:
            if self.rect.colliderect(o.rect) or o.ui:
                result.append(o)
        return result


