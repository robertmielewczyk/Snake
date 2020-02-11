from GameObjects.GameObject import GameObject
from GameObjects.GridRectangle import GridRectangle
from Settings.InitParameters import InitParameters
import random


class Apple(GameObject):
    def __init__(self):
        grid_size = InitParameters.GRID_SIZE
        x = random.randrange(0, grid_size)
        y = random.randrange(0, grid_size)
        blue_color = (0, 255, 0)
        self.positions = GridRectangle(x, y, blue_color)

    def place_random(self):
        grid_size = InitParameters.GRID_SIZE
        x = random.randrange(0, grid_size)
        y = random.randrange(0, grid_size)
        self.positions.x_pos = x
        self.positions.y_pos = y

    '''
    Invokes draw function in GridRectangle which draws using pygame
    '''
    def draw(self, surface):
        self.positions.draw(surface)
