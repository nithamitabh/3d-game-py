import pygame as pg
import sys
from settings import *
class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
    def new_game(self):
        pass
    def update(self):
        pg.display.flip()
        self.clock.tips(FPS)
    def draw(self):
        self.screen.fill('black')
    def check_events(self):
        for event in    
    def run(self):
        while True:
               self.update()
               self.draw() 

    