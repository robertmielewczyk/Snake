from GameObjects.GameObject import GameObject
from Settings.InitParameters import InitParameters
import pygame

class GridRectangle(GameObject):
    '''
    Puts a rectangle on grid in a specified position
    :param x: x position on grid (from left)
    :type x: int
    :param y: y position on grid (from top)
    :type y: int
    :param color: rectangle color (r,g,b) [0-255]
    :type color: tuple
    '''
    def __init__(self, x, y, color):
        self.x_pos = x
        self.y_pos = y
        self.color = color

    def draw(self, surface):
        dis = InitParameters.GRID_DISTANCE
        pygame.draw.rect(surface, self.color, (self.x_pos * dis, self.y_pos * dis, dis, dis))

    def __eq__(self, object):
        return isinstance(object, GridRectangle) and self.x_pos == object.x_pos and self.y_pos == object.y_pos

