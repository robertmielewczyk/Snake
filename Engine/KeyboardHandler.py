import pygame
from Directions import Directions
from Snake import Snake

class KeyboardHandler:
    '''
    :param snake:instance of class snake
    :type snake: Snake
    '''
    def key_preesed(snake):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.change_direction(Directions.LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(Directions.RIGHT)
                elif event.key == pygame.K_UP:
                    snake.change_direction(Directions.UP)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(Directions.DOWN)
                elif event.key == pygame.K_g:
                    snake.grow()