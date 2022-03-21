from game_objects.game_object import GameObject


class Unit(GameObject):
    def __init__(self, *args, color=(255, 255, 255), **kwargs):
        super().__init__(*args, **kwargs)
        self.color = color
        self.target = None
        self.direction = (0, 0)
        self.speed = 0
        self.selected = False

    def move(self):
        self.rect[0] += self.direction[0] * self.speed
        self.rect[1] += self.direction[1] * self.speed



