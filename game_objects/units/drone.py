from game_objects.units import unit, unit_constants
from singletones import pg, camera, window


class Drone(unit.Unit):
    def __init__(self, *args, **kwargs):
        super().__init__(dimensions=(2 * unit_constants.DRONE_RADIUS, 2 * unit_constants.DRONE_RADIUS), *args, **kwargs)

    def draw(self):
        pg.draw.circle(
            window,
            self.color,
            camera.world_to_screen(*self.rect[:2]),
            camera.translate_distance(unit_constants.DRONE_RADIUS)
        )


