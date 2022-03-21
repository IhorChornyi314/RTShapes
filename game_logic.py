from game_objects import select
from game_objects.units import drone
from singletones import camera
import constants
import pygame as pg


class GameLogic:
    def __init__(self, game_objects):
        self.game_objects = game_objects

    def process_input(self, events):
        for event in events:
            method = getattr(self, event, 0)
            if method != 0:
                method()

    def debug_spawn(self):
        self.game_objects.append(drone.Drone(color=constants.Colors.DRONE_1, coords=camera.screen_to_world(*pg.mouse.get_pos())))

    def start_select(self):
        self.game_objects.append(select.Select(camera.screen_to_world(*pg.mouse.get_pos())))

    def stop_select(self):
        for o in self.game_objects:
            if type(o) == select.Select:
                self.game_objects.remove(o)

    def test_performance(self):
        for i in range(1000):
            self.game_objects.append(
                drone.Drone(color=constants.Colors.DRONE_1, coords=camera.screen_to_world(i / 500, i % 900)))
