from singletones import camera, input_handler, window
from game_logic import GameLogic
from ui_logic import UILogic
from constants import Colors
from time import time
import pygame as pg


class Scene:
    def __init__(self):
        self.game_logic = GameLogic([])
        self.ui_logic = UILogic([])

    def render(self):
        window.fill(Colors.BACKGROUND)
        culled_objects = camera.cull_objects(self.game_logic.game_objects)
        objects_to_render = culled_objects + self.ui_logic.ui_elements
        for object_to_render in objects_to_render:
            object_to_render.draw()

        pg.display.flip()

    def run(self):
        while True:
            start_time = time()
            input_handler.process_input()
            if 'quit' in input_handler.events:
                break
            self.game_logic.process_input(input_handler.events)
            self.render()
            print('\r\r\r\r\r\r', end='')
            print(int(1 / (time() - start_time)), end='')


