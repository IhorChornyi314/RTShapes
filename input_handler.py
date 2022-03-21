import pygame as pg
import json


class InputHandler:
    def __init__(self):
        self.events = []
        self.keybinds = json.load(open('inputs.json', 'r'))
        self.current_held_keys = {}

    def process_input(self):
        current_time = pg.time.get_ticks()
        self.events = []
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.events.append('quit')
                return
            if event.type == pg.KEYDOWN or event.type == pg.KEYUP:
                code = 'E_K%d_D' % event.key if event.type == pg.KEYDOWN else 'E_K%d_U' % event.key
                if code in self.keybinds:
                    self.events.append(self.keybinds[code]['action'])

            if event.type == pg.MOUSEBUTTONDOWN or event.type == pg.MOUSEBUTTONUP:
                code = ('E_M%d_D' if event.type == pg.MOUSEBUTTONDOWN else 'E_M%d_U') % event.button
                if code in self.keybinds:
                    self.events.append(self.keybinds[code]['action'])
        keys_down = [i for i in range(len(pg.key.get_pressed())) if pg.key.get_pressed()[i] == 1]

        for key in keys_down:
            code = 'S_K%d' % key
            if code not in self.keybinds:
                continue
            if code not in self.current_held_keys:
                self.current_held_keys[code] = {'start_time': current_time}
            if current_time - self.current_held_keys[code]['start_time'] < self.keybinds[code]['start_cd']:
                continue
            if 'last_cd_time' not in self.current_held_keys[code] or current_time - self.current_held_keys[code]['last_cd_time'] >= self.keybinds[code]['continue_cd']:
                self.current_held_keys[code]['last_cd_time'] = current_time
                self.events.append(self.keybinds[code]['action'])


