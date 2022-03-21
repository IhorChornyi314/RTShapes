import constants
import pygame as pg


class UILogic:
    def __init__(self, ui_elements):
        self.ui_elements = ui_elements

    def process_input(self, events):
        if constants.Events.UI_INTERACT in events:
            mouse_pos = pg.mouse.get_pos()
            for ui_element in self.ui_elements:
                if mouse_pos in ui_element:
                    ui_element.activate()
                    return True
        return False


