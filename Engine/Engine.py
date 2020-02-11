from Settings.InitParameters import InitParameters
import pygame

class Engine:
    '''
    Initializes PyGame
    '''
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake")
        self.window = pygame.display.set_mode((InitParameters.RESOLUTION, InitParameters.RESOLUTION))
        self.clock = pygame.time.Clock()

    '''
    Handles all drawing on screen
    '''
    def redraw(self, surface, objects):
        pygame.time.delay(100)
        self.clock.tick(10)
        surface.fill((0, 0, 0))
        for obj in objects:
            obj.draw(surface)
        self._draw_grid(surface)

        pygame.display.update()

    '''
    Draws grid on pygame window
    '''
    def _draw_grid(self, surface):
        x, y = 0, 0
        for l in range(InitParameters.RESOLUTION):
            x+=InitParameters.GRID_DISTANCE
            y+=InitParameters.GRID_DISTANCE

            pygame.draw.line(surface, (255,255,255), (x,0), (x, InitParameters.RESOLUTION))
            pygame.draw.line(surface, (255,255,255), (0, y), (InitParameters.RESOLUTION, y))

