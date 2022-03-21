from constants import Physics
import numpy as np


class Collider:
    def __init__(self, center):
        self.projections = np.zeros((Physics.COLLIDER_RES, 2, 2))
        self.longest_diag = 0
        self.center = np.array(center)

    def collides(self, other):
        pass


class Circle(Collider):
    def __init__(self, center, radius):
        super().__init__(center)
        self.radius = radius

    def collides(self, other):
        if type(other) == Circle:
            return np.linalg.norm(self.center - other.center) <= self.radius + other.radius
        if type(other) == Rectangle:
            return other.rect[0] <= self.center[0] <= other.rect[2] and other.rect[1] <= self.center[1] <= other.rect[3]


class Rectangle(Collider):
    def __init__(self, center, rect):
        super().__init__(center)
        self.rect = np.array(rect)

    def collides(self, other):
        if type(other) == Circle:
            return other.has_collision(self)
        if type(other) == Rectangle:
            for i in range(4):
                if other.rect[0] <= self.rect[(i // 2) * 2] <= other.rect[2] \
                        and other.rect[1] <= self.rect[(i % 2) * 2 + 1] <= other.rect[3]:
                    return True

            return other.rect[0] <= self.rect[0] <= self.rect[2] <= other.rect[2] and \
                   self.rect[1] <= other.rect[1] <= other.rect[3] <= self.rect[3]
