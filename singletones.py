import pygame as pg
from camera import Camera
from input_handler import InputHandler


window = pg.display.set_mode((900, 500))
pg.display.set_caption('RTShapes')
camera = Camera()
input_handler = InputHandler()
scene = None

